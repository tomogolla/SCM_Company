# dash_components.py
from dash import html, dcc
import dash_bootstrap_components as dbc


# dash_components.py
import dash_bootstrap_components as dbc
from dash import html

def create_metric_card(title, id, value, bg_color="light"):
    return dbc.Card(
        dbc.CardBody([
            html.H4(title, className="card-title", style={"fontSize": "18px", "textAlign": "left"}),
            html.H2(value, id=id, className="total-text", style={"fontSize": "16px", "textAlign": "left"}),  # Placeholder for total sales value
            html.P(
                "This is aggregate value ",                
                className="card-text", style={"fontSize": "9px", "textAlign": "left"}
            ),
            
            dbc.CardLink("See more", href="#"),
            dbc.CardLink("Analyze", href="#"),
        ]
    ),
              
        style={
            "width": "300px",
            "hight": "200px",
            "textAlign": "left",
            "margin": "10px",
            "border": "none",
            "padding-left": "30px"
            },
        #className="shadow-sm",  # Add some shadow for better visual
    )
def create_insights_card(title, value, id, drilldown_arrow="↓", bg_color="#3a4b47"):
    """
    Create an insight cue card with a title, value, and an arrow for drill down.

    Parameters:
    - title: The title of the cue card (e.g., 'Ongoing Sales')
    - value: The value to be displayed in the card (e.g., '10 Orders')
    - id: The ID for the card value (for use in callbacks)
    - drilldown_arrow: Arrow symbol indicating drill-down functionality.
    - bg_color: Background color for the cue card.

    Returns:
    - dbc.Card: Dash Bootstrap Card component.
    """
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
    
# Create a card for visualizations
def create_visual_card(title, chart_id, chart):
    return dbc.Card(
        dbc.CardBody([
            html.H4(title, className="card-title", style={"fontSize": "18px", "textAlign": "left"}),
            dcc.Graph(id=chart_id, figure=chart),  # Insert the chart directly
        ]),
        style={
            "width": "450px",
            "height": "550px",
            "margin": "10px",
            "border": "1px solid #e0e0e0",
            "boxShadow": "2px 2px 10px rgba(0, 0, 0, 0.1)"
        }
    )