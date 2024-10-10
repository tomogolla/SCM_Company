import pandas as pd
from sqlalchemy import create_engine, text
from functools import lru_cache

# MSSQL database connection snippet
def get_db_engine():
    server = 'localhost'
    database = 'SCM'
    username = 'Thomas'
    password = 'Nairobi12345'
    connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'
    return create_engine(connection_string)

def cached_query(func):
    @lru_cache(maxsize=None)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@cached_query
def get_total_sales():
    query = """
    SELECT SUM(s.amount) as TotalSales
    FROM Sales s
    """
    with get_db_engine().connect() as conn:
        df = pd.read_sql(text(query), conn)
    return df

@cached_query
def get_total_orders():
    query = """
    SELECT COUNT(*) as TotalOrders
    FROM Opportunities
    """
    with get_db_engine().connect() as conn:
        df = pd.read_sql(text(query), conn)
    return df

@cached_query
def get_total_revenue():
    query = """
    SELECT 
    SUM(Sales) - SUM(CostPrice) AS TotalRevenue
    FROM 
        Products;
    """
    with get_db_engine().connect() as conn:
        df = pd.read_sql(text(query), conn)
    return df

@cached_query
def get_ongoing_orders():
    query = """
    SELECT COUNT(*) as OngoingOrders
    FROM Opportunities
    WHERE Status = 'In progres';
    """
    with get_db_engine().connect() as conn:
        df = pd.read_sql(text(query), conn)
    return df

@cached_query
def get_pending_orders():
    query = """
    SELECT COUNT(*) as PendingOrders
    FROM Opportunities
    WHERE Status = 'Pending';
    """
    with get_db_engine().connect() as conn:
        df = pd.read_sql(text(query), conn)
    return df

@cached_query
def get_completed_orders():
    query = """
    SELECT COUNT(*) as CompletedOrders
    FROM Opportunities
    WHERE Status = 'Completed';
    """
    with get_db_engine().connect() as conn:
        df = pd.read_sql(text(query), conn)
    return df

@cached_query
def get_delayed_deliveries():
    query = """
    SELECT COUNT(*) as DelayedDeliveries
    FROM Opportunities
    WHERE Status = 'Delayed';
    """
    with get_db_engine().connect() as conn:
        df = pd.read_sql(text(query), conn)
    return df



@cached_query
def get_top_companies_by_opportunity_value():
    query = """
    SELECT TOP 5 c.company_name, log(SUM(o.estimated_value)) as TotalEstimatedValue
    FROM Companies c
    JOIN Opportunities o ON c.company_id = o.company_id
    GROUP BY c.company_name
    ORDER BY TotalEstimatedValue DESC
    """
    with get_db_engine().connect() as conn:
        df = pd.read_sql(text(query), conn)
    return df

@cached_query
def get_opportunity_status_distribution():
    query = """
    SELECT c.company_name, o.Status, COUNT(*) as StatusCount
    FROM Companies c
    JOIN Opportunities o ON c.company_id = o.company_id
    GROUP BY c.company_name, o.Status
    ORDER BY c.company_name, o.Status
    """
    with get_db_engine().connect() as conn:
        df = pd.read_sql(text(query), conn)
    return df

@cached_query
def get_company_sales_by_payment_status():
    query = """
    SELECT TOP 5
        c.company_name,
        s.payment_status,
        SUM(s.amount) as TotalSales
    FROM Companies c
    JOIN Opportunities o ON c.company_id = o.company_id
    JOIN Sales s ON o.id = s.opportunity_id
    GROUP BY c.company_name, s.payment_status
    ORDER BY TotalSales DESC
    """
    with get_db_engine().connect() as conn:
        df = pd.read_sql(text(query), conn)
    return df

@cached_query
def get_company_locations_with_opportunity_count():
    query = """
    SELECT c.company_id, c.company_name, c.location, COUNT(o.id) as OpportunityCount
    FROM Companies c
    LEFT JOIN Opportunities o ON c.company_id = o.company_id
    GROUP BY c.company_id, c.company_name, c.location
    """
    with get_db_engine().connect() as conn:
        df = pd.read_sql(text(query), conn)
    return df
@cached_query
def get_customer_distribution_by_country_and_city():
    query = """
    SELECT c.country, c.city, COUNT(c.customerid) as CustomerCount
    FROM Customers c
    GROUP BY c.country, c.city
    """
    with get_db_engine().connect() as conn:
        df = pd.read_sql(text(query), conn)
    return df
@cached_query
def get_customer_distribution_by_gender():
    query = """
   use scm
 SELECT c.gender, COUNT(c.[CustomerID]) as CustomerCount
    FROM Customers c
    GROUP BY c.gender
    """
    with get_db_engine().connect() as conn:
        df = pd.read_sql(text(query), conn)
    return df
@cached_query
def get_customer_job_titles():
    query = """
   USE scm;

WITH JobTitleCounts AS (
    SELECT 
        c.[JobTitle], 
        COUNT(c.customerId) AS CustomerCount
    FROM Customers c
    GROUP BY c.[JobTitle]
)

SELECT 
    CASE 
        WHEN CustomerCount >= 3 THEN [JobTitle]
        ELSE 'Other'
    END AS JobTitle, 
    SUM(CustomerCount) AS CustomerCount
FROM JobTitleCounts
GROUP BY 
    CASE 
        WHEN CustomerCount >= 3 THEN [JobTitle]
        ELSE 'Other'
    END
ORDER BY CustomerCount DESC;

    """
    with get_db_engine().connect() as conn:
        df = pd.read_sql(text(query), conn)
    return df
