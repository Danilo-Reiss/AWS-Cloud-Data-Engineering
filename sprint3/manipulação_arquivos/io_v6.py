#! python
with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida: # --> Modo de escrita
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida) # --> Redireciona o print p/ a saída indicada

if arquivo.closed:
    print('Arquivo já foi fechado!')

if saida.closed:
    print('Arquivo de saída já foi fechado!')

