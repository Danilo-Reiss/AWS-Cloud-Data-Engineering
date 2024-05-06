# Etapa 2 #################################################################################################

with open('actors.csv', 'r', encoding='utf-8') as arquivo:
    next(arquivo)
    dados = arquivo.readlines()

dados_tratados = dados[4]
dados_tratados = dados_tratados[:14] + dados_tratados[15:]
dados.pop(4)
dados.append(dados_tratados)

# Extração coluna "Gross"
dados = [float(values.strip().split(',')[-1]) for values in dados]
media = sum(dados) // len(dados)

with open('etapa-2.txt', 'w', encoding='utf-8') as saida:
    print(f'A média da receita de bilheteria bruta dos principais filmes dos atores é de aproximadamente {media} milhões de doláres', file=saida)