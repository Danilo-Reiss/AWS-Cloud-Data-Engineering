-- EXERCÍCIOS ########################################################################

-- (Exercício 1) Crie uma coluna calculada com o número de visitas realizadas por cada
-- cliente da tabela sales.customers
with contagem_visitas as(
	select
		customer_id,
		count(*) as n_visit
	from sales.funnel
	group by customer_id
)
select
	fun.customer_id,
	count(con.n_visit) as contagem
from sales.funnel as fun
left join contagem_visitas as con
	on fun.customer_id = con.customer_id
group by fun.customer_id
order by contagem desc

