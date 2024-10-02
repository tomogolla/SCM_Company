# layout.py
from dash import html, dcc
import dash_bootstrap_components as dbc

from dash_components import create_metric_card, create_insights_card # Import custom UI components if needed
from dashboards import create_sales_visual, create_order_category_visual, create_visual_card

external_stylesheets = [dbc.themes.BOOTSTRAP]

# Define the main layout of the application
app_layout = html.Div([

    # Interval for updating data every 30 seconds
    dcc.Interval(
        id="interval-component",
        interval=30 * 1000,  # in milliseconds (30 seconds)
        n_intervals=0  # initial number of intervals
    ),

    # Header
    html.Div(
        className="header",
        children=[
            html.Header("Tom Ogolla", className="top-head"),
        ],
        style={
            'background-color': '#777',
            'fontSize': '20px',
            'fontFamily': 'Arial, sans-serif',
            'color': 'white',
            'padding-left': '20px'
        }
    ),

    # Main Navigation Bar
    dbc.Navbar(
        dbc.Container(
            [
                dbc.NavbarBrand(
                    "SCM Company Ltd.",
                    style={
                        "fontWeight": "bold",
                        "fontSize": "20px",
                        "textDecoration": "underline",
                        "color": "black"
                    }
                ),
                dbc.Nav(
                    [
                        dbc.DropdownMenu(
                            label="Dashboard",
                            nav=True,
                            children=[
                                dbc.DropdownMenuItem("Sales Overview", href="/sales_overview"),
                                dbc.DropdownMenuItem("Financial Summary", href="/financial_summary"),
                                dbc.DropdownMenuItem("Performance Metrics", href="/performance_metrics"),
                            ],
                        ),
                        dbc.DropdownMenu(
                            label="Reports",
                            nav=True,
                            children=[
                                dbc.DropdownMenuItem("Monthly Report", href="/monthly_report"),
                                dbc.DropdownMenuItem("Quarterly Report", href="/quarterly_report"),
                                dbc.DropdownMenuItem("Yearly Analysis", href="/yearly_analysis"),
                            ],
                        ),
                        dbc.DropdownMenu(
                            label="Insights",
                            nav=True,
                            children=[
                                dbc.DropdownMenuItem("Customer Insights", href="/customer_insights"),
                                dbc.DropdownMenuItem("Sales Trends", href="/sales_trends"),
                                dbc.DropdownMenuItem("Market Analysis", href="/market_analysis"),
                            ],
                        ),
                        dbc.DropdownMenu(
                            label="Charts",
                            nav=True,
                            children=[
                                dbc.DropdownMenuItem("Revenue Chart", href="/revenue_chart"),
                                dbc.DropdownMenuItem("Expenses Chart", href="/expenses_chart"),
                                dbc.DropdownMenuItem("Profit Margin", href="/profit_margin"),
                            ],
                        ),
                    ],
                    className="ml-auto",
                    navbar=True,
                ),
            ],
            fluid=True,
        ),
        color="light",
        style={
            'padding-top': '10px',
            'padding-bottom': '10px',
            'padding-right': '100px',
            'height': '50px',
            'color': 'black',
            'padding-left': '30px'
        }
    ),

    # Sub Navigation Menu
    dbc.Navbar(
        dbc.Container(
            [
                dbc.Nav(
                    [
                        dbc.DropdownMenu(
                            label="Customers",
                            nav=True,
                            children=[
                                dbc.DropdownMenuItem("Open in View Mode", href="/customers/view"),
                                dbc.DropdownMenuItem("Open in Edit Mode", href="/customers/edit"),
                            ],
                        ),
                        dbc.DropdownMenu(
                            label="Products",
                            nav=True,
                            children=[
                                dbc.DropdownMenuItem("Open in View Mode", href="/products/view"),
                                dbc.DropdownMenuItem("Open in Edit Mode", href="/products/edit"),
                            ],
                        ),
                        dbc.DropdownMenu(
                            label="Orders",
                            nav=True,
                            children=[
                                dbc.DropdownMenuItem("Open in View Mode", href="/orders/view"),
                                dbc.DropdownMenuItem("Open in Edit Mode", href="/orders/edit"),
                            ],
                        ),
                        dbc.DropdownMenu(
                            label="Suppliers",
                            nav=True,
                            children=[
                                dbc.DropdownMenuItem("Open in View Mode", href="/suppliers/view"),
                                dbc.DropdownMenuItem("Open in Edit Mode", href="/suppliers/edit"),
                            ],
                        ),
                        dbc.DropdownMenu(
                            label="Payments",
                            nav=True,
                            children=[
                                dbc.DropdownMenuItem("Open in View Mode", href="/payments/view"),
                                dbc.DropdownMenuItem("Open in Edit Mode", href="/payments/edit"),
                            ],
                        ),
                    ],
                    className="ml-auto",
                    navbar=True,
                ),
            ],
            fluid=True,
        ),
        color="light",
        style={
            'padding-top': '10px',
            'padding-bottom': '10px',
            'padding-right': '100px',
            'height': '50px',
            'padding-left': '30px'
        }
    ),

    # Content Area
    html.Div(
        className="content",
        children=[
            html.H2("Dashboard Content Area"),
            html.P("This area will contain content like charts and visuals.")
        ],
        style={
            'padding': '20px',
            'fontSize': '12px',
            'padding-left': '30px',
            'fontFamily': 'Arial, sans-serif'
        }
    ),

    # Metric Cards
    html.Div(
        children=[
            html.H2("Insights", style={"fontSize": "24px", "fontWeight": "bold", "textAlign": "left", "padding": "10px 0"}),
            html.Hr(style={"borderColor": "#6c757d"}),
            dbc.Row(
                [
                    create_metric_card("Total Sales", "total-sales", "$16.00M"),
                    create_metric_card("Total Quantity Ordered", "total-quantity-display", "345 Items"),
                    create_metric_card("Total Inventory", "total-inventory-display", "567 Units"),
                    create_metric_card("Avg. Shipping Days", "average-shipping-display", "115 Days"),
                    create_metric_card("Shipped Products", "total-shipped-display", "23 Products"),
                ],
                style={
                    "display": "flex",
                    "justifyContent": "left",
                    "marginTop": "30px",
                    "margin": "10px"
                }
            ),
            
        ],
        style={
            "backgroundColor": "#fff",  # Light background for the layout
            "padding": "40px"
        }
    ),

    # Insights Section
    html.Div(
        children=[
            html.H2("Activities", style={"fontSize": "24px", "fontWeight": "bold", "textAlign": "left", "padding": "10px 0"}),
            html.Hr(style={"borderColor": "#6c757d"}),  # Line separator
            dbc.Row(
                [
                    create_insights_card("ONGOING SALES", "10", "ongoing-sales-display"),
                    create_insights_card("PENDING ORDERS", "5", "pending-orders-display"),
                    create_insights_card("CANCELLED ORDERS", "2", "canceled-orders-display"),                
                    create_insights_card("ONGOING PURCHASES", "3", "ongoing-purchases-display"),
                    create_insights_card("PENDING PAYMENTS", "4", "pending-payments-display"),
                    create_insights_card("COMPLETED PAYMENTS", "15", "completed-payments-display"),
                ],
                style={"margin-bottom": "20px"}
            ),
            dbc.Row(
                [
                    create_insights_card("ADD ACITIVITY", "+", "ongoing-stuff-display"),
                    create_insights_card("ADD ACTIVITY", "+", "pending-stuff1-display"),
                    create_insights_card("ADD ACTIVITY", "+", "completed-stuff2-display"),
                ],
                style={"margin-bottom": "20px"}
            ),
        ],
        style={"padding-left": "40px"}
    ),

    # Main Content Area (allows scrolling)
    html.Div(        
        children=[
            html.H2("Sales Overview", style={"fontSize": "24px", "fontWeight": "bold", "textAlign": "left", "padding": "10px 0"}),
            create_sales_visual()  # This will call the visual created in dashboards.py
        ],
        style={"padding-left": "40px", "padding-top": "20px", "fontSize": "16px"}   
        
    ),
    
    html.Div(
        children=[
            html.H2("Category Quantity Overview", style={"fontSize": "24px", "fontWeight": "bold", "textAlign": "left", "padding": "10px 0"}),
            create_order_category_visual()
        ],
        style={"padding-left": "40px", "padding-top": "30px"}
        
    ),
    html.Div(
        children=[
            html.H2("Inventory Overview", style={"fontSize": "24px", "fontWeight": "bold", "textAlign": "left", "padding": "10px 0"}),
            html.Hr(style={"borderColor": "#6c757d"}),  # Line separator
            dbc.Row(
                [
                    create_visual_card("Inventory", "create_category_fig")
                ]   
            )
                
        ]
    )
           
])
