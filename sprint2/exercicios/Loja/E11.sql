-- Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado 
-- devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.

select 
	cdcli,
	nmcli,
	sum (vl_gasto) as gasto
from (
	select 
		nmcli, 
		cdcli, 
		qtd * vrunt as vl_gasto 
	from tbvendas 
	where status = 'Concluído')
group by cdcli
order by gasto desc
limit 1