-- Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto 
-- em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.
-- Observação: Apenas vendas com status concluído.

SELECT 
	tabdep.cddep,
	tabdep.nmdep,
	tabdep.dtnasc,
	tabcalc.valor_total_vendas
from(
	select
		cdvdd,
		sum(valor) as valor_total_vendas
	from(
		select 
			cdvdd, 
			qtd * vrunt as valor 
		from tbvendas 
		where status = 'Concluído')
	group by cdvdd
	order by valor_total_vendas
	limit 1) as tabcalc
left join tbdependente as tabdep
	on tabcalc.cdvdd = tabdep.cdvdd