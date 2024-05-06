# Etapa 4 #################################################################################################

with open('actors.csv', 'r', encoding='utf-8') as arquivo:
    next(arquivo)
    dados = arquivo.readlines()

dados_tratados = dados[4]
dados_tratados = dados_tratados[:14] + dados_tratados[15:]
dados.pop(4)
dados.append(dados_tratados)

# Extração coluna "Average Per Movie"
top1_filmes = [values.strip().split(',')[4] for values in dados]

# Método para contar ocorrências e armazenar em uma dict
cont_filmes = {}

for filmes in top1_filmes:
    if filmes in cont_filmes:
        cont_filmes[filmes] += 1
    else:
        cont_filmes[filmes] = 1

# Lista ordenada em: 1º maior ocorrência e 2º nome do filme, de forma decrescente
lista_ord = sorted(cont_filmes.items(), key=lambda x: (x[1], x[0]), reverse=True)
lista_ord = dict(lista_ord)

with open('etapa-4.txt', 'w', encoding='utf-8') as saida:
    for filmes, contador in lista_ord.items():
        print(f'O filme {filmes} aparece {contador} vez(es) no dataset', file=saida)