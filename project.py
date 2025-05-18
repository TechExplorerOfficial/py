@app.callback(
    Output('grafico-vendas-lucro', 'figure'),
    [Input('tipo-grafico', 'value')]
    )
    def atualizar_grafico(tipo_grafico):
    if tipo_grafico == 'linha':
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Data'], y=df['Vendas'], name='Vendas'))
    fig.add_trace(go.Scatter(x=df['Data'], y=df['Lucro'], name='Lucro'))
    fig.update_layout(title='Vendas e Lucro ao Longo do Tempo',
    xaxis_title='Data',
    yaxis_title='Valor')
    elif tipo_grafico == 'barras':
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df['Data'], y=df['Vendas'], name='Vendas'))
    fig.add_trace(go.Bar(x=df['Data'], y=df['Lucro'], name='Lucro'))
    fig.update_layout(title='Vendas e Lucro Mensais',
    xaxis_title='Data',
    yaxis_title='Valor')
    return fig