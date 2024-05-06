""" Escreva um código Python que use a função range() para adicionar três números em uma lista(Esta lista deve chamar-se 'números')  
e verificar se esses três números são pares ou ímpares. Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente 
(uma linha para cada número lido). Importante: Aplique a função range() em seu código. """

# Script aceito pela Udemy
numeros = []
novo_numero = 5
for i in range(1, 4):
    novo_numero += i
    numeros.append(novo_numero)

for numero in numeros:
    if numero % 2 == 0:
        print(f'Par: {numero}')
    else:
        print(f'Ímpar: {numero}')


# Script com input:
""" 
numeros = []
for i in range(1, 4):
    novo_numero = int(input(f'Digite o {i}º número: '))
    numeros.append(novo_numero)

par = []
impar = []

for numero in numeros:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f'Par: {par} \nÍmpar: {impar}') """
