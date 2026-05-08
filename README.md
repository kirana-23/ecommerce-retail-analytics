# RetailPulse: Customer Intelligence & RFM Analytics

> End-to-end retail analytics project using Python, MySQL, and Power BI on 500K+ transactions from the UCI Online Retail II dataset.

---

## Project Overview

This project performs full-cycle data analytics on a real-world e-commerce dataset — from raw data ingestion and cleaning through SQL-based analysis, RFM customer segmentation, and an interactive Power BI dashboard. The goal is to uncover actionable business insights around customer behavior, revenue trends, and product performance.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python (Pandas) | Data cleaning, EDA, feature engineering |
| MySQL | Data storage, querying, aggregation |
| Power BI | Interactive dashboard and visualization |
| SQL | Business analytics queries |

---

## Dataset

- **Source:** [UCI Online Retail II Dataset](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II)
- **Size:** 500K+ transactions
- **Period:** 2009–2011
- **Fields:** Invoice, StockCode, Description, Quantity, InvoiceDate, Price, Customer ID, Country

---

## Project Structure

```
RetailPulse/
│
├── data_cleaning.py              # Raw data cleaning & feature engineering
├── eda_cleaned_retail_data.py    # Exploratory data analysis
├── import_data_mysql.py          # MySQL connection & data import
├── analysis_queries.sql          # Business analytics SQL queries
├── retail_project.pbix           # Power BI dashboard file
└── README.md
```

---

## Workflow

### 1. Data Cleaning (`data_cleaning.py`)
- Loaded raw CSV from UCI Online Retail II dataset
- Dropped rows with missing `Customer ID` and `Description`
- Removed cancelled orders (Invoice starting with `C`)
- Filtered out negative and zero `Quantity` and `Price` values
- Engineered new columns: `TotalPrice`, `Year`, `Month`, `MonthName`, `DayOfWeek`
- Renamed columns for consistency and exported cleaned CSV

### 2. Exploratory Data Analysis (`eda_cleaned_retail_data.py`)
- Calculated total revenue across the dataset
- Grouped revenue by month to identify seasonal trends
- Found top 10 best-selling products by quantity
- Identified top 5 countries by revenue
- Analysed most frequent customers by purchase count
- Counted unique customers in the dataset

### 3. MySQL Integration (`import_data_mysql.py`)
- Connected to local MySQL instance (`ecommerce_db`)
- Verified database connection and server details
- Cleaned data imported into `orders` table for SQL querying

### 4. SQL Analytics (`analysis_queries.sql`)
Seven analytical queries covering:
- **Revenue by Month** — monthly and yearly revenue with order counts
- **Top 10 Products** — best sellers by units sold and revenue
- **Revenue by Country** — top 10 countries with customer counts
- **RFM Segmentation** — Recency, Frequency, Monetary per customer
- **Best Day of Week** — order volume and revenue by weekday
- **Average Order Value** — AOV trend by month
- **Customer Segments** — High Value / Medium Value / Low Value classification

### 5. Power BI Dashboard (`retail_project.pbix`)
Interactive dashboard visualising:
- Customer segments and RFM distribution
- Revenue contribution by segment
- Monthly sales trends
- Top-performing customers and products

---

## Key Insights

- Identified high-value customer segments (Champions, Loyal, At-Risk) using RFM analysis
- Uncovered peak revenue months and best-performing weekdays
- Top 10 products account for a significant share of total units sold
- UK dominates revenue; several international markets show growth potential

---

## How to Run

### Prerequisites
```
pip install pandas mysql-connector-python
```

### Steps

1. **Clone the repo**
   ```bash
   git clone https://github.com/kirana-23/RetailPulse.git
   cd RetailPulse
   ```

2. **Download the dataset**
   - Download from [UCI Online Retail II](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II)
   - Update the file path in `data_cleaning.py`

3. **Run data cleaning**
   ```bash
   python data_cleaning.py
   ```

4. **Run EDA**
   ```bash
   python eda_cleaned_retail_data.py
   ```

5. **Set up MySQL**
   - Create a database named `ecommerce_db`
   - Import the cleaned CSV into an `orders` table
   - Update credentials in `import_data_mysql.py`
   - Run `analysis_queries.sql` in MySQL Workbench or CLI

6. **Open Power BI dashboard**
   - Open `retail_project.pbix` in Power BI Desktop
   - Refresh data source if needed

---

## Author

**Kirana B**
- GitHub: [github.com/kirana-23](https://github.com/kirana-23)
- LinkedIn: [linkedin.com/in/kirana-kira23](https://www.linkedin.com/in/kirana-kira23)
- Email: kirana232004@gmail.com
