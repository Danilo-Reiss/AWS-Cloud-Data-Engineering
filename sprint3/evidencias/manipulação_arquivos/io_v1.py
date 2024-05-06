#! python
arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()

for registro in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*registro.split(','))) # --> * vai separar os argumentos da list nas variáveis
