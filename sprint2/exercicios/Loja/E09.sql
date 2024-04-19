-- Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02,
-- e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.

select 
	cdpro,
	nmpro
from tbvendas
where dtven BETWEEN '2014-02-03' and '2018-02-02' and status = 'Concluído'
group by cdpro
order by count(*)desc
limit 1