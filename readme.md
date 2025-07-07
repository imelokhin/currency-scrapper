# Currency Scraper 🏦📊

This Python project scrapes live exchange rates from [x-rates.com](https://www.x-rates.com/table/?from=USD&amount=1) and saves them to an Excel file.

## 📌 Features
- Retrieves currency rates (USD base)
- Saves to Excel with timestamp
- Simple and clear structure

## 📁 Output
- File: `exchange_rates.xlsx`
- Example preview:

| Currency        | Rate        |
|-----------------|-------------|
| Euro            | 0.92        |
| Japanese Yen    | 145.90      |
| Canadian Dollar | 1.36        |

## 🔧 Technologies
- Python 3.x
- `requests`
- `beautifulsoup4`
- `openpyxl`

## 🚀 How to Run
1. Install dependencies:
    ```bash
    pip install requests beautifulsoup4 openpyxl
    ```

2. Run the script:
    ```bash
    python main.py
    ```

3. Check the output Excel file.

---

Created by **Yurii Melekhin** ✨