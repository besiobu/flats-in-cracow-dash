import dash_html_components as html

from src.sliders import *
from src.styles import *

# Divs - forms - sliders
area_div = html.Div(children=[html.Label('Area, \u33A1:'), area_slider], 
                    style=slider_style)

room_div = html.Div(children=[html.Label('Rooms:'), room_slider], 
                    style=slider_style)

bathroom_div = html.Div(children=[html.Label('Bathrooms:'), bathroom_slider], 
                        style=slider_style)

form_sliders = [html.H4('Area & rooms', style=slider_header_style), 
                area_div, 
                room_div, 
                bathroom_div]