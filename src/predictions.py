import dash_html_components as html
import dash_bootstrap_components as dbc

from src.styles import *
from src.tooltips import *

stats_header_div = html.Div(children=[html.H4(children='Prediction details', 
                                              style={'float': 'left'}),
                                      dbc.Badge(children='?', 
                                                pill=True, 
                                                id='tooltip-stats', 
                                                style=badge_header_tooltip_style),
                                      dbc.Tooltip(children=stats_tooltip, 
                                                  target='tooltip-stats', 
                                                  placement='top-start')])

chart_header_div = html.Div(children=[html.H4(children='Prediction chart', 
                                              style={'float': 'left'}), 
                                      dbc.Badge(children='?', 
                                                pill=True, 
                                                id='tooltip-prediction', 
                                                style=badge_header_tooltip_style),
                                      dbc.Tooltip(children=chart_tooltip, 
                                                  target='tooltip-prediction', 
                                                  placement='top-start')])

stats_div = html.Div(children=[html.Div(children=[stats_header_div,
                                                  html.Div(id='pred-stats')])], 
                                        style=about_style)

chart_div = html.Div(children=[html.Div(children=[chart_header_div,
                                                  html.Div(id='prediction')])], 
                     style=chart_style)