import pandas as pd
df=pd.read_csv(r"C:\Users\B KIRANA\Downloads\archive (3)\online_retail_II.csv") #path to csv
print(df.head(10).to_string()) #checking whether data is loaded
print(df.columns.tolist()) #to know about the columns
print(df.info()) #to know about the count and dtype
df=df.dropna(subset=["Customer ID","Description"]) #dropping the na customer id and also description since it cannot be replaced with any other using fillna()
print(df.shape)
df=df[~df["Invoice"].astype(str).str.startswith("C")] #removing the canceled orders
print(df.shape)
df=df[df["Quantity"] > 0] #rempving negative and 0
df=df[df["Price"] > 0]
print(df.shape)
df["TotalPrice"]=df["Price"]*df["Quantity"] #creating total price column
df["InvoiceDate"]=pd.to_datetime(df["InvoiceDate"])
df["Year"]=df["InvoiceDate"].dt.year
df["Month"]=df["InvoiceDate"].dt.month
df["MonthName"]=df["InvoiceDate"].dt.strftime("%B")
df["DayOfWeek"]=df["InvoiceDate"].dt.day_name()
print(df.columns)
df=df.rename(columns={"Invoice":"InvoiceNo","StockCode":"ProductCode","Description":"ProductName","Customer ID":"CustomerID"})
print(df.columns)
print(df.info())
df.to_csv("Cleaned_data_retail",index=False) #exporting the cleaned data as csv