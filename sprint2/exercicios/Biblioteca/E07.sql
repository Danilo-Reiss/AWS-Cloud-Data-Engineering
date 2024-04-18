-- Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.

select autor.nome
from autor
left join livro
	on codautor = autor
where livro.titulo is NULL 