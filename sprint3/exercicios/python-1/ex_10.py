""" Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. 
Utilize a lista a seguir para testar sua função. ['abc', 'abc', 'abc', '123', 'abc', '123', '123'] """


def noDuplicate(lista):
    lista = set(lista)
    lista = list(lista)
    return lista


a = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
a = noDuplicate(a)

print(a)
