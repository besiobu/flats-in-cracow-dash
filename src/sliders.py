import dash_core_components as dcc

# Numeric sliders
area_marks = {i: str(i) for i in list(range(20, 130, 10))}

area_slider = dcc.Slider(id='area-slider', 
                         min=20, 
                         max=120, 
                         step=5, 
                         value=70, 
                         marks=area_marks, 
                         included=False)

room_marks = {i: str(i) for i in range(1, 7)}

room_slider = dcc.Slider(id='room-slider', 
                         min=1, 
                         max=6, 
                         step=1, 
                         value=2, 
                         marks=room_marks,
                         included=False)

bathroom_marks = {i: str(i) for i in range(1, 6)}

bathroom_slider = dcc.Slider(id='bathroom-slider', 
                             min=1, 
                             max=5,
                             step=1, 
                             value=1, 
                             marks=bathroom_marks,
                             included=False)