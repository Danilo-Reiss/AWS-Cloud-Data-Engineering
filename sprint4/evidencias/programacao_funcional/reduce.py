#! python
from functools import reduce

pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17},
]

so_idades = map(lambda p: p['idade'], pessoas) # --> retorna apenas a 'idade' de 'pessoas'
menores = filter(lambda idade: idade < 18, so_idades) # --> retorna apenas a 'idade' menor que 18

# Reduce recebe como parâmetro uma função onde o primeiro parâm. é o acumulador e o segundo
# o item percorrido da lista. O terceiro parâm. da função reduce é o valor inicial do acumulador (0)
soma_idades = reduce(lambda idades, idade: idades + idade, menores, 0) 
print(soma_idades)