""" Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. 
Depois imprima a soma dos valores. A string deve ter valor  "1,3,4,6,10,76" """


def funct(*args):
    lista_num = [int(num) for num in args[0].split(',')]
    print(sum(lista_num))


funct("1,3,4,6,10,76")
