# Exploratory data Analysis - E-Commerce Data Analysis

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.colors as color
pio. templates.default = "plotly_white"

# read the csv file
df = pd.read_csv(r"C:\Users\rajve\Downloads\ecommerce_product_dataset.csv")
print(df.columns)
print(df.head())

# Statistics of the product dataset
print(df.describe())

# information of data
print(df.info())

# Converting into date column
df['DateAdded'] = pd.to_datetime(df['DateAdded'])

#  Sales Analysis - We can also replace our acutual data
"""data = {
    'ProductID': [101, 102, 103, 104, 105],
    'ProductName': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
    'Category': ['Electronics', 'Clothing', 'Grocery', 'Electronics', 'Clothing'],
    'Price': [200, 50, 10, 300, 80],
    'Rating': [4.5, 3.8, 4.2, 4.8, 3.5],
    'NumReviews': [150, 80, 120, 200, 50],
    'StockQuantity': [20, 50, 100, 10, 60],
    'Discount': [10, 20, 5, 15, 25],
    'Sales': [1000, 500, 1500, 2000, 300],
    'DateAdded': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-01-15', '2024-02-10']
}

df = pd.DataFrame(data)
df['DateAdded'] = pd.to_datetime(df['DateAdded'])"""

# 1. Sales Analysis
fig_sales = px.bar(df, x='ProductName', y='Sales', color='Category',title="Sales Analysis by Product Name and Category")
fig_sales.show()

# 2. Ratings Distribution
fig_ratings = px.histogram(df, x='Rating', nbins=5, title="Distribution of Ratings")
fig_ratings.show()

# 3. Number of Reviews
fig_reviews = px.bar(df, x='ProductName', y='NumReviews', color='NumReviews',title="Number of Reviews per Product")
fig_reviews.show()

# 4. Discounts per Product
fig_discount = px.scatter(df, x='ProductName', y='Discount', size='Discount',color='Discount', title="Discounts Offered by Product")
fig_discount.show()

# 5. ProductID and Date Added (Timeline)
fig_date = px.scatter(df, x='DateAdded', y='ProductID', text='ProductName',title="Product Timeline (ProductID and Date Added)",
labels={'DateAdded': 'Date Added', 'ProductID': 'Product ID'})
fig_date.update_traces(textposition='top center')
fig_date.show()

# 6. Product Name vs Discount
fig_product_discount = px.bar(df, x='ProductName', y='Discount', color='Discount',title="Product Name and Discount")
fig_product_discount.show()

