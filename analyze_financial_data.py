import json
import pandas as pd
import matplotlib.pyplot as plt
import os

def analyze_and_plot(data_file='extracted_data.json'):
    """
    Lê os dados financeiros de um arquivo JSON, cria DataFrames do pandas
    e gera gráficos de Receita Líquida, EBITDA e Margem EBITDA.
    """
    try:
        with open(data_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Erro: O arquivo {data_file} não foi encontrado.")
        return
    except json.JSONDecodeError:
        print(f"Erro: Não foi possível decodificar o JSON do arquivo {data_file}.")
        return

    # Dados de Projeções
    projections = data.get('projections', {})
    df_projections = pd.DataFrame({
        'Ano': projections.get('years', []),
        'Receita Líquida': projections.get('receita_liquida', []),
        'EBITDA': projections.get('ebitda', []),
        'Margem EBITDA': projections.get('margem_ebitda', [])
    })
    df_projections = df_projections.set_index('Ano')

    # Criar diretório para salvar os gráficos, se não existir
    output_dir = 'plots'
    os.makedirs(output_dir, exist_ok=True)

    # Gráfico de Receita Líquida e EBITDA
    plt.figure(figsize=(12, 6))
    plt.bar(df_projections.index, df_projections['Receita Líquida'], width=0.4, label='Receita Líquida', align='center')
    plt.bar(df_projections.index, df_projections['EBITDA'], width=0.4, label='EBITDA', align='edge')
    plt.xlabel('Ano')
    plt.ylabel('Valor (R$ milhões)')
    plt.title('Receita Líquida e EBITDA (2021-2030E)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'receita_ebitda_bar_chart.png'))
    plt.close()
    print(f"Gráfico 'receita_ebitda_bar_chart.png' salvo em {output_dir}/")

    # Gráfico de Margem EBITDA
    plt.figure(figsize=(12, 6))
    plt.plot(df_projections.index, df_projections['Margem EBITDA'], marker='o', linestyle='-', color='green', label='Margem EBITDA (%)')
    plt.xlabel('Ano')
    plt.ylabel('Margem EBITDA (%)')
    plt.title('Margem EBITDA (2021-2030E)')
    plt.xticks(rotation=45)
    plt.yticks(fontsize=8)
    plt.legend()
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'margem_ebitda_line_chart.png'))
    plt.close()
    print(f"Gráfico 'margem_ebitda_line_chart.png' salvo em {output_dir}/")

    print("Análise e geração de gráficos concluídas.")

if __name__ == '__main__':
    analyze_and_plot()
