# layout.py
from dash import html, dcc
import dash_bootstrap_components as dbc
from datetime import date, timedelta

# Define the font style
font_style = {
    'fontFamily': '"Segoe UI", "Helvetica Neue", "Helvetica", Arial, sans-serif',
}

# Main layout of the dashboard
layout = dbc.Container([
    # Top Bar
    dbc.Row([
        dbc.Col(
            html.Div(
                className="top-bar",
                style={
                    'display': 'flex',
                    'justifyContent': 'space-between',
                    'alignItems': 'center',
                    'backgroundColor': '#333',
                    'color': 'white',
                    'padding': '10px 20px',
                    'width': '100%',
                },
                children=[
                    html.Div("Tom Ogolla.", style={'fontSize': '16px'}),
                    html.Div(
                        style={'display': 'flex', 'alignItems': 'center'},
                        children=[
                            dcc.Input(
                                placeholder='Search...',
                                style={'marginRight': '20px', 'padding': '5px', 'borderRadius': '0px', 'border': '1px solid #ccc', 'width': '100px', 'height': '20px', 'fontSize': '12px'}
                            ),
                            html.Div(className="notification-icon", style={'marginRight': '20px'}),
                            html.Div("T", style={
                                'backgroundColor': '#55A0B0',
                                'borderRadius': '50%',
                                'width': '20px',
                                'height': '20px',
                                'display': 'flex',
                                'alignItems': 'center',
                                'justifyContent': 'center',
                                'color': 'white',
                                'fontSize': '12px'
                            }),
                        ]
                    )
                ]
            ),
            width=12
        )
    ], style={'marginBottom': '20px'}),
    # Navigation Bar 1
    dbc.Row([
        dbc.Col(
            html.Div(
                className="nav-bar",
                style={
                    'display': 'flex',
                    'justifyContent': 'space-between',
                    'backgroundColor': '#fff',
                    'padding': '10px 20px',
                    'width': '90%',
                    'margin': '0 auto',
                },
                children=[
                    dcc.Link("SCM Company Limited.", href="/", style={'marginRight': '20px', 'textDecoration': 'underline', 'testSize': '18px', 'color': 'black'}, refresh=True),                
                    html.Div("|", style={'marginRight': '5px', 'marginLeft': '7px', 'color': '#333'}),
                    dcc.Link("Insights", href="/insights", style={'marginRight': '10px', 'textDecoration': 'none', 'textSize': '16px', 'color': '#55A0B0'}),                    
                    dcc.Link("Sales Performance", href="/sales-performance", style={'marginRight': '10px', 'textDecoration': 'none', 'textSize': '16px', 'color': '#55A0B0'}),
                    dcc.Link("Opportunities Overview", href="/opportunities-overview", style={'marginRight': '10px', 'textDecoration': 'none', 'textSize': '16px', 'color': '#55A0B0'}),
                    dcc.Link("Orders Overview", href="/orders-overview", style={'textDecoration': 'none', 'textSize': '16px', 'color': '#55A0B0'}),
                ]
            ),
            width=12
        )
    ], style={'marginBottom': '7px', 'padding': '0px'}),

    # Navigation Bar 2
    dbc.Row([
        dbc.Col(
            html.Div(
                className="nav-bar",
                style={
                    'display': 'flex',
                    'justifyContent': 'flex-start',
                    'backgroundColor': '#fff',
                    'padding': '10px 20px',
                    'width': '90%',
                    'margin': '0 auto',
                },
                children=[
                    dcc.Link("Customers", href="/customers", style={'marginRight': '20px', 'textDecoration': 'none', 'textSize': '16px', 'color': '#55A0B0'}),
                    dcc.Link("Orders", href="/orders", style={'marginRight': '20px', 'textDecoration': 'none', 'textSize': '16px', 'color': '#55A0B0'}),
                    dcc.Link("Suppliers", href="/suppliers", style={'marginRight': '20px', 'textDecoration': 'none', 'textSize': '16px', 'color': '#55A0B0'}),
                    dcc.Link("Salespeople", href="/salespeople", style={'textDecoration': 'none', 'textSize': '16px', 'color': '#55A0B0'}),
                ]
            ),
            width=12
        )
    ], style={'marginBottom': '7px', 'padding': '0px'}),

    # Content Area
    html.Div(
        className="content",
        style={'padding': '0px', 'width': '90%', 'margin': '0 auto'},
        children=[
            html.H2("Sales are up by 22.43%", style={'fontSize': '25px', **font_style}),
            html.P("Get started with Pending Orders ... >", style={'marginBottom': '30px', 'fontSize': '18px', **font_style}),

            # Activities Section
            html.H3("Activities", style={'fontSize': '20px', **font_style}),
            html.Hr(style={'border': '1px solid #333'}),
            dbc.Row([
                dbc.Col(
                    html.Div([
                        html.H2("Total sales", style={'fontSize': '16px', 'marginBottom': '10px', 'fontWeight': 'normal', 'paddingLeft': '5px', 'marginTop': '10px', **font_style}),
                        html.Div(id='total-sales-value', style={'fontSize': '27px', 'fontWeight': 'normal', 'width': '100%', 'whiteSpace': 'nowrap', 'overflow': 'hidden', 'textOverflow': 'ellipsis', 'paddingLeft': '5px', **font_style})
                    ],
                    style={
                        'width': '110px',
                        'height': '130px',
                        'backgroundColor': '#fff',
                        'display': 'flex',
                        'flexDirection': 'column',
                        'justifyContent': 'flex-start',
                        'alignItems': 'flex-start'
                    }),
                    width='auto'
                ),
                dbc.Col(
                    html.Div([
                        html.H2("Total revenue", style={'fontSize': '16px', 'marginBottom': '10px', 'fontWeight': 'normal', 'paddingLeft': '5px', 'marginTop': '10px', **font_style}),
                        html.Div(id='total-revenue-value', style={'fontSize': '27px', 'fontWeight': 'bold', 'width': '100%', 'whiteSpace': 'nowrap', 'overflow': 'hidden', 'textOverflow': 'ellipsis', 'paddingLeft': '5px', **font_style})
                    ],
                    style={
                        'width': '110px',
                        'height': '130px',
                        'backgroundColor': 'fff',
                        'display': 'flex',
                        'flexDirection': 'column',
                        'justifyContent': 'flex-start',
                        'alignItems': 'flex-start'
                    }),
                    width='auto'
                ),
                dbc.Col(
                    html.Div([
                        html.H2("Total Orders", style={'fontSize': '16px', 'marginBottom': '10px', 'fontWeight': 'normal', 'paddingLeft': '5px', 'marginTop': '10px', **font_style}),
                        html.Div(id='total-orders-value', style={'fontSize': '27px', 'fontWeight': 'bold', 'width': '100%', 'whiteSpace': 'nowrap', 'overflow': 'hidden', 'textOverflow': 'ellipsis', 'paddingLeft': '5px', **font_style})
                    ],
                    style={
                        'width': '110px',
                        'height': '130px',
                        'backgroundColor': '#fff',
                        'display': 'flex',
                        'flexDirection': 'column',
                        'justifyContent': 'flex-start',
                        'alignItems': 'flex-start'
                    }),
                    width='auto'
                ),
            ], justify='start', style={'marginLeft': '30px'}),

            # Insights Section
            html.H3("Insights", style={'fontSize': '22px', **font_style}),
            html.Hr(style={'border': '1px solid #333'}),
            dbc.Row([
                dbc.Col(
                    html.Div([
                        html.H2("Ongoing orders", style={'fontSize': '10px', 'marginTop': '10px', 'fontWeight': '100', 'paddingLeft': '5px', **font_style}),
                        html.Div(id='ongoing-orders-value', style={'fontSize': '36px', 'fontWeight': '100', 'width': '100%', 'whiteSpace': 'nowrap', 'overflow': 'hidden', 'textOverflow': 'ellipsis', 'paddingLeft': '5px', **font_style})
                    ],
                    style={
                        'width': '110px',
                        'height': '130px',
                        'backgroundColor': '#A0D1D1',
                        'display': 'flex',
                        'flexDirection': 'column',
                        'justifyContent': 'flex-start',
                        'alignItems': 'flex-start'
                    }),
                    width='auto'
                ),
                dbc.Col(
                    html.Div([
                        html.H2("Pending Orders", style={'fontSize': '10px', 'marginBottom': '10px', 'fontWeight': '100', 'paddingLeft': '5px', 'marginTop': '10px', **font_style}),
                        html.Div(id='pending-orders-value', style={'fontSize': '36px', 'fontWeight': '100', 'width': '100%', 'whiteSpace': 'nowrap', 'overflow': 'hidden', 'textOverflow': 'ellipsis', 'paddingLeft': '5px', **font_style})
                    ],
                    style={
                        'width': '110px',
                        'height': '130px',
                        'backgroundColor': '#A0D1D1',
                        'display': 'flex',
                        'flexDirection': 'column',
                        'justifyContent': 'flex-start',
                        'alignItems': 'flex-start'
                    }),
                    width='auto'
                ),
                dbc.Col(
                    html.Div([
                        html.H2("Completed Orders", style={'fontSize': '10px', 'marginBottom': '10px', 'fontWeight': '100', 'paddingLeft': '5px', 'marginTop': '10px', **font_style}),
                        html.Div(id='completed-orders-value', style={'fontSize': '36px', 'fontWeight': '100', 'width': '100%', 'whiteSpace': 'nowrap', 'overflow': 'hidden', 'textOverflow': 'ellipsis', 'paddingLeft': '5px', **font_style})
                    ],
                    style={
                        'width': '110px',
                        'height': '130px',
                        'backgroundColor': '#A0D1D1',
                        'display': 'flex',
                        'flexDirection': 'column',
                        'justifyContent': 'flex-start',
                        'alignItems': 'flex-start'
                    }),
                    width='auto'
                ),
                dbc.Col(
                    html.Div([
                        html.H2("Delayed deliveries", style={'fontSize': '10px', 'marginBottom': '10px', 'fontWeight': '100', 'paddingLeft': '5px', 'marginTop': '10px', **font_style}),
                        html.Div(id='delayed-delveries-value', style={'fontSize': '36px', 'fontWeight': '100', 'width': '100%', 'whiteSpace': 'nowrap', 'overflow': 'hidden', 'textOverflow': 'ellipsis', 'paddingLeft': '5px', **font_style})
                    ],
                    style={
                        'width': '110px',
                        'height': '130px',
                        'backgroundColor': '#A0D1D1',
                        'display': 'flex',
                        'flexDirection': 'column',
                        'justifyContent': 'flex-start',
                        'alignItems': 'flex-start'
                    }),
                    width='auto'
                ),
            ], justify='start', style={'marginLeft': '10px'}),

            # Dashboards Section
            html.H3("Dashboards", style={'fontSize': '22px', **font_style}),
            html.Hr(style={'border': '1px solid #333'}),
            dbc.Row([
               
            ], justify='between'),

            # Companies Section
            html.Div(
                className="companies-section",
                style={'padding': '0px', 'width': '100%', 'margin': '0 auto'},
                children=[
                    html.H2("Companies Information", style={'fontSize': '18px', **font_style}),
                    html.Hr(),
                    # Add this section in the Companies Section before the charts
                    html.Div(
                        className="filter-section",
                        style={'padding': '10px', 'marginBottom': '20px'},
                        children=[
                            dbc.Row([
                                dbc.Col(
                                    [
                                        html.H5("Filter by Opportunity Status", style={'fontSize': '14px'}),
                                        dcc.Dropdown(
                                            id='status-filter',
                                            options=[
                                                {'label': 'All', 'value': 'All'},
                                                {'label': 'Open', 'value': 'Open'},
                                                {'label': 'Closed', 'value': 'Closed'},
                                                # Add more statuses as needed
                                            ],
                                            value='All',  # Default value
                                            clearable=False,
                                            style={'width': '100%'}
                                        ),
                                    ],
                                    width=3
                                ),
                                dbc.Col(
                                    [
                                        html.H5("Filter by Payment Status", style={'fontSize': '14px'}),
                                        dcc.Dropdown(
                                            id='payment-status-filter',  # Ensure this ID matches the callback
                                            options=[
                                                {'label': 'All', 'value': 'All'},
                                                {'label': 'Paid', 'value': 'Paid'},
                                                {'label': 'Pending', 'value': 'Pending'},
                                                {'label': 'Overdue', 'value': 'Overdue'},
                                                # Add more payment statuses as needed
                                            ],
                                            value='All',  # Default value
                                            clearable=False,
                                            style={'width': '100%'}
                                        ),
                                    ],
                                    width=3
                                ),
                            ], justify='end', className='g-0')
                        ]
                    ),
                    dbc.Row([
                        dbc.Col(
                            dbc.Card([
                                dbc.Row([
                                    dbc.Col(html.H5("Top Companies by Opportunity Value", style={'fontSize': '12px', 'fontWeight': 'normal', 'padding-top': '5px'}), width=12)
                                ], className="mb-3"),
                                dbc.Row([
                                    dbc.Col(dcc.Graph(id='top-companies-value-chart'), width=12)
                                ])
                            ], style={'borderRadius': '0'}),
                            width=4
                        ),
                        dbc.Col(
                            dbc.Card([
                                dbc.Row([
                                    dbc.Col(html.H5("Opportunity Status Distribution", style={'fontSize': '12px', 'fontWeight': 'normal', 'padding-top': '5px'}), width=12)
                                ], className="mb-3"),
                                dbc.Row([
                                    dbc.Col(dcc.Graph(id='opportunity-status-chart'), width=12)
                                ])
                            ], style={'borderRadius': '0'}),
                            width=4
                        ),
                        dbc.Col(
                            dbc.Card([
                                dbc.Row([
                                    dbc.Col(html.H5("Company Sales by Payment Status", style={'fontSize': '12px', 'fontWeight': 'normal', 'padding-top': '5px'}), width=12)
                                ], className="mb-3"),
                                dbc.Row([
                                    dbc.Col(dcc.Graph(id='company-sales-chart'), width=12)
                                ])
                            ], style={'borderRadius': '0'}),
                            width=4
                        ),
                    ], style={'width': '100%', 'margin': '0 auto'}),
                ]
            ),
            # Add this section to your existing layout
            html.Div(
                className="map-section",
                style={'padding': '0px', 'width': '100%', 'margin': '0 auto'},
                children=[
                    html.H2("Company Locations and Opportunities", style={'fontSize': '18px', **font_style}),
                    dbc.Card([
                        dbc.Row([
                            dbc.Col(html.H5("Company Locations and Opportunities", style={'fontSize': '12px', 'fontWeight': 'normal', 'padding-top': '5px'}), width=12)
                        ], className="mb-3"),
                        dbc.Row([
                            dbc.Col(dcc.Graph(id='company-locations-map'), width=12)
                        ])
                    ], style={'width': '100%', 'margin': '0 auto', 'borderRadius': '0'})
                ]
            ),
            html.Div(
                className="customers-section",
                style={'padding': '0px', 'width': '100%', 'margin': '0 auto'},
                children=[
                    html.H2("Customer Analytics", style={'fontSize': '18px', **font_style}),
                    html.Hr(),
                    dbc.Row([
                        dbc.Col(html.Div("Customer Distribution by Country and City", style={'fontSize': '12px', 'fontWeight': 'normal', 'padding-top': '5px'}), width=12)
                    ]),
                    dbc.Row([
                        dbc.Col(dcc.Graph(id='customer-distribution-chart'), width=6),
                        dbc.Col(dcc.Graph(id='customer-gender-chart'), width=6)
                    ]),
                    dbc.Row([
                        dbc.Col(dcc.Graph(id='customer-job-titles-chart'), width=12)
                    ])
                ]
            )
        ]
    )
], fluid=True)
