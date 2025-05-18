</codeblock>

Este código cria um dashboard interativo com um dropdown para alternar entre um gráfico de linhas e um gráfico de barras, mostrando a evolução de vendas e lucro ao longo do tempo.

#### b. Streamlit

* **Streamlit:** Framework para criar aplicativos de dados de forma rápida.

<codeblock>
```python
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Crie dados de exemplo
data = {'Data': pd.date_range(start='2023-01-01', end='2023-12-31', freq='M'),
        'Vendas': [120, 150, 180, 200, 220, 250, 230, 210, 240, 260, 280, 300],
        'Lucro': [30, 40, 50, 55, 60, 70, 65, 60, 75, 80, 85, 90]}
df = pd.DataFrame(data)

# Defina o título do aplicativo
st.title("Dashboard de Vendas e Lucro")

# Selecione o tipo de gráfico
tipo_grafico = st.selectbox("Selecione o tipo de gráfico:", ["Gráfico de Linhas", "Gráfico de Barras"])

# Crie o gráfico com base na seleção
if tipo_grafico == "Gráfico de Linhas":
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Data'], y=df['Vendas'], name='Vendas'))
    fig.add_trace(go.Scatter(x=df['Data'], y=df['Lucro'], name='Lucro'))
    fig.update_layout(title='Vendas e Lucro ao Longo do Tempo',
                      xaxis_title='Data',
                      yaxis_title='Valor')
elif tipo_grafico == "Gráfico de Barras":
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df['Data'], y=df['Vendas'], name='Vendas'))
    fig.add_trace(go.Bar(x=df['Data'], y=df['Lucro'], name='Lucro'))
    fig.update_layout(title='Vendas e Lucro Mensais',
                      xaxis_title='Data',
                      yaxis_title='Valor')

# Exiba o gráfico
st.plotly_chart(fig)