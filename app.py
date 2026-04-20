import dash
from dash import dcc, html
import pandas as pd

# Load data
df = pd.read_csv('data/daily_sales_data.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Group by date for total sales
df_total = df.groupby('date')['sales'].sum().reset_index()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser",
            style={'textAlign': 'center'}),
    dcc.Graph(
        id='sales-chart',
        figure={
            'data': [{
                'x': df_total['date'],
                'y': df_total['sales'],
                'type': 'line',
                'name': 'Sales'
            }],
            'layout': {
                'title': 'Pink Morsel Sales Over Time',
                'xaxis': {'title': 'Date'},
                'yaxis': {'title': 'Sales ($)'}
            }
        }
    )
])

if __name__ == '__main__':
    app.run(debug=True)