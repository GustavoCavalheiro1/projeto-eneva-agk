import json
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

def load_data(data_file='extracted_data.json'):
    """
    Carrega os dados financeiros de um arquivo JSON.
    """
    try:
        with open(data_file, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Erro: O arquivo {data_file} não foi encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Erro: Não foi possível decodificar o JSON do arquivo {data_file}.")
        return None

def process_projections(projections_data):
    """
    Processa os dados de projeções em um DataFrame do pandas.
    """
    df_projections = pd.DataFrame({
        'Ano': projections_data.get('years', []),
        'Receita Líquida': projections_data.get('receita_liquida', []),
        'EBITDA': projections_data.get('ebitda', []),
        'Margem EBITDA': projections_data.get('margem_ebitda', [])
    })
    df_projections = df_projections.set_index('Ano')
    return df_projections

def plot_revenue_ebitda(df_projections, output_dir='plots'):
    """
    Gera o gráfico de barras de Receita Líquida e EBITDA com estilo corporativo.
    """
    fig, ax1 = plt.subplots(figsize=(14, 7))

    # Cores corporativas
    color_revenue = '#1f77b4'  # Azul
    color_ebitda = '#ff7f0e'   # Laranja

    # Gráfico de barras para Receita Líquida
    ax1.bar(df_projections.index, df_projections['Receita Líquida'], color=color_revenue, width=0.6, label='Receita Líquida')
    ax1.set_xlabel('Ano Fiscal', fontsize=12)
    ax1.set_ylabel('Receita Líquida (R$ Milhões)', color=color_revenue, fontsize=12)
    ax1.tick_params(axis='y', labelcolor=color_revenue)
    ax1.set_ylim(0, df_projections['Receita Líquida'].max() * 1.2)

    # Adicionar rótulos de dados
    for i, v in enumerate(df_projections['Receita Líquida']):
        ax1.text(i, v + (df_projections['Receita Líquida'].max() * 0.02), f'{v:,.0f}', color=color_revenue, ha='center', fontsize=9)

    # Criar um segundo eixo Y para EBITDA
    ax2 = ax1.twinx()
    ax2.plot(df_projections.index, df_projections['EBITDA'], color=color_ebitda, marker='o', linestyle='-', linewidth=2, label='EBITDA')
    ax2.set_ylabel('EBITDA (R$ Milhões)', color=color_ebitda, fontsize=12)
    ax2.tick_params(axis='y', labelcolor=color_ebitda)
    ax2.set_ylim(0, df_projections['EBITDA'].max() * 1.5)

    # Adicionar rótulos de dados para EBITDA
    for i, v in enumerate(df_projections['EBITDA']):
        ax2.text(i, v + (df_projections['EBITDA'].max() * 0.05), f'{v:,.0f}', color=color_ebitda, ha='center', fontsize=9)

    # Título e layout
    plt.title('Receita Líquida e EBITDA da ENEVA S.A. (2021-2030E)', fontsize=14, fontweight='bold')
    fig.tight_layout()
    fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
    ax1.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, ha='right')

    filepath = os.path.join(output_dir, 'revenue_ebitda_corporate_chart.png')
    plt.savefig(filepath)
    plt.close()
    print(f"Gráfico '{os.path.basename(filepath)}' salvo em {output_dir}/")

def plot_ebitda_margin(df_projections, output_dir='plots'):
    """
    Gera o gráfico de linha da Margem EBITDA com estilo corporativo.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(df_projections.index, df_projections['Margem EBITDA'], color='#2ca02c', marker='s', linestyle='-', linewidth=2, markersize=6, label='Margem EBITDA (%)') # Verde corporativo
    plt.xlabel('Ano Fiscal', fontsize=12)
    plt.ylabel('Margem EBITDA (%)', fontsize=12)
    plt.title('Margem EBITDA da ENEVA S.A. (2021-2030E)', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.yticks(fontsize=10)
    plt.legend(loc='upper left')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.ylim(df_projections['Margem EBITDA'].min() * 0.8, df_projections['Margem EBITDA'].max() * 1.2)

    # Adicionar rótulos de dados
    for i, v in enumerate(df_projections['Margem EBITDA']):
        plt.text(i, v + (df_projections['Margem EBITDA'].max() * 0.02), f'{v:.1f}%', color='#2ca02c', ha='center', fontsize=9)

    plt.tight_layout()
    filepath = os.path.join(output_dir, 'ebitda_margin_corporate_chart.png')
    plt.savefig(filepath)
    plt.close()
    print(f"Gráfico '{os.path.basename(filepath)}' salvo em {output_dir}/")

def main():
    output_dir = 'plots'
    os.makedirs(output_dir, exist_ok=True)

    data = load_data()
    if data is None:
        return

    # Processar Projeções
    projections_data = data.get('projections', {})
    df_projections = process_projections(projections_data)

    if not df_projections.empty:
        plot_revenue_ebitda(df_projections, output_dir)
        plot_ebitda_margin(df_projections, output_dir)
    else:
        print("Nenhum dado de projeção encontrado para plotagem.")

    print("Análise e geração de gráficos concluídas com estilo corporativo.")

if __name__ == '__main__':
    main()
