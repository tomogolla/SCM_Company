# callbacks.py
from dash import Input, Output
import pandas as pd
from database import engine, fetch_orders_data, fetch_products_data  # Import database functions
from app import app
from data_processing import (get_total_sales, 
                            get_avg_shipping_days,
                            get_total_inventory,
                            get_total_shipped_products,
                            )

# Callback to update the Total Sales
# @app.callback(
#     Output("total-sales-display", "children"),
#     [Input("interval-component", "n_intervals")]
# )
# def update_total_sales(n_intervals):
#     print("Callback triggerred for total sales")
#     total_sales = get_total_sales()
#     print(f"Total sales fetched: {total_sales}")
#     if total_sales >= 1_000_000:
#         formatted_sales = f"${total_sales / 1_000_000:.2f}M"  # Format as millions
#     else:
#         formatted_sales = f"${total_sales:,.2f}"  # Format as regular currency   
#     return formatted_sales

def register_callbacks(app):
    @app.callback(
        Output('total-sales', 'children'),
        Input('total-sales', 'id')
    )
    def update_total_sales(_):
        print("Callback triggerred for total sales")
        total_sales = get_total_sales()
        print(f"Total sales fetched: {total_sales}")
        if total_sales >= 1_000_000:
            formatted_sales = f"${total_sales / 1_000_000:.2f}M"  # Format as millions
        else:
            formatted_sales = f"${total_sales:,.2f}"  # Format as regular currency   
        return formatted_sales


 # Define additional callbacks as needed
# Update Total Inventory Card
@app.callback(
    Output("total-inventory-display", "children"),
    [Input("interval-component", "n_intervals")]
)
def update_total_inventory(n_intervals):
    total_inventory = get_total_inventory()
    return f"{total_inventory:,} Units" if total_inventory else "0 Units"

# Update Average Shipping Days Card
@app.callback(
    Output("average-shipping-display", "children"),
    [Input("interval-component", "n_intervals")]
)
def update_avg_shipping_days(n_intervals):
    avg_shipping_days = get_avg_shipping_days()
    return f"{avg_shipping_days} Days" if avg_shipping_days else "0 Days"

# Update Total Shipped Products Card
@app.callback(
    Output("total-shipped-display", "children"),
    [Input("interval-component", "n_intervals")]
)
def update_total_shipped_products(n_intervals):
    total_shipped = get_total_shipped_products()
    return f"{total_shipped} Products" if total_shipped else "0 Products"

# # Callback to update the ongoing sales value
# @app.callback(
#     Output("ongoing-sales-display", "children"),
#     [Input("interval-component", "n_intervals")]
# )
# def update_ongoing_sales(n_intervals):
#     return f"{get_ongoing_sales()} Orders"

import plotly.express as px
import pandas as pd


def register_callbacks(app):
    @app.callback(
        Output('sales-bar-chart', 'figure'),
        Input('sales-bar-chart', 'id')
    )
    def update_bar_chart(_):
        connection = engine.connect()
        query = "SELECT [CarModel], SUM([Sales]) AS total_sales FROM [dbo].[Products] GROUP BY [CarModel] ORDER BY total_sales DESC;"
        df = pd.read_sql(query, connection)
        
        fig = px.bar(df, x='CarModel', y='total_sales', title='Total Sales by Car Model')
        return fig
import plotly.express as px

# Function to register the callbacks
def register_callbacks(app):
    @app.callback(
        Output('category-quantity-chart', 'figure'),  # Update the figure of the chart
        [Input('category-quantity-chart', 'id')]
    )
    def update_category_quantity_chart(_):
        connection = engine.connect()
        query = """
        SELECT [CarCategory], 
               SUM([OrderQuantity]) AS category_quantity 
        FROM Products 
        GROUP BY [CarCategory] 
        ORDER BY category_quantity DESC;
        """
        df = pd.read_sql(query, connection)
        
        # Create the bar chart using Plotly Express
        category_quantity_fig = px.bar(df, x='CarCategory', y='category_quantity',
                                       title='Inventory by Car Category',
                                       labels={'CarCategory': 'Car Category', 'category_quantity': 'Category Quantity (cars)'},
                                       template='plotly_white')
        return category_quantity_fig

register_callbacks(app)