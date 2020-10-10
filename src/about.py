import dash_html_components as html

from src.links import *
from src.styles import *

# Information about the page
about_text_p1 = 'On this site you can find out how much that' \
                ' flat you are thinking about buying should cost.' \
                ' The models were trained using approximately' \
                ' 4500 listings for flats in '

about_text_p2 = '. Feel free to interact with the models and' \
                ' see how different factors impact the final price.' \
                ' For more information on how the models were ' \
                ' developed checkout the projects repo.'

about_div = html.Div(children=[html.H4('About'), 
                               html.Div(children=[about_text_p1, 
                                                  google_maps_link, 
                                                  about_text_p2])], 
                     style=about_style)                