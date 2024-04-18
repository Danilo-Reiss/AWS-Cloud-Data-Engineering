-- Apresente a query para listar as 5 editoras com mais livros na biblioteca. 
-- O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. 
-- Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

select editora.nome,
	endereco.estado,
	endereco.cidade,
	count(livro.titulo) as quantidade
from livro
left join editora
	on editora = codeditora
left join endereco
	on endereco = codendereco
group by editora.nome
order by quantidade desc
limit 5
