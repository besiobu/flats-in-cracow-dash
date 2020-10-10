from collections import deque

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

from src.layout import *
from src.model import Model, generate_features

# Models
gbr = Model(name='gbr').load()
mlp = Model(name='mlp').load()
vote = Model(name='vote').load()

models = [gbr, mlp, vote]

# Store previous predictions
prev_prices = deque(maxlen=2)

# Dash app
meta_tags = {'name': 'viewport', 
             'content': 'width=device-width, initial-scale=1'}

app = dash.Dash(name=__name__, 
                external_stylesheets=[dbc.themes.FLATLY], 
                meta_tags=[meta_tags])

# Flask
server = app.server

app.title = 'Flats in Cracow'

app.layout = html.Div(children=[title_row,
                                middle_about_row,
                                middle_row,
                                form_sliders_row,
                                form_drops_row,
                                bottom_row])

# Callbacks
@app.callback(
    [dash.dependencies.Output('room-slider', component_property='min'),
     dash.dependencies.Output('room-slider', component_property='max')],
    [dash.dependencies.Input('area-slider', 'value')]
)
def update_rooms_slider(area):
    """

    Update rooms slider to sensible values.

    """

    return [1, min(int(area / 30) + 1, 6)]

@app.callback(
    [dash.dependencies.Output('bathroom-slider', component_property='min'),
     dash.dependencies.Output('bathroom-slider', component_property='max')],
    [dash.dependencies.Input('area-slider', 'value')]
)
def update_bathrooms_slider(area):
    """

    Update bathrooms slider to sensible values.

    """

    return [1, min(int(area / 40) + 1, 5)]    

@app.callback(
    dash.dependencies.Output('townhouse-dropdown', 'options'),
    [dash.dependencies.Input('block-dropdown', 'value')]
)
def update_townhouse_dropdown(block):
    """

    Limit townhouse to sensible values.

    Notes
    -----
    Townhouse and block should be mutually exclusive.

    """

    if block:
        opts = [{'label': 'No', 'value': 0}]        
    else:
        opts = [{'label': 'Yes', 'value': 1},
                {'label': 'No', 'value': 0}]        
    return opts

@app.callback(
    dash.dependencies.Output('block-dropdown', 'options'),
    [dash.dependencies.Input('townhouse-dropdown', 'value')]
)
def update_block_dropdown(block):
    """

    Limit esate to sensible values.

    Notes
    -----
    Townhouse and block should be mutually exclusive.

    """

    if block:
        opts = [{'label': 'No', 'value': 0}]        
    else:
        opts = [{'label': 'Yes', 'value': 1},
                {'label': 'No', 'value': 0}]        
    return opts

@app.callback(
    [   dash.dependencies.Output('prediction', 'children'),
        dash.dependencies.Output('pred-stats', 'children')
    ],
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
        dash.dependencies.Input('basement-dropdown', 'value'),
        dash.dependencies.Input('new-dropdown', 'value'),
        dash.dependencies.Input('block-dropdown', 'value'),
        dash.dependencies.Input('townhouse-dropdown', 'value'),
        dash.dependencies.Input('apartment-dropdown', 'value'),
        dash.dependencies.Input('busstop-dropdown', 'value'),                                
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

    stats = update_stats(preds, names, *args)

    return bar_chart, stats

def update_stats(preds, names, *args):
    """

    Get the prediction of the best model and calculate 
    price per square meter and difference in price from 
    the previous parameters.

    Notes
    -----
    Difference shows up after the user 
    changes the settings.

    """

    area = args[2]

    price = preds[names.index('vote')]

    prev_prices.append(price)

    price_per_m2 = int(round(price / area, -2))

    price_paragraph = html.P(f'Price: {price:,} PLN')

    price_per_m2_paragraph = html.P(f'Price per \u33A1: {price_per_m2:,} PLN')

    stats_children = [html.Div(children=[price_paragraph,
                                         price_per_m2_paragraph], 
                               style={'width': '100%', 'float': 'left'})]

    # If user changes settings calculate
    # difference and relative change
    if len(prev_prices) > 1:

        prev_price = prev_prices[-2]
        diff_pln = price - prev_price
        diff_pct = round((price / prev_price - 1) * 100, 2)        

        if diff_pln > 0:
            diff_text = html.P(f'{diff_pln:+,.0f} PLN ({diff_pct:+.2f}%)' , 
                               style={'color': 'green'})
        elif diff_pln < 0:
            diff_text = html.P(f'{diff_pln:+,.0f} PLN ({diff_pct:+.2f}%)', 
                               style={'color': 'red'})
        else:
            diff_text = html.P(f'{diff_pln:+,.0f} PLN ({diff_pct:+.2f}%)')

        diff_tooltip = f'Change in price from previous parameters.'

        stats_children += [html.Div(children=[html.P(children=f'Difference: ', 
                                                     id='tooltip-difference', 
                                                     style={'cursor': 'pointer', 
                                                            'float': 'left'}), 
                                              dbc.Tooltip(children=diff_tooltip, 
                                                          target='tooltip-difference'),
                                              html.Div(children=html.P(diff_text), 
                                                       style={'float': 'left', 
                                                              'margin-left': '5px'})])] 

    stats = html.Div(children=stats_children, style={'width': '100%'})

    return stats

def make_bar_chart(preds, names):
    """

    Draw horizontal bar char with model predictions.

    Notes
    -----
    Last predicton is plotted in darker colour.

    """

    names = [x.upper() for x in names]

    names = [x for x,_ in sorted(zip(names, preds), key=lambda pair: pair[1])]
    preds = [y for _,y in sorted(zip(names, preds), key=lambda pair: pair[1])]

    colours = ['#ABE2FB' if x != 'VOTE' else '#3498DB' for x in names]

    fig = go.Figure(go.Bar(y=names,
                           x=preds,
                           width=(0.5, 0.5, 0.5),
                           marker_color=colours,
                           orientation='h'))

    fig.update_layout(template='plotly_white',        
                      height=150,        
                      margin=dict(l=10, r=10, t=5, b=5, pad=5),
                      yaxis_title=('MODEL'),
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
