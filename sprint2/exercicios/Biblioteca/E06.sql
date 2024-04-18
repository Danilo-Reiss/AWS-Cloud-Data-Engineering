-- Apresente a query para listar o autor com maior número de livros publicados. 
-- O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

select
	autor.codautor,
	autor.nome,
	count(livro.publicacao) as quantidade_publicacoes	
from autor
left join livro
	on codautor = autor
group by autor.nome
order by quantidade_publicacoes desc
limit 1