from dash import Dash, dcc, html
from layouts import layout
import dash_bootstrap_components as dbc

from callbacks import *

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Add dcc.Location to the layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # This is the URL component
    layout
])

if __name__ == '__main__':
    app.run_server(debug=True)