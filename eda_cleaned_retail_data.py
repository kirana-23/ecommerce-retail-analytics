import pandas as pd
df=pd.read_csv(r"C:\Users\B KIRANA\Desktop\Cleaned_data_retail")
print(df.head(10))
#Calculating total revenue
print("Total Revenue is",round(df["TotalPrice"].sum(),2))
#Calculating revenue by month
Rev_month=df.groupby("MonthName")["TotalPrice"].sum().sort_values(ascending=False)
print(Rev_month)
#finding top 10 products
top_products=df.groupby("ProductName")["Quantity"].sum().sort_values(ascending=False).head(10)
print(top_products)
#top 5 countries by revenue
top_country=df.groupby("Country")["TotalPrice"].sum().sort_values(ascending=False).head(5)
print(top_country)
#Most purchased 3 customers
Fav_customer=df["CustomerID"].value_counts().sort_values(ascending=False).head(3)
print(Fav_customer)
#unique customer id
unique_id=df["CustomerID"].nunique()
print(unique_id)
print(df.duplicated(["InvoiceNo"],keep="first"))