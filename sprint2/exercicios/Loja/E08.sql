-- Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), 
-- e que estas vendas estejam com o status concluída.  
-- As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

select 
	tbven.cdvdd,
	tbvdd.nmvdd
from tbvendas as tbven
left join tbvendedor as tbvdd
	on tbven.cdvdd = tbvdd.cdvdd
where tbven.status = 'Concluído'
group by tbven.cdvdd
order by count (*) desc
limit 1