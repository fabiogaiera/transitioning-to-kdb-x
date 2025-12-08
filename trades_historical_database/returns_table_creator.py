import pandas as pd
import plotly.graph_objects as go


def create_table_returns(df):
    # Format return as string for display
    df['return_str'] = df['return'].apply(lambda x: f"{x:.2%}" if pd.notnull(x) else "")

    # Define conditional colors
    return_colors = [
        'green' if val >= 0 else 'red' if pd.notnull(val) else 'white'
        for val in df['return']
    ]

    # Build Plotly Table
    fig = go.Figure(data=[go.Table(

        header=dict(
            values=['date', 'close', 'return'],
            fill_color='lightgrey',
            align='center'
        ),

        cells=dict(

            values=[
                df.index.strftime('%Y-%m-%d'),
                df['close'],
                df['return_str']
            ],

            fill_color=[
                ['white'] * len(df),
                ['white'] * len(df),
                return_colors
            ],

            font=dict(color=[
                ['black'] * len(df),
                ['black'] * len(df),
                ['white'] * len(df)  # white font for green/red cells
            ]),

            align='center'

        )
    )])

    fig.update_layout(title='AAPL Daily Returns',
                      width=500,
                      height=650
                      )

    fig.show()
