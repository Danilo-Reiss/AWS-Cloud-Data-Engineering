#!/bin/bash
#
################################################
# 
# consolidador_de_processamento_de_vendas = Script para consolidação de relatórios
# 
# Autor: Danilo Souza Reis (danilo.reis.pb@compasso.com.br)
# Data de criação: 06/04/2024
#
# Descrição: Script para redirecionar todos os relatórios e gerar um relatório final
#
# Exemplo de uso: ./consolidador_de_processamento_de_vendas 
#
#################################################

cat vendas*/backup/relatorio.txt > relatorio.txt
