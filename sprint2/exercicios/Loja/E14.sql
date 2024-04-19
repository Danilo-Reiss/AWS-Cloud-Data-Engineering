-- Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser 
-- estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de 
-- forma decrescente. Observação: Apenas vendas com status concluído.

SELECT 
	estado,
	round((avg(vl_gasto)),2) as gastomedio
from (
	select 
		estado,
		qtd * vrunt as vl_gasto 
	from tbvendas 
	where status = 'Concluído')
group by estado
order by gastomedio desc