from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier

def treino_KNN(X_train_scaled, y_train, X_test_scaled, y_test, valores):
    lista_KNN = []
    if valores.__len__() > 0:
        for k in valores:
            print(f"\nTreinando o algoritmo KNN (Mapeando distâncias {k})")
            knn = KNeighborsClassifier(n_neighbors=k, metric='euclidean')  # Você pode mudar para 'manhattan' se quiser
            knn.fit(X_train_scaled, y_train)

            # Fazer Previsões
            predict_knn = knn.predict(X_test_scaled)

            # Avaliação Numérica
            print("\nRelatório de Classificação (Churn): 0 / 1:")
            print(classification_report(y_test, predict_knn))
            
            # Armazenar os resultados para análise posterior
            lista_KNN.append({
                'k': k,
                'classification_report': classification_report(y_test, predict_knn),
                'classification_report_dict': classification_report(y_test, predict_knn, output_dict=True),
                'y_pred': predict_knn
            })
        return lista_KNN
    else:
        return print("A lista de valores de k está vazia. Por favor, forneça uma lista válida de valores de k para treinar o modelo KNN.")

def comparar_resultados_KNN(lista_KNN_scaled, lista_KNN_scaled_smoted):
    for resultado1, resultado2 in zip(lista_KNN_scaled, lista_KNN_scaled_smoted):

        print(f"K = {resultado1['k']:<3} {'SCALED':-^50} { 'SMOTED':-^50}")

        for linha1, linha2 in zip(
            resultado1['classification_report'].splitlines(),
            resultado2['classification_report'].splitlines()
        ):
            print(f"{linha1:<60} {linha2}")

        print("-" * 120)

def treino_DecisionTree(X_train, y_train, X_test, y_test, depth):
    lista_tree = []
    if depth.__len__() > 0:
        for i in depth:
            print(f"\nTreinando o algoritmo Decision Tree (Profundidade {i})")
            tree = DecisionTreeClassifier(
                max_depth=i,
                random_state=42,
                min_samples_leaf = 5,
                min_samples_split = 10,
                criterion='gini' 
            )

            tree.fit(X_train, y_train)

            predict_tree = tree.predict(X_test)

            # Avaliação
            print("\nRelatório de Churn: 0 / 1:")
            print(classification_report(y_test, predict_tree))

            lista_tree.append({
                'max_depth': i,
                'model': tree,
                'classification_report': classification_report(y_test, predict_tree),
                'y_pred': predict_tree
            })
        return lista_tree
    else:
        return print("A lista de profundidades está vazia. Por favor, forneça uma lista válida de profundidades para treinar o modelo Decision Tree.")
    
def comparar_resultados_KNN_DECISIONTREE(lista_KNN_scaled, lista_tree):
    for resultado1, resultado2 in zip(lista_KNN_scaled, lista_tree):
        if resultado2['max_depth'] == None:
            depth = 'ilimitada'
        else:
            depth = resultado2['max_depth']
        print(f"K = {resultado1['k']:<3} {'KNN_SCALED':-^50} { 'DECISION_TREE':-^50} Depth = {depth}")

        for linha1, linha2 in zip(
            resultado1['classification_report'].splitlines(),
            resultado2['classification_report'].splitlines()
        ):
            print(f"{linha1:<60} {linha2}")

        print("-" * 120)
