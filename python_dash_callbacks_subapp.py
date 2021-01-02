"""
This file defines the callbacks used in index.py.
This needs to be done to define and use callbacks in multiple files.
"""
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from python_dash_callbacks_app import app

def get_body():
    dropdown_timespan = dcc.Dropdown(options=[
                                        {"label": "1 Month", "value": 1},
                                        {"label": "3 Months", "value": 3},
                                        {"label": "6 Months", "value": 6},
                                        # {"label": "1 Year", "value": 12},
                                        # {"label": "5 Years", "value": 60},
                                        {"label": "Full", "value": -1}
                                        ],
                                        value=-1,
                                        multi=True,
                                        id="dropdown-timespan"
                                    )

    body = [
        dropdown_timespan,
        html.Div(id="content")
    ]

    @app.callback(Output("content", "children"),
                  Input("dropdown-timespan", "value"))
    def set_dropdown(item):
        print(type(item), item)
        if item == 1 or item == [1]:
            return (html.Div("1 Month"))
        elif item == -1 or item == [-1]:
            return (html.Div("Full Test"))
        elif item == []:
            return (html.Div("Select an Item please!"))

    return(body)