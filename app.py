import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

from src.Model import Model, generate_features

# Models
gbr = Model(name='gbr').load()
mlp = Model(name='mlp').load()
vote = Model(name='vote').load()

models = [gbr, mlp, vote]

# App
district_opts = [
    {'label': 'Stare Miasto', 'value': 'stare miasto'},
    {'label': 'Grzegórzki', 'value': 'grzegorzki'},
    {'label': 'Prądnik Czerwony', 'value': 'pradnik czerwony'},                          
    {'label': 'Prądnik Biały', 'value': 'pradnik bialy'},             
    {'label': 'Krowodrza', 'value': 'krowodrza'},
    {'label': 'Bronowice', 'value': 'bronowice'},
    {'label': 'Zwierzyniec', 'value': 'zwierzyniec'},
    {'label': 'Dębniki', 'value': 'debniki'},
    {'label': 'Łagiewniki', 'value': 'lagiewniki'},
    {'label': 'Borek Fałęcki', 'value': 'borek falecki'},
    {'label': 'Swoszowice', 'value': 'swoszowice'},                                                    
    {'label': 'Podgórze Duchackie', 'value': 'podgorze duchackie'},                          
    {'label': 'Bieżanów', 'value': 'biezanow'},
    {'label': 'Prokocim', 'value': 'prokocim'},             
    {'label': 'Podgórze', 'value': 'podgorze'},                                       
    {'label': 'Czyżyny', 'value': 'czyzyny'},                          
    {'label': 'Mistrzejowice', 'value': 'mistrzejowice'},                          
    {'label': 'Bieńczyce', 'value': 'bienczyce'},                                       
    {'label': 'Wzgórza Krzesławickie', 'value': 'wzgorza krzeslawickie'},
    {'label': 'Nowa Huta', 'value': 'nowa huta'}
]

property_opts = [{'label': 'Flat', 'value': 'flat'}]

seller_opts = [{'label': 'Realtor', 'value': 'realtor'},
               {'label': 'Owner', 'value': 'owner'}]

parking_opts = [{'label': 'No parking', 'value': 'no parking'},
                {'label': 'Street', 'value': 'stree'},
                {'label': 'Covered', 'value': 'covered'},
                {'label': 'Garage', 'value': 'garage'}]

bin_opts = [{'label': 'Yes', 'value': 1},
            {'label': 'No', 'value': 0}]        

# Numeric sliders
# area_marks = {i: {'label': str(i), 'style': {'font-size': '1vw'}} for i in range(20, 125, 5)}

area_marks = {i: str(i) for i in range(20, 125, 5)}
area_slider = dcc.Slider(id='area-slider', min=20, max=120, 
                         step=5, value=70, marks=area_marks, 
                         included=False)

room_marks = {i: str(i) for i in range(1, 7)}
room_slider = dcc.Slider(id='room-slider', min=1, max=6, 
                         step=1, value=2, marks=room_marks,
                         included=False)

bathroom_marks = {i: str(i) for i in range(1, 6)}
bathroom_slider = dcc.Slider(id='bathroom-slider', min=1, max=5,
                             step=1, value=1, marks=bathroom_marks,
                             included=False)

# Categorical dropdowns
district_drop = dcc.Dropdown(id='district-dropdown', 
                             options=sorted(district_opts, key=lambda x: x['label']), 
                             value='stare miasto')

propterty_drop = dcc.Dropdown(id='property-dropdown', 
                              options=property_opts, 
                              value='flat')

seller_drop = dcc.Dropdown(id='seller-dropdown', 
                           options=seller_opts, 
                           value='realtor')

parking_drop = dcc.Dropdown(id='parking-dropdown', 
                            options=sorted(parking_opts, key=lambda x: x['label']), 
                            value='no parking')

# Binary dropdowns
garden_drop = dcc.Dropdown(id='garden-dropdown', 
                           options=bin_opts, 
                           value=0)

floor_drop = dcc.Dropdown(id='floor-dropdown', 
                         options=bin_opts, 
                         value=0)

balcony_drop = dcc.Dropdown(id='balcony-dropdown', 
                            options=bin_opts, 
                            value=0)

terrace_drop = dcc.Dropdown(id='terrace-dropdown',
                            options=bin_opts, 
                            value=0)

new_drop = dcc.Dropdown(id='new-dropdown',
                        options=bin_opts, 
                        value=0)

estate_drop = dcc.Dropdown(id='estate-dropdown',
                           options=bin_opts, 
                           value=0)

townhouse_drop = dcc.Dropdown(id='townhouse-dropdown',
                              options=bin_opts, 
                              value=0)

apartment_drop = dcc.Dropdown(id='apartment-dropdown', 
                              options=bin_opts, 
                              value=0)

land_drop = dcc.Dropdown(id='land-dropdown', 
                         options=bin_opts, 
                         value=0)

studio_drop = dcc.Dropdown(id='studio-dropdown', 
                           options=bin_opts, 
                           value=0)

# Links
google_maps_link = html.A(children='Cracow, Poland', 
                          href='https://goo.gl/maps/AXsGvLCugEmcd2WG7', 
                          target='_blank')

github_link = html.A(children='Github', 
                     href='https://github.com/besiobu/flats-in-cracow', 
                     target='_blank')

# Information about the page
about_text_p1 = 'On this site you can find out how much that' \
                ' flat you are thinking about buying should cost.' \
                ' The models were trained using approximately' \
                ' 3500 listings for flats in '

about_text_p2 = '. Feel free to interact with the models and' \
                ' see how different factors impact the final price.' \
                ' For more information on how the models were ' \
                ' developed checkout the projects repo.'

# Styles
title_style = {'margin': '10px',
               'text-align': 'justify'}

chart_style = {'margin': '10px', 
               'text-align': 'justify'}

about_style = {'margin': '10px', 
               'text-align': 'justify'}

slider_header_style = {'margin': '10px'}

slider_style = {'margin': '10px'}

form_header_style = {'margin-left': '10px'}

form_col_style = {'margin': '0px'}

drop_style = {'margin': '10px'}

bottom_style = {'margin': '10px'}

# Divs - forms - sliders
area_div = html.Div(children=[html.Label('Area (meters squared):'), area_slider], 
                    style=slider_style)

room_div = html.Div(children=[html.Label('Rooms:'), room_slider], 
                    style=slider_style)

bathroom_div = html.Div(children=[html.Label('Bathrooms:'), bathroom_slider], 
                        style=slider_style)

form_sliders = [html.H5('Area & rooms', style=slider_header_style), 
                area_div, 
                room_div, 
                bathroom_div]

# Divs - forms - dropdowns
district_div = html.Div(children=[html.Label('District:'), district_drop], 
                        style=drop_style)

garden_div = html.Div(children=[html.Label('Garden:'), garden_drop],
                      style=drop_style)

balcony_div = html.Div(children=[html.Label('Balcony:'), balcony_drop], 
                     style=drop_style)

terrace_div = html.Div(children=[html.Label('Terrace:'), terrace_drop], 
                       style=drop_style)

buyer_div = html.Div(children=[html.Label('Buy from:'), seller_drop], 
                     style=drop_style)

estate_div = html.Div(children=[html.Label('Estate:'), estate_drop], 
                      style=drop_style)

townhouse_div = html.Div(children=[html.Label('Townhouse:'), townhouse_drop], 
                         style=drop_style)

apartment_div = html.Div(children=[html.Label('Apartment:'), apartment_drop], 
                         style=drop_style)

studio_div = html.Div(children=[html.Label('Studio:'), studio_drop],
                      style=drop_style)

new_div = html.Div(children=[html.Label('New:'), new_drop], 
                   style=drop_style)

parking_div = html.Div(children=[html.Label('Parking:'), parking_drop], 
                       style=drop_style)

floor_div = html.Div(children=[html.Label('Ground floor:'), floor_drop], 
                    style=drop_style)

land_div = html.Div(children=[html.Label('Land:'), land_drop], 
                    style=drop_style)

about_div = html.Div(children=[html.H5('About'), 
                               html.Div(children=[about_text_p1, 
                                                  google_maps_link, 
                                                  about_text_p2])], 
                     style=about_style)

chart_div = html.Div(children=[html.Div(children=[html.H5('Prediction'), 
                               html.Div(id='prediction')])], 
                     style=chart_style)

bottom = html.Div(children=[github_link], 
                  style=bottom_style)                     

# Divs - layout, in order of appearance
title = html.Div(children=[html.H2('How much will your new flat cost ?')],
                 style=title_style)

# About
middle = [html.Div(children=[chart_div, about_div])]

# Form headers
center_form_header = html.H5('Property type', style=form_header_style)
right_form_header = html.H5('Extras', style=form_header_style)
left_form_header = html.H5('Basic information', style=form_header_style)

# Basic info
form_left = html.Div(children=[left_form_header,
                               buyer_div,
                               district_div,        
                               new_div], 
                     style=form_col_style)

# Other information
form_center = html.Div(children=[center_form_header,
                                 estate_div,
                                 townhouse_div,                                 
                                 apartment_div,
                                 studio_div,
                                 floor_div], 
                       style=form_col_style)

# Extras
form_right = html.Div(children=[right_form_header,
                                parking_div,
                                garden_div,
                                balcony_div,
                                terrace_div,
                                land_div], 
                      style=form_col_style)

# Responsive layout
middle_col_left = {'offset': 0, 'order': 1, 'width': 8}
middle_col_right = {'offset': 0, 'order': 2, 'width': 4}

form_col_left = {'offset': 0, 'order': 1, 'width': 4}
form_col_center = {'offset': 0, 'order': 2, 'width': 4}
form_col_right = {'offset': 0, 'order': 3, 'width': 4}

# Rows, in order of appearance
title_row = dbc.Row(children=[dbc.Col(title, xs=12, sm=12, md=12, lg=12, xl=6)], 
                    justify='center')

middle_row = dbc.Row(children=[dbc.Col(chart_div, xs=middle_col_left, 
                                                  sm=middle_col_left, 
                                                  md=middle_col_left, 
                                                  lg=middle_col_left, 
                                                  xl=3),
                               dbc.Col(about_div, xs=middle_col_right, 
                                                  sm=middle_col_right, 
                                                  md=middle_col_right, 
                                                  lg=middle_col_right, 
                                                  xl=3)], 
                     justify='center')

form_sliders_row = dbc.Row(children=[dbc.Col(form_sliders, xs=12, sm=12, md=12, lg=12, xl=6)], 
                           justify='center')

form_drops_row = dbc.Row(children=[dbc.Col(form_left, xs=form_col_left, 
                                                      sm=form_col_left, 
                                                      md=form_col_left, 
                                                      lg=form_col_left, 
                                                      xl=2),
                                   dbc.Col(form_center, xs=form_col_center, 
                                                        sm=form_col_center, 
                                                        md=form_col_center, 
                                                        lg=form_col_center, 
                                                        xl=2),
                                   dbc.Col(form_right, xs=form_col_right, 
                                                       sm=form_col_right, 
                                                       md=form_col_right, 
                                                       lg=form_col_right, 
                                                       xl=2)], 
                         justify='center')

bottom_row = dbc.Row(children=[dbc.Col(bottom, xs=12, sm=12, md=12, lg=12, xl=6)], 
                     justify='center')

# Dash app
meta_tags = {"name": "viewport", 
             "content": "width=device-width, initial-scale=1"}

app = dash.Dash(name=__name__, 
                external_stylesheets=[dbc.themes.FLATLY], 
                meta_tags=[meta_tags])

# Flask
server = app.server

app.title = 'Flats in Cracow'

app.layout = html.Div(children=[title_row,
                                middle_row,
                                form_sliders_row,
                                form_drops_row,
                                bottom_row])

@app.callback(
    [dash.dependencies.Output('room-slider', component_property='min'),
     dash.dependencies.Output('room-slider', component_property='max')],
    [dash.dependencies.Input('area-slider', 'value')]
)
def update_rooms_slider(area):
    """

    Update rooms slider to sensible values.

    """

    return [1, min(int(area / 30),6)]

@app.callback(
    [dash.dependencies.Output('bathroom-slider', component_property='min'),
     dash.dependencies.Output('bathroom-slider', component_property='max')],
    [dash.dependencies.Input('area-slider', 'value')]
)
def update_bathrooms_slider(area):
    """

    Update bathrooms slider to sensible values.

    """

    return [1, min(int(area / 40), 5)]    

@app.callback(
    dash.dependencies.Output('townhouse-dropdown', 'options'),
    [dash.dependencies.Input('estate-dropdown', 'value')]
)
def update_townhouse_dropdown(estate):
    """

    Limit townhouse to sensible values.

    Notes
    -----
    Townhouse and estate should be mutually exclusive.

    """

    if estate:
        opts = [{'label': 'No', 'value': 0}]        
    else:
        opts = [{'label': 'Yes', 'value': 1},
                {'label': 'No', 'value': 0}]        
    return opts

@app.callback(
    dash.dependencies.Output('estate-dropdown', 'options'),
    [dash.dependencies.Input('townhouse-dropdown', 'value')]
)
def update_estate_dropdown(estate):
    """

    Limit esate to sensible values.

    Notes
    -----
    Townhouse and estate should be mutually exclusive.

    """

    if estate:
        opts = [{'label': 'No', 'value': 0}]        
    else:
        opts = [{'label': 'Yes', 'value': 1},
                {'label': 'No', 'value': 0}]        
    return opts


@app.callback(
    dash.dependencies.Output('prediction', 'children'),
    [
        dash.dependencies.Input('district-dropdown', 'value'),           
        dash.dependencies.Input('seller-dropdown', 'value'),                                        
        dash.dependencies.Input('area-slider', 'value'),
        dash.dependencies.Input('room-slider', 'value'),        
        dash.dependencies.Input('bathroom-slider', 'value'),                
        dash.dependencies.Input('parking-dropdown', 'value'),                                
        dash.dependencies.Input('garden-dropdown', 'value'),
        dash.dependencies.Input('balcony-dropdown', 'value'),
        dash.dependencies.Input('terrace-dropdown', 'value'),
        dash.dependencies.Input('floor-dropdown', 'value'),
        dash.dependencies.Input('new-dropdown', 'value'),
        dash.dependencies.Input('estate-dropdown', 'value'),
        dash.dependencies.Input('townhouse-dropdown', 'value'),
        dash.dependencies.Input('apartment-dropdown', 'value'),
        dash.dependencies.Input('land-dropdown', 'value'),                                
        dash.dependencies.Input('studio-dropdown', 'value'),                                        
    ]    
)
def update_prediction(*args):
    """

    Retrieve predictions from model and draw
    updated chart.

    """

    x = generate_features(*args)

    preds = [mdl.predict(x) for mdl in models]
    names = [mdl.name for mdl in models]

    bar_chart = make_bar_chart(preds=preds,
                               names=names)

    return bar_chart    

def make_bar_chart(preds, names):
    """

    Draw horizontal bar char with model predictions.

    Notes
    -----
    Last predicton is plotted in darker colour.

    """

    names = [x.upper() for x in names]

    colours = ['#ABE2FB' for i in range(len(preds)-1)]
    colours += ['#3498DB']

    fig = go.Figure(go.Bar(y=names,
                           x=preds,
                           width=(0.5, 0.5, 0.5),
                           marker_color=colours,
                           orientation='h'))

    fig.update_layout(template='plotly_white',        
                      height=150,        
                      margin=dict(l=10, r=10, t=5, b=5, pad=5),
                      xaxis=dict(range=[Model.min_pred, Model.max_pred]),
                      xaxis_title=('PLN'),
                      hoverlabel=dict(bgcolor='white', 
                                      font_size=12, 
                                      font_family='Segoe UI, sans-serif'),        
                      font=dict(family="Segoe UI, sans-serif", 
                                size=12, 
                                color='#212529')
    )

    # Disable toolbar
    bar_chart = dcc.Graph(figure=fig, 
                          config={'displayModeBar': False})

    return bar_chart

if __name__ == '__main__':
    app.run_server(debug=True)
