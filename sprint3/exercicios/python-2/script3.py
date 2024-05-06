# Etapa 3 #################################################################################################

with open('actors.csv', 'r', encoding='utf-8') as arquivo:
    next(arquivo)
    dados = arquivo.readlines()

dados_tratados = dados[4]
dados_tratados = dados_tratados[:14] + dados_tratados[15:]
dados.pop(4)
dados.append(dados_tratados)

# Extração colunas "Actor" e "Average per Movie"
nomes = [values.strip().split(',')[0] for values in dados]
avg_pmovies = [float(values.strip().split(',')[3]) for values in dados]

# Criação de um dict com as duas listas anteriores seguindo o padrão 'nomes: avg_pmovies'
dicio = {key: value for key, value in zip(nomes, avg_pmovies)}
# Utilização da função max com a ordenação definida pelo max_valor e armazenamento em duas vars
max_nome, max_valor = max(dicio.items(), key=lambda item: item[1])

with open('etapa-3.txt', 'w', encoding='utf-8') as saida:
    print(f'O ator com a maior média de receita de bilheteria bruta por filme é o(a) {max_nome} com {max_valor} milhões de dólares', file=saida)
