""" Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada:
Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!
Use as variáveis abaixo para representar cada operação matemática:
mediana, media, valor_minimo , valor_maximo 
Importante: Esperamos que você utilize as funções abaixo em seu código: random, max, min, sum """

import random


def calc_mediana(lista):
    lista_ordenada = sorted(lista)
    tamanho = len(lista)

    if tamanho % 2 != 0:
        mediana = lista_ordenada[tamanho // 2]
    else:
        metade_sup = tamanho // 2
        metade_inf = metade_sup - 1
        mediana = (lista_ordenada[metade_sup] + lista_ordenada[metade_inf]) / 2

    return mediana


random_list = random.sample(range(500), 50)

mediana = calc_mediana(random_list)
media = sum(random_list) / len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')
