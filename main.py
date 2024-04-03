import numpy as np
import pandas as pd


# Calculando os pesos para cada framework dentro de cada critério
def calculate_weights(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    max_eigenvalue = np.max(eigenvalues)
    index_max_eigenvalue = np.argmax(eigenvalues)
    weights = eigenvectors[:, index_max_eigenvalue].real
    normalized_weights = weights / np.sum(weights)
    return {"normalized_weights": normalized_weights,
            "max_eigenvalue": max_eigenvalue}


A = pd.DataFrame({
    "performance": {
        "performance": 1,
        "popularidade": 5,
        "facilidade": 7
    },
    "popularidade": {
        "performance": 1/5,
        "popularidade": 1,
        "facilidade": 3
    },
    "facilidade": {
        "performance": 1/7,
        "popularidade": 1/3,
        "facilidade": 1
    },
})

# Calculando o vetor de pesos (auto vetor associado ao maior auto valor)
weights = calculate_weights(A)
criteria_normalized_weights = weights["normalized_weights"]
max_eigenvalue = weights["max_eigenvalue"]

# Calculando o índice de consistência (CI) e a razão de consistência (CR)
n = A.shape[0]
CI = (max_eigenvalue - n) / (n - 1)

# Valores aleatórios padrão para matrizes de ordem n=1..9
RI = [0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45]
CR = CI / RI[n-1]

print("Pesos normalizados | Índice de Consistência | Razão de Consistência")
print(criteria_normalized_weights, CI, CR)


# Matrizes de comparação para cada critério
performance_matrix = pd.DataFrame({
    "django": {
        "django": 1,
        "fastapi": 3,
        "flask": 1/3
    },
    "fastapi": {
        "django": 1/3,
        "fastapi": 1,
        "flask": 1/5
    },
    "flask": {
        "django": 3,
        "fastapi": 5,
        "flask": 1
    },

})

popularidade_matrix = pd.DataFrame({
    "django": {
        "django": 1,
        "fastapi": 1/7,
        "flask": 1/3
    },
    "fastapi": {
        "django": 7,
        "fastapi": 1,
        "flask": 3
    },
    "flask": {
        "django": 3,
        "fastapi": 1/3,
        "flask": 1
    },

})

facilidade_codigo_matrix = pd.DataFrame({
    "django": {
        "django": 1,
        "fastapi": 1/7,
        "flask": 1/5
    },
    "fastapi": {
        "django": 7,
        "fastapi": 1,
        "flask": 3
    },
    "flask": {
        "django": 5,
        "fastapi": 1/3,
        "flask": 1
    },

})
performance_weights = calculate_weights(
                        performance_matrix)['normalized_weights']
popularidade_weights = calculate_weights(
                        popularidade_matrix)['normalized_weights']
facilidade_codigo_weights = calculate_weights(
                        facilidade_codigo_matrix)['normalized_weights']

print(performance_weights, popularidade_weights, facilidade_codigo_weights)

pontuacao_global = np.array([
    performance_weights,
    popularidade_weights,
    facilidade_codigo_weights
]).T.dot(criteria_normalized_weights)

print(pontuacao_global)
