# app.py
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import Dash

from callbacks import *
from layout import app_layout  # Import the main layout


# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True  # Add this line

app.title = "SCM Inc"


app.layout = app_layout

# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)
