![.](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyjrF64yMg2p0HUJFMxWJYRgvSwQweHVajqg&s)

# Analisador de Planilha de Proventos (B3 para IR)

[![🔥 Siga no GitHub](https://img.shields.io/badge/👉🏼-GitHub-white)](https://www.github.com/fcardan)
[![🔥 Siga no Linkedin](https://img.shields.io/badge/👉🏼-Linkedin-blue)](https://www.linkedin.com/in/fcardan)
[![⭐ en-us](https://img.shields.io/badge/👉🏼-EnUS-red)](https://github.com/fcardan/b3-earnings-spreadsheet)
[![⭐ Estrelas](https://img.shields.io/github/stars/fcardan/b3-earnings-spreadsheet)](https://github.com/fcardan/b3-earnings-spreadsheet)

Ferramenta em Python para analisar e visualizar dados de rendimentos de investimentos na B3 (bolsa de valores brasileira), incluindo dividendos, juros sobre capital próprio (JCP) e rendimentos de fundos imobiliários (FII).

---

## 🔹 Índice
- [Visão Geral](#visão-geral)
- [Problema Resolvido](#problema-resolvido)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Licença](#licença)

---

## Visão Geral
Automatiza a análise de proventos de investimentos, gerando:
- Relatórios consolidados por ativo e tipo de evento
- Gráficos de evolução mensal
- Diretrizes para declaração de imposto de renda
- Identificação dos maiores pagadores

---

## Problema Resolvido
Simplifica os processos manuais de:
1. Agregar rendimentos de diversas fontes
2. Calcular totais por ativo e período
3. Gerar visualizações analíticas
4. Preparar dados para a declaração de imposto

---

## Funcionalidades
✅ Visão Consolidada  
✅ Resumo Mensal com Gráficos  
✅ Maiores Pagadores por Categoria  
✅ Guia para Declaração de IR  
✅ Formatação Automática de Valores  
✅ Compatível com Excel (.xlsx)

---

## Tecnologias Utilizadas
- **Python 3.10+**: Lógica principal
- **Pandas**: Processamento de dados
- **Matplotlib**: Geração de gráficos
- **Openpyxl**: Integração com Excel

---

## Instalação
```bash
# Clonar o repositório
git clone https://github.com/fcardan/b3-earnings-spreadsheet.git

# Instalar dependências
pip install pandas openpyxl matplotlib

# OU instale tudo via arquivo de requisitos
pip install -r requirements.txt
```

---

## Configuração
- Coloque sua planilha na pasta do projeto
- Configure as constantes conforme necessário:

```python
# [DATA :: RAW] - Nome do seu arquivo
INPUT_PATH: str = 'proventosb3.xlsx'

# [DATA :: PROCESSED] - Nome do arquivo final
OUTPUT_PATH: str = 'resumo_proventos.xlsx'

# Planilha Final - Nome das Abas
SHEET_VISAO: str = 'Visão Geral'
SHEET_RESUMO: str = 'Resumo Anual'
SHEET_IR: str = 'Imposto de Renda'

# Planilha Final - Nome das Colunas
COLUNA_PRODUTO: str = 'Produto'
COLUNA_VALOR: str = 'Valor líquido'
COLUNA_TIPO: str = 'Tipo de Evento'
COLUNA_TICKER: str = 'Ticker'
COLUNA_MES: str = 'Mês'
COLUNA_DATA: str = 'Pagamento'
```

---

## Como usar
```bash
# Executar script (Windows)
python earningsreport.py
```

---

## Saída Gerada
- Nova planilha: resumo_proventos.xlsx (com 3 abas)
- Logs exibidos no console

_Os gráficos gerados abaixo foram extraído de valores testes._

![pie-chart](https://github.com/fcardan/b3-earnings-spreadsheet/blob/main/earningreport-dt.jpg)
![ev-chart](https://github.com/fcardan/b3-earnings-spreadsheet/blob/main/earningreport-link.jpg)

---

## Licença
Este repositório está licenciado. Isso significa que você é livre para compartilhar e adaptar este conteúdo para qualquer propósito, inclusive comercialmente, desde que forneça os devidos créditos ao autor original. Para mais detalhes, consulte o arquivo [LICENSE.md]().
