-- EXERCÍCIOS ########################################################################

-- (Exercício 1) Identifique quais as marcas de veículo mais visitada na tabela sales.funnel
select pro.brand,
	count (visit_page_date) as visitas
from sales.products as pro
left join sales.funnel as fun
	on pro.product_id = fun.product_id
group by pro.brand
order by visitas desc

select 
	pro.brand,
	count(visit_page_date) as visitas
from sales.funnel as fun
full join sales.products as pro
	on fun.product_id = pro.product_id
group by pro.brand
order by visitas desc

-- (Exercício 2) Identifique quais as lojas de veículo mais visitadas na tabela sales.funnel
select sto.store_name,
	count(visit_page_date) as visitas
from sales.stores as sto
full join sales.funnel as fun
	on sto.store_id = fun.store_id
group by sto.store_name
order by visitas desc


-- (Exercício 3) Identifique quantos clientes moram em cada tamanho de cidade (o porte da cidade
-- consta na coluna "size" da tabela temp_tables.regions)
select reg.size,
	count(cus.cpf) as quant
from temp_tables.regions as reg
left join sales.customers as cus
	on lower(reg.state) = lower(cus.state)
	and lower(reg.city) = lower(cus.city)
group by reg.size
order by quant

select
	reg.size,
	count(cus.cpf) as contagem
from sales.customers as cus
left join temp_tables.regions as reg
	on lower(cus.city) = lower(reg.city)
	and lower(cus.state) = lower(reg.state)
group by reg.size
order by contagem