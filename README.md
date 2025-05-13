![.](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyjrF64yMg2p0HUJFMxWJYRgvSwQweHVajqg&s)

# Earnings Spreadsheet Analyzer (B3 to tax)

[![🔥 Follow my GitHub](https://img.shields.io/badge/👉🏼-GitHub-white)](https://www.github.com/fcardan)
[![🔥 Follow my Linkedin](https://img.shields.io/badge/👉🏼-Linkedin-blue)](https://www.linkedin.com/in/fcardan)
[![⭐ pt-br](https://img.shields.io/badge/👉🏼-PtBr-green)](https://github.com/fcardan/b3-earnings-spreadsheet/main/blob/README-ptbr.md)
[![⭐ Star](https://img.shields.io/github/stars/fcardan/b3-earnings-spreadsheet)](https://github.com/fcardan/b3-earnings-spreadsheet)


A Python tool to analyze and visualize investment income data from B3 (Brazilian stock exchange), including dividends, interest, and real estate fund (FII) distributions.

## 🔹Table of Contents
- [Overview](#🔹overview)
- [Problem Solved](#🔹problem-solved)
- [Features](#🔹features)
- [Tech Stack](#🔹tech-stack)
- [Installation](#🔹installation)
- [Configuration](#🔹configuration)
- [Usage](#🔹usage)
- [License](#🔹license)

## 🔹Overview
Automates investment income analysis by generating:
- Consolidated reports by asset and event type
- Monthly evolution charts
- Tax declaration guidelines
- Top payer identification

## 🔹Problem Solved
Simplifies manual processes of:
1. Aggregating income from multiple sources
2. Calculating totals by asset and period
3. Generating analysis visualizations
4. Preparing fiscal declaration data

## 🔹Features
✅ Consolidated Overview  
✅ Monthly Summary with Charts  
✅ Top Payers by Category  
✅ Tax Declaration Guide  
✅ Automatic Value Formatting  
✅ Excel Compatibility (.xlsx)

## 🔹Tech Stack
- **Python 3.10+**: Core logic
- **Pandas**: Data processing
- **Matplotlib**: Chart generation
- **Openpyxl**: Excel integration

## 🔹Installation
```bash
# Clone repository
git clone https://github.com/your-user/proventos-report.git

# Install dependencies
pip install pandas openpyxl matplotlib

# OR Install
pip install -r requirements.txt

```

## 🔹Configuration
- Place your spreadsheet in project folder
- Rename to proventosb3.xlsx
- Expected spreadsheet structure:
  - Columns: Product, Payment, Event Type, Net Value

## 🔹Usage
```bash
# Run script (Windows)
python proventosreport.py
```

## 🔹Generated Output
- resumo_proventos.xlsx (3 sheets)
- Console logs

## 🔹License
This repository is licensed. This means you are free to share and adapt this content for any purpose, even commercially, as long as you provide appropriate credit to the original author. For more details, please refer to the [LICENSE.md](https://github.com/fcardan/b3-earnings-spreadsheet/blob/main/LICENSE.md) file.
