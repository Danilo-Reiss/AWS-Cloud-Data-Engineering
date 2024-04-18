-- Apresente a query para listar a quantidade de livros publicada por cada autor. 
-- Ordenar as linhas pela coluna nome (autor), em ordem crescente. 
-- Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).

select
	autor.nome,
	autor.codautor,
	autor.nascimento,
	count(livro.titulo) as quantidade
from autor
left join livro
	on codAutor = autor
group by autor.nome 
order by autor.nome
