import dash_bootstrap_components as dbc

from src.about import *
from src.form import *
from src.links import *
from src.predictions import *
from src.slider_containers import *
from src.title import *

# Responsive layout
middle_col_left = {'offset': 0, 'order': 1, 'width': 8}
middle_col_right = {'offset': 0, 'order': 2, 'width': 4}

form_col_left = {'offset': 0, 'order': 1, 'width': 4}
form_col_center = {'offset': 0, 'order': 2, 'width': 4}
form_col_right = {'offset': 0, 'order': 3, 'width': 4}

# Rows, in order of appearance
title_row = dbc.Row(children=[dbc.Col(children=title, 
                                      xs=12, 
                                      sm=12, 
                                      md=12, 
                                      lg=12, 
                                      xl=6)], 
                    justify='center')


middle_about_row = dbc.Row(children=[dbc.Col(children=about_div, 
                                             xs=12, 
                                             sm=12, 
                                             md=12, 
                                             lg=12, 
                                             xl=6)], 
                           justify='center')

# middle = [html.Div(children=[chart_div, stats_div])]

middle_row = dbc.Row(children=[dbc.Col(children=chart_div, 
                                       xs=middle_col_left, 
                                       sm=middle_col_left, 
                                       md=middle_col_left, 
                                       lg=middle_col_left, 
                                       xl=4),
                               dbc.Col(children=stats_div, 
                                       xs=middle_col_right, 
                                       sm=middle_col_right, 
                                       md=middle_col_right, 
                                       lg=middle_col_right, 
                                       xl=2)], 
                     justify='center')

form_sliders_row = dbc.Row(children=[dbc.Col(children=form_sliders, 
                                             xs=12,
                                             sm=12, 
                                             md=12, 
                                             lg=12, 
                                             xl=6)], 
                           justify='center')

# Form headers
center_form_header = html.H4('Property type', style=form_header_style)
right_form_header = html.H4('Extras', style=form_header_style)
left_form_header = html.H4('Basic information', style=form_header_style)


# Basic info
form_left = html.Div(children=[left_form_header,
                               buyer_div,
                               district_div,        
                               new_div], 
                     style=form_col_style)

# Other information
form_center = html.Div(children=[center_form_header,
                                 block_div,
                                 townhouse_div,                                 
                                 apartment_div,
                                 studio_div,
                                 basement_div], 
                       style=form_col_style)

# Extras
form_right = html.Div(children=[right_form_header,
                                parking_div,
                                garden_div,
                                balcony_div,
                                terrace_div,
                                busstop_div], 
                      style=form_col_style)

form_drops_row = dbc.Row(children=[dbc.Col(children=form_left, 
                                           xs=form_col_left, 
                                           sm=form_col_left, 
                                           md=form_col_left, 
                                           lg=form_col_left, 
                                           xl=2),
                                   dbc.Col(children=form_center, 
                                           xs=form_col_center, 
                                           sm=form_col_center, 
                                           md=form_col_center, 
                                           lg=form_col_center, 
                                           xl=2),
                                   dbc.Col(children=form_right, 
                                           xs=form_col_right, 
                                           sm=form_col_right, 
                                           md=form_col_right, 
                                           lg=form_col_right, 
                                           xl=2)], 
                         justify='center')

# Footer
bottom = html.Div(children=[github_link], 
                  style=bottom_style)     

bottom_row = dbc.Row(children=[dbc.Col(children=bottom, 
                                       xs=12, 
                                       sm=12, 
                                       md=12, 
                                       lg=12, 
                                       xl=6)], 
                     justify='center')
