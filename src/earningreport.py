"""
proventosreport.py

Script para processamento de planilha de proventos de investimentos.

Funcionalidades:
- Visão geral por ativo e tipo de evento
- Resumo mensal com gráficos
- Análise dos principais pagadores
- Guia de Imposto de Renda para cada provento

Autor: @fcardan
GitHub: https://github.com/fcardan
Data: 12/05/2025
Versão: 1.1
"""

import pandas as pd
import matplotlib.pyplot as plt
from openpyxl.drawing.image import Image
from io import BytesIO
import warnings
from typing import Tuple


# -----------------------------------------------------------------------------
# Configurações Globais e Constantes
# -----------------------------------------------------------------------------
warnings.filterwarnings(
    "ignore", category=UserWarning, module="openpyxl"
)
plt.style.use('default')  # Estilo padrão do matplotlib

# Caminhos de arquivo
INPUT_PATH: str = 'proventosb3.xlsx'
OUTPUT_PATH: str = 'resumo_proventos.xlsx'

# Nomes de planilhas
SHEET_VISAO: str = 'Visão Geral'
SHEET_RESUMO: str = 'Resumo Anual'
SHEET_IR: str = 'Imposto de Renda'

# Colunas esperadas no DataFrame
COLUNA_PRODUTO: str = 'Produto'
COLUNA_VALOR: str = 'Valor líquido'
COLUNA_TIPO: str = 'Tipo de Evento'
COLUNA_TICKER: str = 'Ticker'
COLUNA_MES: str = 'Mês'
COLUNA_DATA: str = 'Pagamento'

# Formatação e cores
FORMATO_MOEDA: str = 'R$ #,##0.00'
CORES: list[str] = ['#4CAF50', '#2196F3', '#FFC107', '#9C27B0']

# Legenda para aba "Imposto de Renda"
LEGEND_IR: list[list[str]] = [
    ['Item', 'Ficha', 'Grupo', 'Código'],
    ['Ações - Patrimônio Aplicado', 'Bens e Direitos', '03 - Participações Societárias', '01'],
    ['Dividendos', 'Rendimentos Isentos e Não Tributáveis', '-', '09'],
    ['Juros Sobre Capital Próprio Pago', 'Rendimentos Sujeitos à Tributação Exclusiva', '-', '10'],
    ['Juros Sobre Capital Próprio Declarado e não pago', 'Bens e Direitos', '99 - Outros Bens e Direitos', '07'],
    ['FIIs - Patrimônio Aplicado', 'Bens e Direitos', '07 - Fundos', '03'],
    ['Dividendos FIIs', 'Rendimentos Isentos e Não Tributáveis', '-', '09'],
]


# -----------------------------------------------------------------------------
# Funções Auxiliares
# -----------------------------------------------------------------------------

def formatar_valor_monetario(valor: str | int | float) -> float:
    """
    Converte valores monetários do formato brasileiro para float.

    Args:
        valor: Valor em 'R$ 1.000,50' ou numérico.

    Returns:
        float: Valor convertido.

    Raises:
        ValueError: Se não for possível converter.
    """
    if pd.isna(valor):
        return 0.0
    if isinstance(valor, (int, float)):
        return float(valor)

    # Remove símbolos e formata
    texto = str(valor).replace('R$', '').strip()
    texto = texto.replace('.', '').replace(',', '.')

    try:
        return float(texto)
    except ValueError as exc:
        raise ValueError(
            f"Não foi possível converter '{valor}' para float"
        ) from exc


def criar_grafico_pizza(dados: pd.DataFrame, titulo: str) -> BytesIO:
    """
    Cria gráfico de pizza para distribuição de valores por tipo.

    Args:
        dados: DataFrame com colunas ['Tipo', 'Valor'].
        titulo: Título do gráfico.

    Returns:
        BytesIO: Imagem PNG em buffer.
    """
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie(
        dados['Valor'],
        labels=dados['Tipo'],
        autopct='%1.1f%%',
        startangle=90,
        colors=CORES[:len(dados)]
    )
    ax.set_title(titulo)

    buffer = BytesIO()
    fig.savefig(buffer, format='png', dpi=120, bbox_inches='tight')
    plt.close(fig)
    buffer.seek(0)
    return buffer


def criar_grafico_linha(dados: pd.Series, titulo: str) -> BytesIO:
    """
    Cria gráfico de linha para evolução mensal de proventos.

    Args:
        dados: Series indexada por 'Mês/Ano' com valores.
        titulo: Título do gráfico.

    Returns:
        BytesIO: Imagem PNG em buffer.
    """
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(
        dados.index,
        dados.values,
        marker='o',
        linewidth=2.5,
        color=CORES[1]
    )
    ax.set_title(titulo)
    ax.set_xlabel(COLUNA_MES)
    ax.set_ylabel('Valor (R$)')
    ax.grid(linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)

    buffer = BytesIO()
    fig.savefig(buffer, format='png', dpi=120, bbox_inches='tight')
    plt.close(fig)
    buffer.seek(0)
    return buffer


def ajustar_largura_colunas(sheet) -> None:
    """
    Ajusta largura das colunas com base no conteúdo.
    """
    for coluna in sheet.columns:
        max_largura = max(
            len(str(celda.value)) for celda in coluna
        )
        letra = coluna[0].column_letter
        sheet.column_dimensions[letra].width = max_largura + 2


# -----------------------------------------------------------------------------
# Processamento de Dados
# -----------------------------------------------------------------------------

def processar_dados(df: pd.DataFrame) -> Tuple[pd.DataFrame, float]:
    """
    Limpa e prepara DataFrame de entrada para análises.

    - Remove linhas sem produto ou valor
    - Converte datas
    - Normaliza valores
    - Extrai campo Ticker e Mês/Ano

    Returns:
        df_limpo (DataFrame), total_anual (float)
    """
    # Filtra linhas vazias ou totais
    df = df.dropna(subset=[COLUNA_PRODUTO, COLUNA_VALOR], how='all')
    df = df[~df[COLUNA_PRODUTO].astype(str).str.match(r'^\s*$|Total')]

    # Datas e valores
    df[COLUNA_DATA] = pd.to_datetime(
        df[COLUNA_DATA], dayfirst=True, errors='coerce'
    )
    df = df.dropna(subset=[COLUNA_DATA])
    df[COLUNA_VALOR] = df[COLUNA_VALOR].apply(formatar_valor_monetario)

    # Colunas derivadas
    df['Mês/Ano'] = df[COLUNA_DATA].dt.strftime('%m/%Y')
    df[COLUNA_MES] = df[COLUNA_DATA].dt.strftime('%Y-%m')
    df[COLUNA_TICKER] = (
        df[COLUNA_PRODUTO].str.split(' - ').str[0].str.strip()
    )

    total_anual = round(df[COLUNA_VALOR].sum(), 2)
    return df, total_anual


def gerar_visao_geral(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, BytesIO]:
    """
    Gera relatório "Visão Geral" e gráfico de pizza.
    """
    # Pivot por ticker e tipo
    tabela_visao = df.groupby([
        COLUNA_TICKER, COLUNA_TIPO
    ])[COLUNA_VALOR].sum().unstack(fill_value=0).round(2)

    # Top pagadores sem apply (idxmax)
    indices_top = df.groupby(COLUNA_TIPO)[COLUNA_VALOR].idxmax()
    top_pagadores = df.loc[
        indices_top, [COLUNA_TIPO, COLUNA_TICKER, COLUNA_VALOR]
    ].reset_index(drop=True)

    # Dados para pizza
    df_pizza = (
        df.groupby(COLUNA_TIPO)[COLUNA_VALOR]
        .sum().reset_index().rename(columns={
            COLUNA_TIPO: 'Tipo', COLUNA_VALOR: 'Valor'
        })
    )
    graf_pizza = criar_grafico_pizza(df_pizza, 'Distribuição por Tipo')
    return tabela_visao, top_pagadores, graf_pizza


def gerar_resumo_anual(df: pd.DataFrame) -> Tuple[pd.DataFrame, BytesIO]:
    """
    Gera tabela e gráfico para resumo anual.
    """
    resumo = (
        df.groupby([COLUNA_MES, 'Mês/Ano'])[COLUNA_VALOR]
        .sum().reset_index().sort_values(COLUNA_MES)
    )
    resumo['Acumulado'] = resumo[COLUNA_VALOR].cumsum().round(2)

    serie = resumo.set_index('Mês/Ano')[COLUNA_VALOR]
    graf_linha = criar_grafico_linha(serie, 'Evolução Mensal')
    return resumo, graf_linha


def criar_relatorio_excel(
    df_visao: pd.DataFrame,
    df_top: pd.DataFrame,
    graf_pizza: BytesIO,
    df_resumo: pd.DataFrame,
    graf_linha: BytesIO,
    total_anual: float
) -> None:
    """
    Cria e formata o arquivo Excel com as três abas.
    """
    with pd.ExcelWriter(OUTPUT_PATH, engine='openpyxl') as writer:
        # Aba Visão Geral
        df_visao.to_excel(
            writer, sheet_name=SHEET_VISAO, startrow=0
        )
        df_top.to_excel(
            writer, sheet_name=SHEET_VISAO,
            startrow=len(df_visao) + 3,
            index=False
        )
        ws_visao = writer.sheets[SHEET_VISAO]
        ws_visao['A1'] = 'Visão Geral de Proventos'
        ws_visao[f'A{len(df_visao)+4}'] = 'Top Pagadores'
        ws_visao.add_image(
            Image(graf_pizza), f'F{len(df_visao)+4}'
        )

        # Aba Resumo Anual
        df_resumo.to_excel(
            writer, sheet_name=SHEET_RESUMO, index=False
        )
        ws_resumo = writer.sheets[SHEET_RESUMO]
        ws_resumo['A1'] = 'Resumo Anual'
        ws_resumo.add_image(
            Image(graf_linha), 'A15'
        )

        # Aba Imposto de Renda
        book = writer.book
        ws_ir = book.create_sheet(SHEET_IR)
        for linha in LEGEND_IR:
            ws_ir.append(linha)

        # Formatação geral
        for aba in writer.sheets.values():
            ajustar_largura_colunas(aba)
            for row in aba.iter_rows():
                for cell in row:
                    if isinstance(cell.value, (int, float)):
                        cell.number_format = FORMATO_MOEDA

        # Total Anual ao final da primeira aba
        ws_visao[f'A{len(df_visao)+6}'] = (
            f"Total Anual: {total_anual:,.2f}".replace('.', '|')
            .replace(',', '.').replace('|', ',')
        )


def main() -> None:
    """
    Função principal: executa todo o fluxo.
    """
    try:
        df_original = pd.read_excel(INPUT_PATH, engine='openpyxl')
        df_limpo, total = processar_dados(df_original)
        visao, top, pizza = gerar_visao_geral(df_limpo)
        resumo, linha = gerar_resumo_anual(df_limpo)
        criar_relatorio_excel(visao, top, pizza, resumo, linha, total)
        print(f"Relatório gerado em '{OUTPUT_PATH}' com sucesso.")
    except Exception as error:
        print(f"Falha ao gerar relatório: {error}")


if __name__ == '__main__':
    main()
