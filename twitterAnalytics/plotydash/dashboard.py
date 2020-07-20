import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd

def create_dashboard(server):
    """Create a Plotly Dashboard"""    
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/'
    )
    
    dash_app.layout = html.Div(children=[
        # html.H1(children='Hours of the day with more activity'),
        dcc.Location(id='url', refresh=False),
        html.H1(children='Tweets overtime:'),

        html.Div(children='''
            Test: Hours of the day with more activity.
        '''),
        html.Div(id='selectedReport'),

        dcc.Graph(
            id='hours_activity',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization'
                }
            }
        )
    ])

    init_callbacks(dash_app)

    return dash_app.server

def init_callbacks(dash_app):
    @dash_app.callback(dash.dependencies.Output('selectedReport', 'children'), [dash.dependencies.Input('url', 'pathname')])
    def display_page(pathname): # pylint: disable=unused-variable
        return html.Div([
            html.H3('Your selected report is {}'.format(pathname))
        ])