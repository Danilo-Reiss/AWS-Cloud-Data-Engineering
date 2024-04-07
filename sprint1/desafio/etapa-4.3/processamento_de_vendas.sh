#!/bin/bash

########################################################
#
# processamento_de_vendas.sh - Script de gerenciamento, processamento e geração de relatórios
# 
# Autor: Danilo Souza Reis (danilo.reis.pb@compasso.com.br)
# Data de criação: 05/04/2024
#
# Descrição: Script que cria e gerencia diretórios/arquivos, processa dados de um arquivo de vendas e gera relatórios a cada execução
#
# Exemplo de uso: ./processamento_de_vendas.sh
#
#########################################################

# Gerenciamento de diretórios/arquivos
mkdir vendas ; cp dados_de_vendas.csv vendas
mkdir vendas/backup ; cp dados_de_vendas.csv vendas/backup/dados-"$(date +%Y%m%d)".csv
cd vendas/backup ; mv dados-* backup-dados-"$(date +%Y%m%d)".csv

# Geração de relatório
echo '===============RELATÓRIO=================' > relatorio.txt
echo -n 'Data de execução: ' >> relatorio.txt
date +"%Y/%m/%d %H:%M" >> relatorio.txt
echo -n 'Data primeira venda: ' >> relatorio.txt
head -2 backup-dados-* |tail -1 |cut -d "," -f 5 >> relatorio.txt
echo -n 'Data última venda: ' >> relatorio.txt
tail -1 backup-dados-* |cut -d "," -f 5 >> relatorio.txt
echo -n 'Número de itens diferentes vendidos: ' >> relatorio.txt
tail -n +2 backup-dados-* |cut -d "," -f 2 |sort |uniq |wc -l >> relatorio.txt
echo 'Lista dos 9 primeiros itens vendidos:' >> relatorio.txt
head -n 10 backup-dados-* >> relatorio.txt
echo ' ' >> relatorio.txt
zip -r backup-dados"$(date +%Y%m%d)" *.csv
rm -r *.csv ; cd .. ; rm dados_de_vendas.csv ; cd ..

## Estrutura para possibilitar execução sequenciais
# Estrutura condicional para geração de um contador
if [ ! -f contador.txt ]; then
	echo 0 > contador.txt
fi

# Atribuição de variável numérica no nome do diretório pai
contador=$(<contador.txt)
((contador++))
echo $contador > contador.txt
mv vendas vendas$contador
