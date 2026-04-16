# STEP 1A
import sqlite3
import pandas as pd

# STEP 1B
conn = sqlite3.connect("data.sqlite")


# STEP 2
df_first_five = pd.read_sql_query("""
SELECT employeeNumber, lastName
FROM employees;
""", conn)


# STEP 3
df_five_reverse = pd.read_sql_query("""
SELECT lastName, employeeNumber
FROM employees;
""", conn)


# STEP 4
df_alias = pd.read_sql_query("""
SELECT employeeNumber AS ID,
       lastName
FROM employees;
""", conn)


# STEP 5
df_executive = pd.read_sql_query("""
SELECT lastName,
       CASE
           WHEN jobTitle LIKE '%Manager%' OR jobTitle LIKE '%Director%' THEN 'Executive'
           ELSE 'Not Executive'
       END AS role
FROM employees;
""", conn)


# STEP 6
df_name_length = pd.read_sql_query("""
SELECT lastName,
       LENGTH(lastName) AS name_length
FROM employees;
""", conn)


# STEP 7
df_short_title = pd.read_sql_query("""
SELECT jobTitle,
       SUBSTR(jobTitle, 1, 2) AS short_title
FROM employees;
""", conn)


# STEP 8
sum_total_price = pd.read_sql_query("""
SELECT SUM(quantityOrdered * priceEach)
FROM orderdetails;
""", conn).iloc[0, 0]


# STEP 9
df_day_month_year = pd.read_sql_query("""
SELECT orderDate,
       STRFTIME('%d', orderDate) AS day,
       STRFTIME('%m', orderDate) AS month,
       STRFTIME('%Y', orderDate) AS year
FROM orders;
""", conn)