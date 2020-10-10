import dash_bootstrap_components as dbc
import dash_html_components as html

from src.dropdowns import *
from src.styles import *
from src.tooltips import *

# Forms by columns in order of appearance

# Form, first column

district_div = html.Div(children=[html.Label('District'), 
                                  dbc.Badge(children='?', 
                                            pill=True, 
                                            id='tooltip-district', 
                                            className='ml-1', 
                                            style=badge_form_tooltip_style),                                                                                                                        
                                  dbc.Tooltip(children=district_tooltip, 
                                              target='tooltip-district'),
                                  district_drop], 
                        style=drop_style)

buyer_div = html.Div(children=[html.Label('Seller'), 
                               dbc.Badge(children='?', 
                                         pill=True,
                                         id='tooltip-buyer', 
                                         className='ml-1', 
                                         style=badge_form_tooltip_style),                                                                                        
                               dbc.Tooltip(children=buyer_tooltip, 
                                           target='tooltip-buyer'), 
                               seller_drop], 
                     style=drop_style)                        

new_div = html.Div(children=[html.Label('New'), 
                             dbc.Badge(children='?', 
                                         pill=True,
                                         id='tooltip-new', 
                                         className='ml-1', 
                                         style=badge_form_tooltip_style),
                             dbc.Tooltip(children=new_tooltip, 
                                         target='tooltip-new'),
                             new_drop], 
                   style=drop_style)

# Form, second column

block_div = html.Div(children=[html.Label('Residential block'), 
                               dbc.Badge(children='?', 
                                         pill=True,
                                         id='tooltip-block', 
                                         className='ml-1', 
                                         style=badge_form_tooltip_style),                                              
                               dbc.Tooltip(children=block_tooltip, 
                                           target='tooltip-block'), 
                               block_drop], 
                      style=drop_style)

townhouse_div = html.Div(children=[html.Label('Townhouse'), 
                                   dbc.Badge(children='?', 
                                             pill=True,
                                             id='tooltip-townhouse', 
                                             className='ml-1', 
                                             style=badge_form_tooltip_style),                                              
                                   dbc.Tooltip(children=townhouse_tooltip, 
                                               target='tooltip-townhouse'),
                                   townhouse_drop], 
                         style=drop_style)


apartment_div = html.Div(children=[html.Label('Apartment'),
                                   dbc.Badge(children='?', 
                                             pill=True,
                                             id='tooltip-apartment', 
                                             className='ml-1', 
                                             style=badge_form_tooltip_style),
                                   dbc.Tooltip(children=apartment_tooltip, 
                                               target='tooltip-apartment'),
                                   apartment_drop], 
                         style=drop_style)

studio_div = html.Div(children=[html.Label('Studio'), 
                                dbc.Badge(children='?', 
                                          pill=True,
                                          id='tooltip-studio',
                                          className='ml-1',
                                          style=badge_form_tooltip_style),
                                dbc.Tooltip(children=studio_tooltip, 
                                            target='tooltip-studio'),
                                studio_drop],
                      style=drop_style)

basement_div = html.Div(children=[html.Label('Basement'), 
                                  dbc.Badge(children='?', 
                                            pill=True,
                                            id='tooltip-basement', 
                                            className='ml-1', 
                                            style=badge_form_tooltip_style),
                                  dbc.Tooltip(children=basement_tooltip, 
                                              target='tooltip-basement'),
                                  basement_drop], 
                    style=drop_style)

# Form, third column

parking_div = html.Div(children=[html.Label('Parking'), 
                                 dbc.Badge(children='?', 
                                           pill=True,
                                           id='tooltip-parking', 
                                           className='ml-1', 
                                           style=badge_form_tooltip_style),
                                 dbc.Tooltip(children=parking_tooltip, 
                                             target='tooltip-parking'),
                                 parking_drop], 
                       style=drop_style)


garden_div = html.Div(children=[html.Label('Garden'), 
                                dbc.Badge(children='?', 
                                          pill=True, 
                                          id='tooltip-garden', 
                                          className='ml-1', 
                                          style=badge_form_tooltip_style),                                                                                                                        
                                dbc.Tooltip(children=garden_tooltip, 
                                            target='tooltip-garden'),
                                garden_drop],
                      style=drop_style)

balcony_div = html.Div(children=[html.Label('Balcony'), 
                                 dbc.Badge(children='?', 
                                           pill=True, 
                                           id='tooltip-balcony', 
                                           className='ml-1', 
                                           style=badge_form_tooltip_style),
                                 dbc.Tooltip(children=balcony_tooltip, 
                                             target='tooltip-balcony'),
                                 balcony_drop],                      
                     style=drop_style)

terrace_div = html.Div(children=[html.Label('Terrace'), 
                                 dbc.Badge(children='?', 
                                           pill=True, 
                                           id='tooltip-terrace', 
                                           className='ml-1', 
                                           style=badge_form_tooltip_style),                                                                                        
                                 dbc.Tooltip(children=terrace_tooltip, 
                                             target='tooltip-terrace'),
                                 terrace_drop], 
                       style=drop_style)

busstop_div = html.Div(children=[html.Div(children=[html.Label('Bus stops nearby'),
                                                    dbc.Badge(children='?', 
                                                              pill=True,
                                                              id='tooltip-busstop', 
                                                              style=badge_form_tooltip_style),                                                
                                                    dbc.Tooltip(children=busstop_tooltip, 
                                                                target='tooltip-busstop')]), 
                                 busstop_drop], 
                    style=drop_style)