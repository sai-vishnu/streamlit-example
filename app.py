from dash import Dash, html
import pandas as pd

df = pd.read_csv('users.csv', low_memory=False)


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app = Dash(__name__)

app.layout = html.Div([
    html.H4(children='Users details'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)