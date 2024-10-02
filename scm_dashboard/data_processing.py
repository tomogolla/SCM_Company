# data_processing.py
import pandas as pd

from database import engine
from database import fetch_orders_data, fetch_products_data
                
                    
connection = engine.connect

def prepare_order_data():
    df = fetch_orders_data()
    df['OrderDay'] = pd.to_datetime(df['OrderDate']).dt.day_name()
    df['OrderMonth'] = pd.to_datetime(df['OrderDate']).dt.strftime('%B')
    return df

# Add more data processing or transformation functions as needed
def calculate_total_sales():
    orders_df = fetch_orders_data()
    products_df = fetch_products_data()
    merged_df = pd.merge(orders_df, products_df[['ProductID', 'CarPrice']], on='ProductID')
    total_sales = (merged_df['OrderQuantity'] * merged_df['CarPrice']).sum()
    return total_sales

# Prepare data for order frequency heatmap visualization
def prepare_order_frequency_data():
    orders_df = fetch_orders_data()
    # Ensure 'OrderDate' is in datetime format and extract day/month for analysis
    orders_df['OrderDate'] = pd.to_datetime(orders_df['OrderDate'])
    orders_df['OrderDay'] = orders_df['OrderDate'].dt.day_name()
    orders_df['OrderMonth'] = orders_df['OrderDate'].dt.strftime('%B')
    return orders_df

def get_total_sales():
    query = "SELECT SUM(sales) as total_sales FROM orders;"
    result = pd.read_sql(query, connection)
    return result['total_sales'][0]

def get_total_quantity():
    query = "SELECT SUM(quantityordered) as total_quantity FROM orders;"
    result = pd.read_sql(query, connection)
    return result['total_quantity'][0]

def get_total_inventory():
    query = "SELECT SUM(OrderQuantity) as total_inventory FROM products;"
    result = pd.read_sql(query, connection)
    return result['total_inventory'][0]

def get_avg_shipping_days():
    query = "SELECT AVG(DATEDIFF(day, OrderDate, ShipDate)) as avg_shipping_days FROM orders;"
    result = pd.read_sql(query, connection)
    return round(result['avg_shipping_days'][0], 2)

def get_total_shipped_products():
    query = "SELECT COUNT(*) as total_shipped FROM orders WHERE status='Shipped';"
    result = pd.read_sql(query, connection)
    return result['total_shipped'][0]

def fetch_car_sales_data():
    query = """
    SELECT [CarModel], 
           SUM([Sales]) AS total_sales 
    FROM [dbo].[Products] 
    GROUP BY [CarModel] 
    ORDER BY total_sales DESC;
    """
    df = pd.read_sql(query, connection)
    return df