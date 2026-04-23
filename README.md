# Análise Financeira da ENEVA S.A. - Galapagos Challenge

Este repositório contém um script Python para analisar e visualizar dados financeiros da ENEVA S.A., com base nas informações extraídas do Google Sites "Galapagos Challenge" e do PDF "AGK_Inicial.pdf".

## Conteúdo do Repositório

*   `extracted_data.json`: Arquivo JSON contendo os dados financeiros extraídos do PDF e do Google Sites.
*   `analyze_financial_data.py`: Script Python que lê os dados do `extracted_data.json` e gera gráficos de Receita Líquida, EBITDA e Margem EBITDA.
*   `plots/`: Diretório onde os gráficos gerados pelo script Python são salvos.
    *   `receita_ebitda_bar_chart.png`: Gráfico de barras mostrando a Receita Líquida e o EBITDA ao longo do tempo.
    *   `margem_ebitda_line_chart.png`: Gráfico de linha mostrando a Margem EBITDA ao longo do tempo.
*   `requirements.txt`: Lista das bibliotecas Python necessárias para executar o script.

## Como Usar

Para replicar a análise e gerar os gráficos, siga os passos abaixo:

1.  **Clone o Repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd <nome_do_seu_repositorio>
    ```

2.  **Crie um Ambiente Virtual (Opcional, mas Recomendado):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o Script Python:**
    ```bash
    python3 analyze_financial_data.py
    ```

    Após a execução, os gráficos serão salvos no diretório `plots/`.

## Dados Analisados

Os dados foram extraídos das projeções financeiras da ENEVA S.A. para o período de 2021 a 2030, incluindo:

*   **Receita Líquida**
*   **EBITDA**
*   **Margem EBITDA**
*   **Métricas de Valuation** (Enterprise Value, Dívida Líquida, Equity Value, Preço-Alvo Implícito)
*   **Componentes do WACC** (Custo de Capital Médio Ponderado)

## Contribuição

Sinta-se à vontade para explorar, modificar e melhorar este projeto. Sugestões e pull requests são bem-vindos!
