![.](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyjrF64yMg2p0HUJFMxWJYRgvSwQweHVajqg&s)

# Earnings Spreadsheet Analyzer (B3 to tax)

[![🔥 Follow my GitHub](https://img.shields.io/badge/👉🏼-GitHub-white)](https://www.github.com/fcardan)
[![🔥 Follow my Linkedin](https://img.shields.io/badge/👉🏼-Linkedin-blue)](https://www.linkedin.com/in/fcardan)
[![⭐ pt-br](https://img.shields.io/badge/👉🏼-PtBr-green)](https://github.com/fcardan/b3-earnings-spreadsheet/blob/main/README-ptbr.md)
[![⭐ Star](https://img.shields.io/github/stars/fcardan/b3-earnings-spreadsheet)](https://github.com/fcardan/b3-earnings-spreadsheet)

A Python tool to analyze and visualize investment income data from B3 (Brazilian stock exchange), including dividends, interest, and real estate fund (FII) distributions.

## 🔹Table of Contents
- [Overview](#overview)
- [Problem Solved](#problem-solved)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Configuration](#configuration)
- [Installation and Usage](#installation-and-usage)
- [Workflow](#workflow)
- [License](#license)

---

## Overview
Automates investment income analysis by generating:
- Consolidated reports by asset and event type
- Monthly evolution charts
- Tax declaration guidelines
- Top payer identification

---

## Problem Solved
Simplifies manual processes of:
1. Aggregating income from multiple sources
2. Calculating totals by asset and period
3. Generating analysis visualizations
4. Preparing fiscal declaration data

---

## Features
✅ Consolidated Overview  
✅ Monthly Summary with Charts  
✅ Top Payers by Category  
✅ Tax Declaration Guide  
✅ Automatic Value Formatting  
✅ Excel Compatibility (.xlsx)

---

## Tech Stack
- **Python 3.10+**: Core logic
- **Pandas**: Data processing
- **Matplotlib**: Chart generation
- **Openpyxl**: Excel integration

---

## Configuration
- Place your spreadsheet in project folder
- You can config the constants:
```bash
# [DATA :: RAW] - Name of your file
INPUT_PATH: str = 'proventosb3.xlsx'

# [DATA :: PROCESSED] - Final file name
OUTPUT_PATH: str = 'resumo_proventos.xlsx'

# Source Spreadsheet - Column Names
SHEET_VISAO: str = 'Visão Geral'
SHEET_RESUMO: str = 'Resumo Anual'
SHEET_IR: str = 'Imposto de Renda'

# Final Spreadsheet - Tab Names
COLUNA_PRODUTO: str = 'Produto'
COLUNA_VALOR: str = 'Valor líquido'
COLUNA_TIPO: str = 'Tipo de Evento'
COLUNA_TICKER: str = 'Ticker'
COLUNA_MES: str = 'Mês'
COLUNA_DATA: str = 'Pagamento'
```

---

## Installation and Usage

Follow the steps below to properly install and run the project on Windows, Linux, or macOS:

#### 1. Clone the repository

Download the project files using the command below. This will create a new folder named `b3-earnings-spreadsheet`.

```bash
git clone https://github.com/fcardan/b3-earnings-spreadsheet.git
```

#### 2. Navigate to the project folder
Enter the cloned folder:

```bash
cd b3-earnings-spreadsheet
```

#### 3. Install dependencies
You can install the required libraries manually:

```bash
pip install pandas openpyxl matplotlib
```

Or, more conveniently, use the requirements file:

```bash
pip install -r requirements.txt
```

#### 4. Check your current directory
Make sure you're inside the folder where the earningreport.py file is located. You can check with:

```bash
ls  # Linux/macOS
dir # Windows
```
#### 5. Run the script
Run the script according to your operating system:

✅ For Linux/macOS:

```bash
python3 earningreport.py
```

✅ For Windows:

```bash
python earningreport.py
```

---

## Generated Output
- new spreadsheet: resumo_proventos.xlsx (3 sheets)
- Console logs

_The graphs generated below were extracted from the test values._

![pie-chart](https://github.com/fcardan/b3-earnings-spreadsheet/blob/main/docs/assets/earningreport-dt.jpg)
![ev-chart](https://github.com/fcardan/b3-earnings-spreadsheet/blob/main/docs/assets/earningreport-link.jpg)

---

## Workflow

![project-workflow](https://github.com/fcardan/b3-earnings-spreadsheet/blob/main/docs/assets/earningreport-workflow.png)

### Step 1️⃣: Downloading Data

- **Access B3 Investor Portal**
  
   Visit https://www.investidor.b3.com.br/login and authenticate with your credentials

- **Navigate to dividend records**
  
   Go to https://www.investidor.b3.com.br/proventos/recebidos

- **Configure time filter**
  
   Select the full previous calendar year (January through December)

- **Apply event filters**
  
   - Dividend payments
   - Interest on equity (Juros sobre Capital Próprio)
   - Earnings distributions (Rendimentos)

- **Filter asset types**
  
   - Stocks (Ações)
   - Real Estate Funds (Fundos Imobiliários)

- **Export data**
  
   Download the Excel file (e.g. dividend_history.xlsx) containing your complete income records

### Step 2️⃣: Processing Data

- Clone this repository
- Read Excel: the script loads your raw file into a Pandas DataFrame.
- Process Data: it cleans, aggregates and calculates key metrics.
- Generate Statistics: computes totals, ratios and trends for each asset.

### Step 3️⃣: Generating Report
**Export new Excel**

After processing, the script writes a new workbook new_spreadsheet.xlsx containing:

- Summary sheet with aggregated proventos per ticker and period

- Charts illustrating monthly and top‑5 distributions

- Open new_spreadsheet.xlsx in Excel or any spreadsheet tool to review your updated portfolio income report.

---

## Thanks for checking it out ❤️
### Did you like the project?

- ➡️ **Follow**: [@fcardan](https://github.com/fcardan)

- *️⃣ **Star**: Give it a star to support future updates!  

- 🔀 **Fork**: Fork it to customize for your needs!

---

## License
This repository is licensed. This means you are free to share and adapt this content for any purpose, even commercially, as long as you provide appropriate credit to the original author. For more details, please refer to the [LICENSE.md](https://github.com/fcardan/b3-earnings-spreadsheet/blob/main/LICENSE.md) file.
