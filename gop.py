from turtle import color
import dash    
import plotly.express as px                         
import dash_core_components as dcc
from dash.dependencies import Output, Input
from dash_extensions import Lottie       
import dash_bootstrap_components as dbc  
import pandas as pd                     
from datetime import date
import dash_html_components as html
url_like= "https://assets8.lottiefiles.com/datafiles/KZAksH53JBd6PNu/data.json" 
url_comment = "https://assets7.lottiefiles.com/packages/lf20_dO9smc.json"
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

df1 = pd.read_csv('feeds_comments.csv')
df2 = pd.read_csv('feeds_likes.csv')
output1 = pd.concat([df1, df2])
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
 
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardImg(src='/assets/Ulektz-logo.png') # 150px by 45px
            ],className='mb-2'),
            dbc.Card([
                dbc.CardBody([
                    dbc.CardLink("ulektz Data", target="_blank")
                ])
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.DatePickerSingle(
                        id='my-date-picker-start',
                        date=date(2022,5,19),
                        className='ml-5'
                    ),
                    dcc.DatePickerSingle(
                        id='my-date-picker-end',
                        date=date(2022,5,25),
                        className='mb-2 ml-2'
                    ),
                ])
            ], color="Green", style={'height':'18vh'}),
        ], width=8),
    ],className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="67%", height="67%",url=url_like)),
                dbc.CardBody([
                    html.H6('likes'),
                    html.H2(id='liked_by', children="000")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="67%", height="67%",url=url_comment)),
                dbc.CardBody([
                    html.H6('comment'),
                    html.H2(id='comment', children="000")
                ], style={'textAlign': 'center'})
            ]),
        ], width=2),
    ],className='mb-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='line-chart', figure={}, config={'displayModeBar': False}),
                ])
            ]),
        ], width=6),
    ],className='mb-2')
], fluid=True)

@app.callback(
    Output('liked_by','children'),
    Output('comment','children'),
    Input('my-date-picker-start','date'),
    Input('my-date-picker-end','date'),
)
def getuser(start_date, end_date):
    dff_c = output1.copy()
    dff_c = dff_c[(dff_c['created_on']>=start_date) & (dff_c['created_on']<=end_date)]
    compns_num = len(dff_c['liked_by'].unique())

    dff_r = output1.copy()
    dff_c = dff_c[(dff_c['created_on']>=start_date) & (dff_c['created_on']<=end_date)]
    react = len(dff_r['comment'].unique())

    return compns_num,react

@app.callback(
    Output('line-chart','figure'),
    Input('my-date-picker-start','date'),
    Input('my-date-picker-end','date'),
)
def update_line(start_date, end_date):
    dff = output1.copy()
    dff = dff[(dff['created_on']>=start_date) & (dff['created_on']<=end_date)]
    dff = dff[["liked_by"]].value_counts()
    dff = dff.to_frame()
    dff.reset_index(inplace=True)
    dff.rename(columns={0: 'Total likes'}, inplace=True)

    fig_line = px.line(dff, x='liked_by', y='Total likes', template='ggplot2',
                  title="Total registration")
    fig_line.update_traces(mode="lines+markers", fill='tozeroy',line={'color':'green'})
    fig_line.update_layout(margin=dict(l=20, r=20, t=30, b=20))

    return fig_line


if __name__=='__main__':
    app.run_server(debug=False, host='0.0.0.0')
