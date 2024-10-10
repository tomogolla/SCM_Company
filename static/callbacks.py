from dash.dependencies import Input, Output
from dash import callback
import plotly.express as px
import pandas as pd
from db import (get_top_companies_by_opportunity_value, get_opportunity_status_distribution, 
                get_company_sales_by_payment_status, get_customer_distribution_by_country_and_city, get_customer_distribution_by_gender, 
                get_customer_job_titles, 
                get_total_sales, get_total_orders,
                get_total_revenue, get_ongoing_orders, get_pending_orders,
                get_completed_orders, get_delayed_deliveries
            )

# Define color scheme
color_scheme = ['#55A0B0', '#7FBAC4', '#A9D4D9', '#D3E9ED', '#808080', '#A9A9A9', '#C0C0C0', '#D3D3D3']

# Define the font style for the layout
font_style = {
    'family': '"Gotham", "Helvetica Neue", "Helvetica", Arial, sans-serif',
    'size': 13
}

# Function to apply font style and legend position to layout
def apply_chart_style(fig, title):
    fig.update_layout(
        font=font_style,
        # title=title,
        margin=dict(l=10, r=10, t=60, b=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5)
    )
    return fig
@callback(
    Output('total-sales-value', 'children'),
    Input('url', 'pathname')
)
def update_total_sales_value(pathname):
    df = get_total_sales()
    total_sales = df.iloc[0]["TotalSales"]
    if total_sales >= 1e9:
        return f'${total_sales/1e9:.2f}B'
    elif total_sales >= 1e6:
        return f'${total_sales/1e6:.2f}M'
    else:
        return f'${total_sales:,.2f}'

@callback(
    Output('total-orders-value', 'children'),
    Input('url', 'pathname')
)
def update_total_orders_value(pathname):
    df = get_total_orders()
    return f'{df.iloc[0]["TotalOrders"]:,}'

@callback(
    Output('total-revenue-value', 'children'),
    Input('url', 'pathname')
)
def update_total_revenue_value(pathname):
    df = get_total_revenue()
    total_revenue = df.iloc[0]["TotalRevenue"]
    if total_revenue >= 1e9:
        return f'${total_revenue/1e9:.2f}B'
    elif total_revenue >= 1e6:
        return f'${total_revenue/1e6:.2f}M'
    else:
        return f'${total_revenue:,.2f}'

@callback(
    Output('ongoing-orders-value', 'children'),
    Input('url', 'pathname')
)
def update_ongoing_orders_value(pathname):
    df = get_ongoing_orders()
    return f'{df.iloc[0]["OngoingOrders"]:,}'

@callback(
    Output('pending-orders-value', 'children'),
    Input('url', 'pathname')
)
def update_pending_orders_value(pathname):
    df = get_pending_orders()
    return f'{df.iloc[0]["PendingOrders"]:,}'

@callback(
    Output('completed-orders-value', 'children'),
    Input('url', 'pathname')
)
def update_completed_orders_value(pathname):
    df = get_completed_orders()
    return f'{df.iloc[0]["CompletedOrders"]:,}'


@callback(
    Output('delayed-deliveries-value', 'children'),
    Input('url', 'pathname')
)
def update_delayed_deliveries_value(pathname):
    df = get_delayed_deliveries()
    return f'{df.iloc[0]["DelayedDeliveries"]:,}'





# Callback for the top companies by opportunity value
@callback(
    Output('top-companies-value-chart', 'figure'),
    Input('url', 'pathname')
)

def update_top_companies_value_chart(pathname):
    df = get_top_companies_by_opportunity_value()
    
    print(df.head())  # Check the DataFrame content
    print(df.columns)  # Check the column names

    # Ensure TotalEstimatedValue is numeric
    df['TotalEstimatedValue'] = pd.to_numeric(df['TotalEstimatedValue'], errors='coerce')
    df.dropna(subset=['TotalEstimatedValue'], inplace=True)  # Drop NaN values

    # Filter for values greater than x (e.g., x = 1000)
    x = 1000
    df = df[df['TotalEstimatedValue'] > x]

    # Log the scales of the bars
    print("Filtered DataFrame for TotalEstimatedValue > {}: \n{}".format(x, df[['company_name', 'TotalEstimatedValue']]))

    # Create the bar chart with adjusted width and custom color scheme
    fig = px.bar(df, x='company_name', y='TotalEstimatedValue', 
                 color='TotalEstimatedValue',
                 color_continuous_scale=['#55A0B0', '#7FBAC4', '#A9D4D9', '#D3E9ED'],
                #  title='Top Companies by Opportunity Value',
                 width=600)  # Set width to a valid value (e.g., 600 pixels)

    # Update layout to place legend above the chart
    fig.update_layout(
        margin=dict(l=10, r=10, t=40, b=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='"Segoe UI", "Helvetica Neue", "Helvetica", Arial, sans-serif', size=12),
        legend=dict(title='Total Estimated Value', orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5)  # Legend on top
    )
    
    return fig

# Callback for opportunity status distribution
@callback(
    Output('opportunity-status-chart', 'figure'),
    Input('url', 'pathname'),
    Input('status-filter', 'value')
)
def update_opportunity_status_chart(pathname, selected_status):
    df = get_opportunity_status_distribution()
    
    # Filter the DataFrame based on the selected status
    if selected_status != 'All':
        df = df[df['Status'] == selected_status]
    
    fig = px.bar(df, x='company_name', y='StatusCount', color='Status',
                 color_discrete_sequence=color_scheme,
                 barmode='group')
    
    fig = apply_chart_style(fig, 'Opportunity Status Distribution')
    
    return fig

# Callback for company sales by payment status
@callback(
    Output('company-sales-chart', 'figure'),
    Input('url', 'pathname'),
    Input('payment-status-filter', 'value')  # This should match the ID in the layout
)
def update_company_sales_chart(pathname, selected_payment_status):
    df = get_company_sales_by_payment_status()
    
    # Filter the DataFrame based on the selected payment status
    if selected_payment_status != 'All':
        df = df[df['payment_status'] == selected_payment_status]
    
    fig = px.bar(df, x='company_name', y='TotalSales', color='payment_status',
                #  title='Company Sales by Payment Status',
                 barmode='group')
    
    fig.update_layout(
        margin=dict(l=10, r=10, t=40, b=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='"Segoe UI", "Helvetica Neue", "Helvetica", Arial, sans-serif', size=12)
    )
    
    return fig
@callback(
    Output('customer-distribution-chart', 'figure'),
    Input('url', 'pathname')
)
def update_customer_distribution_chart(pathname):
    df = get_customer_distribution_by_country_and_city()
    
    fig = px.bar(df, x='country', y='CustomerCount', color='city',
                 barmode='group')

@callback(
    Output('customer-gender-chart', 'figure'),
    Input('url', 'pathname')
)
def update_customer_gender_chart(pathname):
    df = get_customer_distribution_by_gender()
    
    fig = px.bar(df, x='gender', y='CustomerCount')
    
@callback(
    Output('customer-job-titles-chart', 'figure'),
    Input('url', 'pathname')
)
def update_customer_job_titles_chart(pathname):
    df = get_customer_job_titles()
    
    fig = px.bar(df, x='JobTitle', y='CustomerCount', title='Customer Count by Job Title', labels={'JobTitle': 'Job Title', 'CustomerCount': 'Number of Customers'}, text='CustomerCount')

