import plotly.graph_objects as go


def create_candlestick_chart(df):
    fig = go.Figure(data=[
        go.Candlestick(
            x=df.index,
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close'],
            showlegend=False,
            increasing=dict(line=dict(color='green')),
            decreasing=dict(line=dict(color='red'))
        )
    ])
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.show()
