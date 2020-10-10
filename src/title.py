import dash_html_components as html

from src.styles import title_style

text = 'How much will your new flat cost ?'

title = html.Div(children=[html.H1(children=text)],
                 style=title_style)