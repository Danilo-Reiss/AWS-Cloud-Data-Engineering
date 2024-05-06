# Etapa 1 #################################################################################################

with open('actors.csv', 'r', encoding='utf-8') as arquivo:
    next(arquivo)  # Lê apenas a partir da segunda linha
    dados = arquivo.readlines()

# Trata o erro de posicionamento da vírgula na linha 6
dados_tratados = dados[4]
dados_tratados = dados_tratados[:14] + dados_tratados[15:]

# Remove a linha com erro e acrescenta a linha tratada
dados.pop(4)
dados.append(dados_tratados)

# Lista com todos os valores da coluna "Actor" e da coluna "Number of movies"
nomes = [values.strip().split(',')[0] for values in dados]
num_movies = [int(values.strip().split(',')[2]) for values in dados]

# Criação de um dict com as duas listas anteriores seguindo o padrão 'nomes: num_movies'
dicio = {key: value for key, value in zip(nomes, num_movies)}
# Acessa o maior valor através da ordenação da função lambda no arg key e armazena o par em duas vars
max_chave, max_valor = max(dicio.items(), key=lambda item: item[1])


# Redirecionamento
with open('etapa-1.txt', 'w', encoding='utf-8') as saida:
    print(f'O ator com o maior número de filmes participados é o(a) {max_chave} com {max_valor} filmes', file=saida)
