# 🛒 E-Commerce Sales Analytics Dashboard

## 📌 Project Overview
End-to-end retail analytics project analyzing 800K+ 
UK retail transactions using Python, MySQL and Power BI
to uncover revenue trends, top products and 
customer segments.

## 🛠️ Tools & Technologies
| Tool | Purpose |
|---|---|
| Python (pandas) | Data cleaning & EDA |
| MySQL | Database & SQL queries |
| Power BI | Interactive dashboard |

## 📂 Project Structure
```
ecommerce-retail-analytics/
├── data_cleaning.py          # Data cleaning script
├── eda_cleaned_retail_data.py # Exploratory analysis
├── import_data_mysql.py      # MySQL import script
├── analysis_queries.sql      # All SQL queries
├── cleaned_data_retail.csv   # Cleaned dataset
└── screenshots/              # Dashboard images
    ├── page1_sales.png
    ├── page2_products.png
    ├── page3_geography.png
    └── page4_rfm.png
```

## 📊 Dashboard Pages
- **Page 1:** Sales Overview — KPIs, Monthly Revenue, Day of Week
- **Page 2:** Product Performance — Top Products, Treemap
- **Page 3:** Customer & Geography — World Map, Country Analysis
- **Page 4:** RFM Analysis — Customer Segmentation

## 🔍 Key Insights
- 📈 November has highest revenue due to pre-Christmas demand
- 🌍 UK contributes 85% of total revenue
- 👥 Top 20% customers drive 65% of total revenue
- 📦 WHITE HANGING HEART T-LIGHT HOLDER is top product
- 📅 Thursday is the best day for sales

## 📸 Dashboard Preview
### Page 1 - Sales Overview
![Sales](screenshots/page1_sales.png)

### Page 2 - Product Performance
![Products](screenshots/page2_products.png)

### Page 3 - Customer & Geography
![Geography](screenshots/page3_geography.png)

### Page 4 - RFM Analysis
![RFM](screenshots/page4_rfm.png)

## 📁 Dataset
- **Source:** UK Online Retail II Dataset
- **From:** UCI Machine Learning Repository via Kaggle
- **Size:** 800K+ transactions
- **Period:** 2009 - 2011

## ⚙️ How to Run
1. Clone this repository
2. Install requirements:
```
   pip install pandas openpyxl sqlalchemy pymysql
```
3. Run data cleaning:
```
   python data_cleaning.py
```
4. Import to MySQL:
```
   python import_data_mysql.py
```
5. Run SQL queries in MySQL Workbench
6. Open Power BI and connect to MySQL

## 👤 Author
**Kirana B**
- Email: kirana232004@gmail.com
