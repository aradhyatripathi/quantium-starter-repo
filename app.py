import dash
from dash import dcc, html, Input, Output
import pandas as pd

df = pd.read_csv('data/daily_sales_data.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser",
            style={
                'textAlign': 'center',
                'color': '#2c3e50',
                'fontFamily': 'Arial',
                'padding': '20px',
                'backgroundColor': '#f8f9fa',
                'marginBottom': '0'
            }),
    html.Div([
        html.Label("Filter by Region:",
                   style={'fontFamily': 'Arial', 'fontWeight': 'bold', 'marginRight': '10px'}),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
            ],
            value='all',
            inline=True,
            style={'fontFamily': 'Arial'}
        )
    ], style={
        'textAlign': 'center',
        'padding': '15px',
        'backgroundColor': '#f8f9fa',
        'borderBottom': '2px solid #dee2e6'
    }),
    dcc.Graph(id='sales-chart')
], style={'backgroundColor': '#ffffff', 'maxWidth': '1200px', 'margin': '0 auto'})

@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(region):
    if region == 'all':
        filtered = df
    else:
        filtered = df[df['region'] == region]

    df_grouped = filtered.groupby('date')['sales'].sum().reset_index()

    return {
        'data': [{
            'x': df_grouped['date'],
            'y': df_grouped['sales'],
            'type': 'line',
            'name': 'Sales',
            'line': {'color': '#e74c3c', 'width': 2}
        }],
        'layout': {
            'title': f'Pink Morsel Sales Over Time ({region.title()})',
            'xaxis': {'title': 'Date'},
            'yaxis': {'title': 'Sales ($)'},
            'plot_bgcolor': '#f8f9fa',
            'paper_bgcolor': '#ffffff'
        }
    }

if __name__ == '__main__':
    app.run(debug=True)