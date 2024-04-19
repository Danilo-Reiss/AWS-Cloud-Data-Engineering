-- A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) 
-- por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 

-- Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas 
-- na base de dados com status concluído.

-- As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser 
-- apresentado em ordem decrescente arredondado na segunda casa decimal.

select
	tbven.nmvdd as vendedor,
	tbsom.somatoria as valor_total_vendas,
	round(((tbsom.somatoria * tbven.perccomissao) / 100),2) as comissao
from (
	select 
		cdvdd, 
		sum(valor_total) as somatoria
	from (
		select 
			cdvdd, 
			qtd * vrunt as valor_total 
		from tbvendas 
		where status = 'Concluído')
		group by cdvdd) as tbsom
left join tbvendedor as tbven
	on tbsom.cdvdd = tbven.cdvdd
order by comissao desc