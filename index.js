dcc.Dropdown(
    id='tipo-grafico',
    options=[
        {'label': 'Gráfico de Linhas', 'value': 'linha'},
        {'label': 'Gráfico de Barras', 'value': 'barras'},
    ],
    value='linha',  # Valor padrão
    style={'width': '50%', 'margin': 'auto'}
),
dcc.Graph(id='grafico-vendas-lucro'),