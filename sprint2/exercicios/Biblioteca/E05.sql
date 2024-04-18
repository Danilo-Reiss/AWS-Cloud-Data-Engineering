-- Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. 
-- Ordene o resultado pela coluna nome, em ordem crescente. 
-- Não podem haver nomes repetidos em seu retorno.

select DISTINCT autor.nome
from autor 
left join livro
	on codautor = autor 
left join editora
	on editora = codeditora
left join endereco
	on endereco = codendereco
where endereco.estado <> 'PARANÁ' AND endereco.estado <> 'RIO GRANDE DO SUL'
order by autor.nome