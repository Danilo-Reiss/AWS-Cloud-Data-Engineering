""" Dada as listas a seguir:
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]
Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".
Exemplo:
0 - João Soares está com 19 anos """

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

primeirosNomes = list(enumerate(primeirosNomes))
sobreNomes = list(enumerate(sobreNomes))
idades = list(enumerate(idades))

for i in primeirosNomes:
    for i_2 in sobreNomes:
        for i_3 in idades:
            if i[0] == i_2[0] == i_3[0]:
                print(f'{i[0]} - {i[1]} {i_2[1]} está com {i_3[1]} anos')
