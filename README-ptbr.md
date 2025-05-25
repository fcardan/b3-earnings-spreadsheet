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
- [Configuração](#configuração)
- [Instalação e Uso](#instalação-e-uso)
- [Saída Gerada](#saída-gerada)
- [Fluxo de Trabalho](#fluxo-de-trabalho)
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

## Instalação e Uso

Siga os passos abaixo para instalar e executar o projeto de forma correta, seja no Windows, Linux ou macOS:

#### 1. Clone o repositório

Baixe os arquivos do projeto com o comando abaixo. Isso criará uma nova pasta chamada `b3-earnings-spreadsheet`.

```bash
git clone https://github.com/fcardan/b3-earnings-spreadsheet.git
```

#### 2. Acesse a pasta do projeto
Entre na pasta clonada:

```bash
cd b3-earnings-spreadsheet
```

#### 3. Instale as dependências
Você pode instalar as bibliotecas manualmente:

```bash
pip install pandas openpyxl matplotlib
```

Ou, de forma mais prática, usando o arquivo de requisitos:

```bash
pip install -r requirements.txt
```

#### 4. Verifique o diretório atual
Certifique-se de que está dentro da pasta onde o arquivo earningsreport.py está localizado. Você pode usar:

```bash
ls  # Linux/macOS
dir # Windows
```

#### 5. Execute o script
Execute o script conforme seu sistema operacional:

✅ Para Linux/macOS:
```bash
python3 earningsreport.py
```

✅ Para Windows:
```bash
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

## Fluxo de Trabalho

![fluxo-do-projeto](https://github.com/fcardan/b3-earnings-spreadsheet/blob/main/earningreport-workflow.png)

### Passo 1️⃣: Baixar os Dados

- **Acesse o site da B3**  
   Vá para [https://www.b3.com.br](https://www.b3.com.br) e faça login na sua conta.
- **Exporte seu histórico de proventos**  
   Baixe o arquivo Excel (ex. `planilha_historico.xlsx`) contendo todos os seus proventos (dividendos e distribuições).

### Passo 2️⃣: Processar os Dados

- Clone este repositório
- Ler Excel: o script carrega seu arquivo bruto em um DataFrame do Pandas.
- Processar Dados: realiza limpeza, agregação e cálculo de métricas-chave.
- Gerar Estatísticas: calcula totais, índices e tendências para cada ativo.

### Passo 3️⃣: Gerar Relatório
**Exportar nova planilha Excel**

Após o processamento, o script gera um novo arquivo `nova_planilha.xlsx` contendo:

- Resumo com proventos agregados por ticker e período

- Gráficos ilustrando distribuições mensais e top‑5

- Abra `nova_planilha.xlsx` no Excel ou qualquer ferramenta de planilha para analisar seu relatório de rendimentos atualizado.

---

## Licença
Este repositório está licenciado. Isso significa que você é livre para compartilhar e adaptar este conteúdo para qualquer propósito, inclusive comercialmente, desde que forneça os devidos créditos ao autor original. Para mais detalhes, consulte o arquivo [LICENSE.md]().
