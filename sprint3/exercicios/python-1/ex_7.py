""" Dada a seguinte lista: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Faça um programa que gere uma nova lista contendo apenas números ímpares. """

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lista_impar = []

for n_impar in a:
    if n_impar % 2 != 0:
        lista_impar.append(n_impar)

print(f'{lista_impar}')