"""
This file app.py defines the dash app at a central location to be imported in all necessary locations.
This needs to be done to define and use callbacks in multiple files.
"""
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])
server = app.server