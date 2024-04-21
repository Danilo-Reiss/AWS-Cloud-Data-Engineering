-- 4.2 - Transformação modelo relacional para modelo dimensional

-- Criação de views p/ referência
CREATE VIEW view_dim_cliente AS
SELECT * FROM tb_cliente tc 
--
CREATE VIEW view_dim_carro AS
SELECT * FROM tb_carro tc
--
CREATE VIEW view_dim_combustivel AS
SELECT * FROM tb_combustivel tc 
--
CREATE VIEW view_dim_combustivel AS
SELECT * FROM tb_combustivel tc 
--
CREATE VIEW view_dim_vendedor AS 
select * FROM tb_vendedor tv 
--
CREATE VIEW view_fato_locacao AS
SELECT * FROM tb_locacao tl 
--
CREATE VIEW view_dim_dataLocacao AS
SELECT DISTINCT
	dataLocacao,
	strftime('%Y', dataLocacao), 
 	strftime('%m', dataLocacao),
	strftime('%d', dataLocacao), 
	strftime('%w', dataLocacao)
FROM tb_locacao tl
--
CREATE VIEW view_dim_dataEntrega AS
SELECT DISTINCT
	dataEntrega,
	strftime('%Y', dataEntrega), 
 	strftime('%m', dataEntrega),
	strftime('%d', dataEntrega), 
	strftime('%w', dataEntrega)
FROM tb_locacao tl
DROP VIEW view_dim_carro
DROP VIEW view_dim_cliente
DROP VIEW view_dim_combustivel 
DROP VIEW view_dim_dataEntrega
DROP VIEW view_dim_dataLocacao 
DROP VIEW view_dim_vendedor
DROP VIEW view_fato_locacao

-- Criação das dimensões
ALTER TABLE tb_carro RENAME TO dim_carro
ALTER TABLE tb_cliente  RENAME TO dim_cliente
ALTER TABLE tb_combustivel RENAME TO dim_combustivel
ALTER TABLE tb_vendedor  RENAME TO dim_vendedor
CREATE TABLE dim_dataLocacao (
	dataCompleta datetime PRIMARY KEY NOT NULL,
	ano date,
	mes date,
	dia date,
	dow date
)
CREATE TABLE dim_dataEntrega (
	dataCompleta datetime PRIMARY KEY NOT NULL,
	ano date,
	mes date,
	dia date,
	dow date
)

-- Inserção de dados nas dimensões de data
INSERT INTO dim_dataLocacao (dataCompleta,ano,mes,dia,dow)
SELECT DISTINCT
	dataLocacao,
	strftime('%Y', dataLocacao), 
 	strftime('%m', dataLocacao),
	strftime('%d', dataLocacao), 
	strftime('%w', dataLocacao)
FROM tb_locacao 
--
INSERT INTO dim_dataEntrega (dataCompleta,ano,mes,dia,dow)
SELECT DISTINCT
	dataEntrega,
	strftime('%Y', dataEntrega), 
 	strftime('%m', dataEntrega),
	strftime('%d', dataEntrega), 
	strftime('%w', dataEntrega)
FROM tb_locacao 

-- Criação da fato
PRAGMA foreign_keys = ON
create table fato_locacao (
	idLocacao int primary key not null unique,
	idCliente int not null,
	idCarro int not null,
	kmCarro int default null,
	idcombustivel int not null,
	dataLocacao datetime,
	horaLocacao time,
	qtdDiaria int default null,
	vlrDiaria decimal (18,2) default null,
	dataEntrega datetime,
	horaEntrega time,
	idVendedor int not null,
	FOREIGN KEY (idCliente) references dim_cliente(idCliente)
	FOREIGN KEY (idCarro) references dim_carro(idCarro)
	FOREIGN KEY (idcombustivel) references dim_combustivel(idcombustivel)
	FOREIGN KEY (dataLocacao) REFERENCES dim_dataLocacao (dataCompleta)
	FOREIGN KEY (dataEntrega) REFERENCES dim_dataEntrega (dataCompleta)
	FOREIGN KEY (idVendedor) references dim_vendedor(idVendedor)
)
insert into fato_locacao (idLocacao,idCliente,idCarro,kmCarro,idcombustivel,dataLocacao,horaLocacao,qtdDiaria,vlrDiaria,dataEntrega,horaEntrega,idVendedor)
select * from tb_locacao
DROP TABLE tb_locacao