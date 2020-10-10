import dash_core_components as dcc

from src.dropdown_options import *

# Categorical dropdowns
district_drop = dcc.Dropdown(id='district-dropdown', 
                             options=sorted(district_opts, key=lambda x: x['label']), 
                             value='stare miasto', 
                             searchable=False, 
                             clearable=False)

propterty_drop = dcc.Dropdown(id='property-dropdown', 
                              options=property_opts, 
                              value='flat', 
                              searchable=False, 
                              clearable=False)

seller_drop = dcc.Dropdown(id='seller-dropdown', 
                           options=seller_opts, 
                           value='realtor', 
                           searchable=False, 
                           clearable=False)

parking_drop = dcc.Dropdown(id='parking-dropdown', 
                            options=sorted(parking_opts, key=lambda x: x['label']), 
                            value='no parking', 
                            searchable=False, 
                            clearable=False)

# Binary dropdowns
garden_drop = dcc.Dropdown(id='garden-dropdown', 
                           options=bin_opts, 
                           value=0,
                           searchable=False, 
                           clearable=False)

basement_drop = dcc.Dropdown(id='basement-dropdown', 
                         options=bin_opts, 
                         value=0,
                         searchable=False, 
                         clearable=False)

balcony_drop = dcc.Dropdown(id='balcony-dropdown', 
                            options=bin_opts, 
                            value=0,
                            searchable=False, 
                            clearable=False)

terrace_drop = dcc.Dropdown(id='terrace-dropdown',
                            options=bin_opts, 
                            value=0,
                            searchable=False, 
                            clearable=False)

new_drop = dcc.Dropdown(id='new-dropdown',
                        options=bin_opts, 
                        value=0,
                        searchable=False, 
                        clearable=False)

block_drop = dcc.Dropdown(id='block-dropdown',
                          options=bin_opts, 
                          value=0,
                          searchable=False, 
                          clearable=False)

townhouse_drop = dcc.Dropdown(id='townhouse-dropdown',
                              options=bin_opts, 
                              value=0,
                              searchable=False, 
                              clearable=False)

apartment_drop = dcc.Dropdown(id='apartment-dropdown', 
                              options=bin_opts, 
                              value=0,
                              searchable=False, 
                              clearable=False)

busstop_drop = dcc.Dropdown(id='busstop-dropdown', 
                            options=bin_opts, 
                            value=0,
                            searchable=False, 
                            clearable=False)

studio_drop = dcc.Dropdown(id='studio-dropdown', 
                           options=bin_opts, 
                           value=0,
                           searchable=False, 
                           clearable=False)