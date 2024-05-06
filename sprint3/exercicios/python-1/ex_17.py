""" Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. 
Teste sua implementação com a lista abaixo
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] """


def div_list(lista):
    tamanho = len(lista)
    tam_parte = tamanho // 3

    if tamanho % 3 != 0:
        raise ValueError(
            "A lista não pode ser dividida em três partes iguais!")

    parte1 = lista[:tam_parte]
    parte2 = lista[tam_parte:tam_parte*2]
    parte3 = lista[tam_parte*2:]

    new_list = []
    new_list.append(parte1)
    new_list.append(parte2)
    new_list.append(parte3)

    string_lista = [str(item) for item in new_list]
    string_conc = ' '.join(string_lista)
    print(string_conc)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
lista1 = div_list(lista)
