import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pages.analyse as analyse
import pages.dashboard as dashboard

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dcc.Link("Analyse", href="/", className="nav-link")),
            dbc.NavItem(dcc.Link("Portefeuille", href="/dashboard", className="nav-link")),
        ],
        brand="Analyse Forex / Crypto",
        color="primary",
        dark=True,
    ),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/dashboard':
        return dashboard.layout
    return analyse.layout

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8050)