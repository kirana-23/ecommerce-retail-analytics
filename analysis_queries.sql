-- E-Commerce Sales Analytics
-- SQL Queries for MySQL
-- Author: Kirana B

USE ecommerce_db;

-- Query 1: Total Revenue by Month
SELECT Year, Month, MonthName,
       ROUND(SUM(TotalPrice), 2) AS Revenue,
       COUNT(DISTINCT InvoiceNo) AS TotalOrders
FROM orders
GROUP BY Year, Month, MonthName
ORDER BY Year, Month;

-- Query 2: Top 10 Best Selling Products
SELECT ProductName,
       SUM(Quantity) AS TotalUnitsSold,
       ROUND(SUM(TotalPrice), 2) AS TotalRevenue
FROM orders
GROUP BY ProductName
ORDER BY TotalUnitsSold DESC
LIMIT 10;

-- Query 3: Revenue by Country
SELECT Country,
       COUNT(DISTINCT CustomerID) AS TotalCustomers,
       ROUND(SUM(TotalPrice), 2) AS Revenue
FROM orders
GROUP BY Country
ORDER BY Revenue DESC
LIMIT 10;

-- Query 4: RFM Customer Segmentation
SELECT CustomerID,
       COUNT(DISTINCT InvoiceNo) AS Frequency,
       ROUND(SUM(TotalPrice), 2) AS Monetary,
       MAX(InvoiceDate) AS LastPurchaseDate
FROM orders
GROUP BY CustomerID
ORDER BY Monetary DESC
LIMIT 20;

-- Query 5: Best Day of Week
SELECT DayOfWeek,
       COUNT(DISTINCT InvoiceNo) AS TotalOrders,
       ROUND(SUM(TotalPrice), 2) AS Revenue
FROM orders
GROUP BY DayOfWeek
ORDER BY Revenue DESC;

-- Query 6: Average Order Value by Month
SELECT Year, Month,
       ROUND(SUM(TotalPrice) /
       COUNT(DISTINCT InvoiceNo), 2) AS AvgOrderValue
FROM orders
GROUP BY Year, Month
ORDER BY Year, Month;

-- Query 7: Customer Segments
CREATE TABLE customer_segments AS
SELECT CustomerID,
       COUNT(DISTINCT InvoiceNo) AS Frequency,
       ROUND(SUM(TotalPrice), 2) AS TotalSpent,
CASE
    WHEN SUM(TotalPrice) > 5000 THEN 'High Value'
    WHEN SUM(TotalPrice) > 1000 THEN 'Medium Value'
    ELSE 'Low Value'
END AS CustomerSegment
FROM orders
GROUP BY CustomerID;