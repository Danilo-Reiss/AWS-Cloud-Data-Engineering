#! python
with open('pessoas.csv') as arquivo: # --> Fecha automaticamente!
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo já foi fechado!')

