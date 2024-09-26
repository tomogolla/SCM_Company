import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

import plotly.express as px

df = pd.read_csv('cleaned_sales_data.csv')


def create_dash_app(flask_app):
    dash_app = dash.Dash(
        __name__,
        server=flask_app,
        routes_pathname_prefix='/dash/'
    )

    # Create a simple figure (scatter plot, bar chart, etc.)
    fig = px.scatter(df, x='sales', y='status', color='status')

    # Define the Dash layout
    dash_app.layout = html.Div([
        dcc.Graph(id='basic-chart', figure=fig),
        html.Label('Select Category:'),
        dcc.Dropdown(
            id='dropdown',
            options=[{'label': cat, 'value': cat} for cat in df['status'].unique()],
            value=df['status'].unique()[0]
        )
    ])


def init_dashboard(server):
    # Initialize Dash app
    dash_app = dash.Dash(__name__, server=server, routes_pathname_prefix='/dash/')

    # Load the CSV data
   

    # Define the layout and graphs
    dash_app.layout = html.Div([
        dcc.Dropdown(
            id='dropdown',
            options=[{'label': col, 'value': col} for col in df.columns],
            value='sales'
        ),
        dcc.Graph(id='my-graph'),
        dcc.Checklist(
            id='filter-options',
            options=[{'label': 'Show Sales', 'value': 'sales'}],
            value=['sales']
        ),
        html.Div(id='kpi-cards'),
    ])

    # Callbacks to update graphs and KPIs
    @dash_app.callback(
        Output('my-graph', 'figure'),
        [Input('dropdown', 'value'), Input('filter-options', 'value')]
    )
    def update_graph(selected_column, filter_values):
        filtered_df = df[filter_values]
        figure = {
            'data': [{'x': df['customername'], 'y': df[selected_column], 'type': 'bar'}]
        }
        return figure

    @dash_app.callback(
        Output('kpi-cards', 'children'),
        [Input('dropdown', 'value')]
    )
    def update_kpi(selected_column):
        # Generate KPI values based on the selected column
        kpi_value = df[selected_column].sum()
        return f"Total {selected_column}: {kpi_value}"

    return dash_app
