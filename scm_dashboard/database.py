# database.py
import pandas as pd
from sqlalchemy import create_engine

# Define the database connection parameters
server = 'DESKTOP-BUGKGO7'
database = 'SCM'
driver = 'ODBC Driver 17 for SQL Server'
username = 'Thomas'
password = 'Nairobi12345'

# Create SQLAlchemy engine
connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver.replace(" ", "+")}'
engine = create_engine(connection_string)


# Helper functions to simulate fetching data from the database
def fetch_orders_data():
    # Replace this with your actual SQL query and connection
    query = "SELECT * FROM Orders"
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
    return result.to_dict('records')


def fetch_products_data():
    # Replace this with your actual SQL query and connection
    query = "SELECT * FROM Products"
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
    return result.to_dict('records')


def fetch_cleaned_sales_data():
    # Replace this with your actual SQL query and connection
    query = "SELECT * FROM Suppliers"
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
    return result.to_dict('records')# Callback to update the ontime deilveries

def get_total_sales():
    query = "SELECT SUM(Sales) AS total_sales FROM Products"
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
        return result['total_sales'][0] #returns the total sales value


def get_total_quantity_ordered():
    query = "SELECT SUM(OrderQuantity) AS total_quantity_ordered From Orders"
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
        return result['total_quantity_ordered'][0]

def get_inventory():
    query = "SELECT SUM(StockLevel) AS inventory FROM [SCM].[dbo].[Products]"
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
        return result['inventory'][0]
    
def get_average_shipping_days():
    query = "select AVG(ShippingDays) as average_shipping_days from Orders "
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
        return result['average_shipping_days'][0]

def get_shipped_products():
    query = "SELECT COUNT(OrderStatus) as shipped_products FROM Orders WHERE OrderStatus = 'Shipped'"
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
        return result['shipped_products'][0]


def get_OnTime_deliveries():
    query = "Select COUNT(*) AS onTime_deliveries from Orders where DeliveryStatus = 'On Time';"
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
        return result['onTime_deliveries'][0]
 
 
#visuals
# sample heatmap
# fetch order frequency data
def fetch_order_frequency():
    query = """
    SELECT o.CustomerID, SUM(o.OrderQuantity * p.CarPrice) AS OrderValue
    FROM orders o
    LEFT JOIN products p ON o.ProductID = p.ProductID
    GROUP BY o.CustomerID;
    """
    df = pd.read_sql(query, engine)
    # create columns for Day and month
    df['OrderDay'] = pd.to_datetime(df['OrderDate']).dt.day_name()
    df['OrderMonth']= pd.to_datetime(df['OrderDate']).dt.strftime('%B')
    return df
# Fetch Customer Segmentation Data
def fetch_customer_segmentation():
    query = """
    SELECT o.CustomerID, SUM(o.OrderQuantity * p.CarPrice) AS OrderValue
    FROM orders o
    LEFT JOIN products p ON o.ProductID = p.ProductID
    GROUP BY o.CustomerID;
    """
    return pd.read_sql(query, engine)
