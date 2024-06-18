## 2. Lab AWS Athena  
**Etapa 1 - Configurar *AWS Athena*:**  
<img src="../evidencias/lab-aws-athena/local-consulta.png" alt="print">

**Etapa 2 - Criar um banco de dados:**  
<img src="../evidencias/lab-aws-athena/criando-db.png" alt="print">

**Etapa 3 - Criar uma tabela:**  
* Criando tabela:  
<img src="../evidencias/lab-aws-athena/criando-tabela.png" alt="print">

* Realizando *query* de teste:  
<img src="../evidencias/lab-aws-athena/consulta1.png" alt="print">

* *Script* da *query* que lista os 3 nomes mais usados em cada década desde 1950 até hoje:  
<img src="../evidencias/lab-aws-athena/consulta2.png" alt="print">

* *Output* da *query* anterior:  
<img src="../evidencias/lab-aws-athena/resultado-consulta2.png" alt="print">

* **Script para conferência:**  
```SQL
WITH nomes_com_decada AS (
    SELECT
        nome,
        sexo,
        total,
        ano,
        (CAST(ano / 10 AS INTEGER) * 10) AS decada
    FROM
        meubanco.nomes
    WHERE
        ano >= 1950
),
nomes_ordenados AS (
    SELECT
        nome,
        sexo,
        total,
        ano,
        decada,
        ROW_NUMBER() OVER (PARTITION BY decada ORDER BY total DESC) AS rn
    FROM
        nomes_com_decada
)
SELECT
    decada,
    nome,
    total
FROM
    nomes_ordenados
WHERE
    rn <= 3
ORDER BY
    decada,
    rn
```
  