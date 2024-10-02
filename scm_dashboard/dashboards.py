from dash import Dash, html, dcc, Input, Output  
import plotly.express as px

import dash_bootstrap_components as dbc  
import pandas as pd    

from dash_components import create_visual_card

from database import engine

connection = engine.connect


# Connect to the SQL database
connection = engine.connect()



def create_insights_card(title, value, id, drilldown_arrow="↓", bg_color="#3a4b47"):
    
    return dbc.Card(
            dbc.CardBody([
                html.H4(title, className="card-title", style={"fontSize": "16px", "textAlign": "left", "margin-bottom": "5px", "padding": "0"}),
                html.H2(value, id=id, className="insight-value", style={"fontSize": "60px", "textAlign": "left", "color": "white", "padding": "0"}),
                # html.Div(drilldown_arrow, className="drilldown-arrow", style={"fontSize": "20px", "textAlign": "center", "color": "white"}),
                dbc.CardFooter(">")
            ]),
            style={
                "width": "150px", 
                "height": "200px", 
                "backgroundColor": '#83c5be',
                "margin": "5px", 
                "borderRadius": "0px",  # No rounded corners
                "border": "0px solid #2f3c3c"
            }
        )
    
    




# Query to fetch car model and sales data
query = """
SELECT [CarModel], 
       SUM([Sales]) AS total_sales 
FROM [dbo].[Products] 
GROUP BY [CarModel] 
ORDER BY total_sales DESC;
"""
# Load the data into a DataFrame
df = pd.read_sql(query, connection)

# Create a bar chart using Plotly Express
def create_sales_visual():
    sales_fig = px.bar(df, x='CarModel', y='total_sales',
                       labels={'CarModel': 'Car Model', 'total_sales': 'Total Sales ($)'},
                       title='Total Sales by Car Model',
                       template='plotly_white')
    return dcc.Graph(
        id='sales-chart',
        figure=sales_fig,
        style={
            "width": "700px",
            #"margin": "20px auto",  # Centering the chart
            "height": "500px",
            "padding": "40px"
        }
    )

# Query to fetch category quantities
query1 = """
SELECT [CarCategory], SUM([OrderQuantity]) as category_quantity
FROM Products
GROUP BY [CarCategory]
ORDER BY category_quantity DESC;
"""
# Load the data into a DataFrame
df1 = pd.read_sql(query1, connection)

# Create a visual for Category Quantity
def create_order_category_visual():
    category_quantity_fig = px.bar(
        df1, 
        x='CarCategory', 
        y='category_quantity',
        labels={'CarCategory': 'Car Category', 'category_quantity': 'Category Quantity (cars)'},
        title='Inventory by Car Category',
        template='plotly_white'
    )
    
    # Use the new create_visual_card function to wrap the visual
    return create_visual_card("Category Quantity Overview", "category-quantity-chart", category_quantity_fig)