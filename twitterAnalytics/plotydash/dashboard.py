import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd

def create_dashboard(server):
    """Create a Plotly Dashboard"""    
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        suppress_callback_exceptions=False
    )
    
    dash_app.layout = html.Div(children=[        
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])
    init_callbacks(dash_app)
    return dash_app.server

def init_callbacks(dash_app):
    @dash_app.callback(dash.dependencies.Output('page-content', 'children'), [dash.dependencies.Input('url', 'pathname')])
    def display_page(pathname): # pylint: disable=unused-variable
        rType, rName = clean_pathname(pathname)
        return html.Div([
            html.H3('Your selected report type is {}'.format(rType)),
            html.H3('Your report name is {}'.format(rName))
        ])

def clean_pathname(pathname):
    txt = pathname.replace('/dashapp/', '')
    rType = txt[0]
    rName = txt[2:]
    return rType, rName