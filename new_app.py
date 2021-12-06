import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output


colors = {"background": "#E5ECF6", "text": "#636EFA"}

data = pd.read_csv('Iris.csv')

p=px.scatter(data, x="PetalWidthCm", y="PetalLengthCm", color="Species",size='SepalLengthCm', hover_data=['SepalWidthCm'])
app = dash.Dash(__name__)

app.title = 'Iris Dataset Visulalization'

app.layout = html.Div([
    html.Div([
        html.Div([
            html.H1("Iris Dataset Visulalization", className='title'),
            html.H2("Select type of Iris"),
            dcc.Dropdown(
                id='iris_dropdown',
                options=[
                    {'label': 'Iris-setosa', 'value': 'Iris-setosa'},
                    {'label': 'Iris-versicolor', 'value': 'Iris-versicolor'},
                    {'label': 'Iris-virginica', 'value': 'Iris-virginica'},
                    
                ],
                value='Iris-setosa',
                style={'width': "60%"},
                className='dropdown-list'
            )
        ],
            className='text-display'),
        html.Div([
            dcc.Graph(id="iris-scatterplot",
                      
                      config={
                          'scrollZoom': True,
                          'doubleClick': 'reset',
                      }
                      ),
            
        ],
            className='graph-display'),
        
        
    ],
        className='app',
    ),
    
    html.Div([
            dcc.Graph(id="irispetal-scatterplot",
                      figure=p,
                      style={'background-color': colors['background']},
                      config={
                          'scrollZoom': True,
                          'doubleClick': 'reset',
                      }
                      ),
            
        ],
            className='graphily-display'), 
    
    html.Div([
        html.Label("Created by Chinmay Pant(101903597)", className='footer')
    ])
])



@app.callback(
    Output('iris-scatterplot', 'figure'),
    [
        Input('iris_dropdown', 'value'),
        
    ]
)
def update_figure(cl_selected):
    
    data = pd.read_csv('Iris.csv')

    data = data[data['Species']== cl_selected]

    fig = px.scatter(
        data,
        title=f'{cl_selected} Sepal Length vs sepal Width',
        x='SepalLengthCm',
        y='SepalWidthCm',
        color="Species",
        hover_data=['PetalWidthCm']
    )
    fig.update_layout(
        paper_bgcolor=colors["background"],
        font_color=colors["text"]
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=False)
