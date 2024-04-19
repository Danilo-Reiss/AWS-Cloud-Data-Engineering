-- Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou 
-- Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser 
-- cdpro, nmcanalvendas, nmpro e quantidade_vendas.

select
	cdpro,
	nmcanalvendas,
	nmpro,
	sum(qtd) as quantidade_vendas
from (
	SELECT 
		cdpro,
		nmcanalvendas,
		nmpro,
		qtd
	from tbvendas
	where status = 'Concluído' and nmcanalvendas = 'Ecommerce' )
group by cdpro

union all

select
	cdpro,
	nmcanalvendas,
	nmpro,
	sum(qtd) as quantidade_vendas
from (
	SELECT 
		cdpro,
		qtd,
		nmcanalvendas,
		nmpro
	from tbvendas
	where status = 'Concluído' and nmcanalvendas = 'Matriz' )
group by cdpro
order by quantidade_vendas