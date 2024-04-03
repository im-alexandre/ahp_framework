import numpy as np

# Tempos de resposta médios (em ms)
tempos_resposta = np.array([120, 100, 80])

# Invertendo os valores para que menor tempo de resposta signifique maior valor
valores_invertidos = 1 / tempos_resposta

# Normalizando os valores invertidos
valores_normalizados = valores_invertidos / np.sum(valores_invertidos)

# Matriz de julgamentos ponderada anterior e pontuação global de cada framework
matriz_ponderada_ponderada_total = np.array([0.49783599, 0.37292508, 0.12923893
                                             ])

# Supondo que o novo critério "Tempo de Resposta Médio" tenha um peso, vamos
# definir arbitrariamente para este exemplo
# Como temos agora um critério adicional, vamos recalibrar os pesos dos
# critérios
# Adicionando peso 1 para simplificação
pesos_critérios_atualizados = np.array([0.73830738, 0.17017232, 0.0915203, 1])
pesos_critérios_normalizados = pesos_critérios_atualizados / np.sum(
    pesos_critérios_atualizados)

# Ajustando a contribuição do novo critério para a pontuação global de
# cada framework
contribuicao_novo_criterio = valores_normalizados * \
    pesos_critérios_normalizados[-1]

# Somando as contribuições do novo critério às pontuações globais anteriores
# para atualizar a pontuação
pontuação_global_atualizada = matriz_ponderada_ponderada_total + \
    contribuicao_novo_criterio

print(pontuação_global_atualizada, valores_normalizados)
