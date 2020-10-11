import dash_html_components as html

from src.links import *
from src.styles import *

# Information about the page
about_text_p1 = 'On this site you can find out how much that' \
                ' flat you are thinking about buying should cost.' \
                ' The models were trained using nearly' \
                ' 4500 listings for flats in '

about_text_p2 = '. Feel free to interact with the models and' \
                ' see how different factors impact the final price.' \
                ' For a overview of the districts in Kraków, Poland see '

about_text_p3 = ". For more information about the project see it's "

about_text_p4 = '.'

about_div = html.Div(children=[html.H4('About'), 
                               html.Div(children=[about_text_p1, 
                                                  google_maps_link, 
                                                  about_text_p2,
                                                  district_link,
                                                  about_text_p3,
                                                  github_link,
                                                  about_text_p4])], 
                     style=about_style)                