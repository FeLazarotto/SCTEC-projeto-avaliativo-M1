#   Análise Preditiva de Churn em E-commerce

### Projeto desenvolvido para o Módulo 1 do programa SCTEC, com foco em Análise Exploratória de Dados (EDA) e Machine Learning para previsão de evasão (Churn) de clientes de uma plataforma de e-commerce.

## 1. Objetivo

### O objetivo deste projeto é identificar clientes com maior probabilidade de cancelar seu relacionamento com a empresa (Churn), utilizando técnicas de Ciência de Dados e Machine Learning.

    Para isso foram realizadas as seguintes etapas:

    Limpeza e tratamento dos dados;
    Análise Exploratória (EDA);
    Engenharia de atributos;
    Seleção de Features;
    Balanceamento das classes utilizando SMOTE;
    Treinamento e comparação de modelos de Machine Learning.

## 2. Dataset

### O conjunto de dados contém informações comportamentais de clientes de um e-commerce, incluindo características como:

    Tempo de permanência (Tenure)
    Número de pedidos
    Cashback recebido
    Reclamações
    Tempo desde o último pedido
    Utilização de cupons
    Satisfação do cliente
    Entre outras variáveis.
    
### Variável alvo

    Churn
    0 → Cliente permanece
    1 → Cliente cancelou
    🛠 Tecnologias Utilizadas
    Python
    Pandas
    NumPy
    Matplotlib
    Seaborn
    Scikit-Learn
    Imbalanced-Learn (SMOTE)
    Jupyter Notebook

## 3. Etapas do Projeto

###     3.1. Análise Exploratória (EDA)
        Foram analisadas diversas relações entre as variáveis para compreender o comportamento dos clientes.

        Exemplos:
        Distribuição da variável Churn
        Correlação entre atributos
        Análise por gênero
        Tempo de permanência
        Cashback

###     3.2. Tratamento dos dados
        Remoção de inconsistências
        Tratamento de valores ausentes
        Tratamento de Outliers

###     3.3. Engenharia de Features

        Foi criada uma nova variável CashBackByOrder que representa o cashback médio recebido por pedido:
        CashBackByOrder = CashbackAmount / OrderCount
    
###     3.4. Separação, Balanceamento e Escalonamento Seguro

        Encoding
        Balanceamento de Classes
        Escalonamento Seguro

###     3.5. Modelagem e Validação 

        Otimização do KNN com o parâmetro n_neighbors (K) testado com 5 valores distintos.
        Otimização da Árvore com o parâmetro max_depth testado com 5 valores distintos.
        Diagnóstico de Overfitting escolhendo com base nos dados o modelo que melhor responde o problema.

        Foram comparados dois algoritmos:

        - K-Nearest Neighbors (KNN)
            StandardScaler
            Testes com diferentes valores de K
            Avaliação utilizando métricas de classificação

        - Decision Tree
            Critério Gini
            Diferentes profundidades (max_depth)
            Comparação de desempenho


###     3.6. Avaliação e Veredito de Negócios

        Visualização do relatório Classification Report e Matriz de Confusão
        A escolha do modelo priorizou a redução de falsos negativos, uma vez que classificar um cliente que irá abandonar a plataforma como não churn pode gerar maior impacto financeiro para o negócio.


## 4. Estrutura do Projeto
```
    SCTEC-projeto-avaliativo-M1
    │
    ├── dataset/
    │       └── E Commerce Dataset.xlsx - E Comm.csv
    │
    ├── SCTEC-projeto-avaliativo-M1.ipynb
    ├── funcoes.py
    └── README.md
```


## 5. Como executar

    git clone https://github.com/FeLazarotto/SCTEC-projeto-avaliativo-M1.git

    cd SCTEC-projeto-avaliativo-M1

    pip install -r requirements.txt

    Abra o notebook principal utilizando Jupyter Notebook ou VS Code.
    
## 6. Aprendizados

    Durante o desenvolvimento deste projeto foi possível aplicar conceitos de:

    Limpeza e preparação de dados
    Visualização de dados
    Engenharia de atributos
    Seleção de Features
    Balanceamento de classes
    Machine Learning supervisionado
    Avaliação de modelos

## Autor

    Felipe Jacques Lazarotto

    GitHub: https://github.com/FeLazarotto
    LinkedIn: https://www.linkedin.com/in/felazarotto