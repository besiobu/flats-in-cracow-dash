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

# App components
# Categorical options
district_opts = [
    {'label': 'Stare Miasto', 'value': 'stare miasto'},
    {'label': 'Grzegórzki', 'value': 'grzegórzki'},
    {'label': 'Prądnik Czerwony', 'value': 'prądnik czerwony'},                          
    {'label': 'Prądnik Biały', 'value': 'prądnik biały'},             
    {'label': 'Krowodrza', 'value': 'krowodrza'},
    {'label': 'Bronowice', 'value': 'bronowice'},
    {'label': 'Zwierzyniec', 'value': 'zwierzyniec'},
    {'label': 'Dębniki', 'value': 'dębniki'},
    {'label': 'Łagiewniki', 'value': 'łagiewniki'},
    {'label': 'Borek Fałęcki', 'value': 'borek fałęcki'},
    {'label': 'Swoszowice', 'value': 'swoszowice'},                                                    
    {'label': 'Podgórze Duchackie', 'value': 'podgórze duchackie'},                          
    {'label': 'Bieżanów', 'value': 'bieżanów'},
    {'label': 'Prokocim', 'value': 'prokocim'},             
    {'label': 'Podgórze', 'value': 'podgórze'},                                       
    {'label': 'Czyżyny', 'value': 'czyżyny'},                          
    {'label': 'Mistrzejowice', 'value': 'mistrzejowice'},                          
    {'label': 'Bieńczyce', 'value': 'bieńczyce'},                                       
    {'label': 'Wzgórza Krzesławickie', 'value': 'wzgórza krzesławickie'},                                       
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
area_marks = {i: str(i) for i in range(20, 125, 5)}
area_slider = dcc.Slider(id='area-slider', min=20, max=120, 
                         step=5, value=70, marks=area_marks)

room_marks = {i: str(i) for i in range(1, 7)}
room_slider = dcc.Slider(id='room-slider', min=1, max=6, 
                         step=1, value=2, marks=room_marks)

bathroom_marks = {i: str(i) for i in range(1, 6)}
bathroom_slider = dcc.Slider(id='bathroom-slider', min=1, max=5,
                             step=1, value=1, marks=bathroom_marks)

# Categorical dropdowns
district_drop = dcc.Dropdown(id='district-dropdown', 
                             options=district_opts, 
                             value='stare miasto')

propterty_drop = dcc.Dropdown(id='property-dropdown', 
                              options=property_opts, 
                              value='flat')

seller_drop = dcc.Dropdown(id='seller-dropdown', 
                           options=seller_opts, 
                           value='realtor')

parking_drop = dcc.Dropdown(id='parking-dropdown', 
                            options=parking_opts, 
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

# Styles

slider_header_style = {'margin': '5px', 'text-align': 'left', 'width': '100%'}

slider_style = {'margin': '5px'}

form_header_style = {'margin': '10px'}

drop_style = {'margin': '10px'}

form_col_style = {'float': 'left', 
                  'width': '33%', 
                  'margin': '0'}

form_body_style = {'width': '100%', 
                   'margin': '0 auto', 
                   'text-align': 'left'}

title_style = {'width': '100%', 
               'text-align': 'justify'}

pred_style = {'width': '100%', 
              'margin': '0 auto', 
              'text-align': 'left'}

bottom_style = {'margin': '10px', 
                'float': 'left',
                'width' : '100%',
                'text-align': 'left'}  

body_style = {'width': '40%', 
              'height': '100%', 
              'margin': '0 auto'}                                 

# Divs - forms - sliders
area_div = html.Div(children=[html.Label('Area (meters squared):'), area_slider], 
                    style=slider_style)

room_div = html.Div(children=[html.Label('Rooms:'), room_slider], 
                    style=slider_style)

bathroom_div = html.Div(children=[html.Label('Bathrooms:'), bathroom_slider], 
                        style=slider_style)

form_sliders = [html.H5('Area & rooms', style=slider_header_style), area_div, room_div, bathroom_div]

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

floor_div = html.Div(children=[html.Label('Floor:'), floor_drop], 
                    style=drop_style)

land_div = html.Div(children=[html.Label('Land:'), land_drop], 
                    style=drop_style)

# Divs - layout - dropdowns, in order of appearance
title = [html.H2('How much will your new flat cost ?')]

# html.Div(id='prediction')

# Bottom
bottom_note = 'I created a model from scratch to predict flat prices in Cracow, Poland.'
bottom_note += ' The model was trained using approximately 3500 data points scraped in august and september 2020.'
bottom_note += ' On this website you can interact with the model and see how different factors impact the final price.'
bottom_note += ' For more information on how the model was developed checkout the repo in the link below.'

bottom = [dcc.Link('Github', href='https://github.com/besiobu/flats-in-cracow')]
        #   dcc.Link('Linkedin', href='https://github.com/besiobu/flats-in-cracow', style={'margin-left': '10px'})]

pred = [html.Div(children=[html.Div(children=[html.Div(children=[html.H5('Prediction'), html.Div(id='prediction')])], 
                                                       style={'float': 'left', 'width': '40%', 'height': '150px', 'margin': '5px', 'text-align': 'justify'}), 
                                              html.Div(children=[html.H5('About'), html.P(bottom_note, style={'height': '150px'})], 
                                                       style={'float': 'left', 'width': '55%', 'height': '150px', 'vertical-align': 'middle', 'margin': '5px', 'text-align': 'justify'})], 
                                    style={'margin': '0 auto', 'height': '200px', 'width': '100%'})
]

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



# Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

# Flask
server = app.server

app.title = 'Flats in Cracow'

app.layout = html.Div(children=[

    # Title
    html.Div(children=title, style=title_style),

    # Predictions
    html.Div(children=pred, style=pred_style),

    # Sliders
    html.Div(children=form_sliders, style=form_body_style),

    # # Dropdowns
    html.Div(children=[form_left, form_center, form_right], 
             style=form_body_style),

    # Footer
    html.Div(children=[html.Div(children=bottom, 
                                style=bottom_style)], 
             style=form_body_style)

    ], style=body_style)

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

    fig = go.Figure(go.Bar(y=names,
                           x=preds,
                           width=(0.5, 0.5, 0.5),
                           marker_color=['#ABE2FB', '#ABE2FB', '#3498DB'],
                           orientation='h'))

    fig.update_layout(
        template='plotly_white',        
        width=275,
        height=150,        
        margin=dict(l=10, r=10, t=5, b=5, pad=5),
        xaxis=dict(range=[1 * 10 ** 5, 2 * 10 ** 6]),
        xaxis_title=('PLN'),
        hoverlabel=dict(bgcolor='white', font_size=12, font_family='Segoe UI, sans-serif'),        
        font=dict(family="Segoe UI, sans-serif", size=12, color='#212529')
    )

    # Disable toolbar
    bar_chart = dcc.Graph(figure=fig,
                           config={'displayModeBar': False})

    return bar_chart

if __name__ == '__main__':
    app.run_server(debug=True)
