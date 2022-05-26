import dash    
import plotly.express as px                         
import dash_core_components as dcc
from dash.dependencies import Output, Input
from dash_extensions import Lottie       
import dash_bootstrap_components as dbc  
import pandas as pd                     
from datetime import date, datetime
import dash_html_components as html 

url_reg_out = "https://assets6.lottiefiles.com/private_files/lf30_4nows39l.json"
url_reg_in = "https://assets5.lottiefiles.com/private_files/lf30_t58qlnnx.json"
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))
df_cnt = pd.read_csv('users.csv', low_memory=False)
df_cnt["created_date"] = pd.to_datetime(df_cnt["created_date"])

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
                        date=date(2018, 1, 1),
                        className='ml-5'
                    ),
                    dcc.DatePickerSingle(
                        id='my-date-picker-end',
                        date=date(2021, 4, 4),
                        className='mb-2 ml-2'
                    ),
                ])
            ], color="Green", style={'height':'18vh'}),
        ], width=8),
    ],className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="87%", height="87%",url=url_reg_in)),
                dbc.CardBody([
                    html.H6('registered'),
                    html.H2(id='content-reg', children="000")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="67%", height="67%",url=url_reg_out)),
                dbc.CardBody([
                    html.H6('not-reg'),
                    html.H2(id='content-reg-in', children="000")
                ], style={'textAlign':'center'})
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
    ],className='mb-2'),
], fluid=True)

@app.callback(
    Output('content-reg','children'),
    Output('content-reg-in','children'),
    Input('my-date-picker-start','date'),
    Input('my-date-picker-end','date'),
)
def getuser(start_date, end_date):

    # Invitations
    dff_i = df_cnt.copy()
    dff_i = dff_i[(dff_i['created_date']>=start_date) & (dff_i['created_date']<=end_date)]
    # print(dff_i)
    in_num = len(dff_i[dff_i['register_status']=='1'])
    out_num = len(dff_i[dff_i['register_status']=='0'])

    return in_num, out_num

@app.callback(
    Output('line-chart','figure'),
    Input('my-date-picker-start','date'),
    Input('my-date-picker-end','date'),
)
def update_line(start_date, end_date):
    dff = df_cnt.copy()
    dff = dff[(dff['created_date']>=start_date) & (dff['created_date']<=end_date)]
    dff = dff[["register_status"]].value_counts()
    dff = dff.to_frame()
    dff.reset_index(inplace=True)
    dff.rename(columns={0: 'Total registration'}, inplace=True)

    fig_line = px.line(dff, x='register_status', y='Total registration', template='ggplot2',
                  title="Total registration")
    fig_line.update_traces(mode="lines+markers", fill='tozeroy',line={'color':'green'})
    fig_line.update_layout(margin=dict(l=20, r=20, t=30, b=20))

    return fig_line



if __name__=='__main__':
    app.run_server(debug=False)
