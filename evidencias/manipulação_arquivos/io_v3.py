#! python
arquivo = open('pessoas.csv')
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(','))) # --> strip retira os espaços em branco ao redor
arquivo.close()

