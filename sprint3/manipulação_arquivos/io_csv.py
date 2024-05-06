import csv

with open('pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada): # --> csv.reader já faz todo os tratamentos dos dados
        print('Nome: {}, Idade: {}'.format(*pessoa))