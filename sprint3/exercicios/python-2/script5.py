with open('actors.csv', 'r', encoding='utf-8') as arquivo:
    next(arquivo)
    dados = arquivo.readlines()

dados_tratados = dados[4]
dados_tratados = dados_tratados[:14] + dados_tratados[15:]
dados.pop(4)
dados.append(dados_tratados)

nomes = [values.strip().split(',')[0] for values in dados]
receita_bruta = [values.strip().split(',')[1] for values in dados]

dicio = {key: value for key,value in zip(nomes, receita_bruta)}

lista_ord = sorted(dicio.items(), key=lambda x: x[1], reverse=True)
lista_ord = dict(lista_ord)

with open('etapa-5.txt', 'w', encoding='utf-8') as saida:
    for nome, receita in lista_ord.items():
        print(f'{nome} - {receita}', file=saida)
