import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import random

# --- 1. Simulação de Conexão de Dados ---
class DataSource:
    def __init__(self, name):
        self.name = name

    def fetch_data(self, start_date, end_date):
        # Simula a busca de dados de uma fonte (e.g., um banco de dados, um arquivo CSV)
        num_days = (end_date - start_date).days
        data = {
            'date': [start_date + timedelta(days=i) for i in range(num_days + 1)],
            'impressions': np.random.randint(100, 1000, size=num_days + 1),
            'clicks': np.random.randint(10, 100, size=num_days + 1),
            'spend': np.random.uniform(10, 50, size=num_days + 1),
            'region': [random.choice(['North', 'South', 'East', 'West']) for _ in range(num_days + 1)],
            'product': [random.choice(['A', 'B', 'C']) for _ in range(num_days + 1)]
        }
        return pd.DataFrame(data)

# --- 2. Simulação de Transformação de Dados (Power Query) ---
def transform_data(df):
    # Calcula métricas derivadas
    df['ctr'] = df['clicks'] / df['impressions']
    df['cpc'] = df['spend'] / df['clicks']
    df['roas'] = (df['clicks'] * 2) / df['spend'] # Simulação de receita por clique
    return df

# --- 3. Simulação de Criação de Visualizações (Power BI) ---
def create_visualizations(df):
    plt.figure(figsize=(12, 6))

    # Gráfico de Linha: Impressões e Cliques ao longo do tempo
    plt.subplot(1, 2, 1)
    plt.plot(df['date'], df['impressions'], label='Impressions')
    plt.plot(df['date'], df['clicks'], label='Clicks')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.title('Impressions vs Clicks Over Time')
    plt.legend()
    plt.grid(True)

    # Gráfico de Dispersão: Gasto vs ROAS
    plt.subplot(1, 2, 2)
    sns.scatterplot(x='spend', y='roas', data=df)
    plt.xlabel('Spend')
    plt.ylabel('ROAS')
    plt.title('Spend vs Return on Ad Spend (ROAS)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

    # Gráfico de Barras: Gasto por Região
    region_spend = df.groupby('region')['spend'].sum().sort_values(ascending=False)
    plt.figure(figsize=(8, 5))
    region_spend.plot(kind='bar', color='skyblue')
    plt.title('Total Spend by Region')
    plt.xlabel('Region')
    plt.ylabel('Total Spend')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

    # Tabela de Métricas Agregadas
    print("\n--- Métricas Agregadas ---")
    print(df[['impressions', 'clicks', 'spend', 'ctr', 'cpc', 'roas']].sum())

# --- 4. Simulação de Serviço Power BI (Orquestração) ---
class PowerBIServiceSimulator:
    def __init__(self):
        self.data_sources = {}
        print("Serviço Power BI Simulado iniciado.")

    def connect_data_source(self, name):
        data_source = DataSource(name)
        self.data_sources[name] = data_source
        print(f"Fonte de dados '{name}' conectada.")
        return data_source

    def refresh_data(self, source_name, start_date, end_date):
        if source_name in self.data_sources:
            print(f"Atualizando dados da fonte '{source_name}'...")
            return self.data_sources[source_name].fetch_data(start_date, end_date)
        else:
            print(f"Erro: Fonte de dados '{source_name}' não encontrada.")
            return None

    def build_report(self, df):
        if df is not None and not df.empty:
            print("Construindo relatório...")
            transformed_df = transform_data(df.copy())
            create_visualizations(transformed_df)
            print("Relatório construído e visualizações exibidas.")
        else:
            print("Erro: Nenhum dado disponível para construir o relatório.")

# --- Execução da Simulação ---
if __name__ == "__main__":
    power_bi_service = PowerBIServiceSimulator()

    # Conectar a uma fonte de dados simulada
    ad_data_source = power_bi_service.connect_data_source("MarketingAds")

    # Definir o período de dados a ser analisado
    start_date = datetime(2025, 5, 1)
    end_date = datetime(2025, 5, 10)

    # Simular a atualização dos dados
    data = power_bi_service.refresh_data("MarketingAds", start_date, end_date)

    # Construir o relatório e exibir as visualizações
    power_bi_service.build_report(data)

    print("\nSimulação do Serviço Power BI concluída.")