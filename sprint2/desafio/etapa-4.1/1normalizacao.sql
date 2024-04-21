-- Etapa 4.1 - Normalização dos dados

-- Criação das tabelas
CREATE table tb_cliente ( 
	idCliente int primary key not null unique,
	nomeCliente varchar(100),
	cidadeCliente varchar(40),
	estadoCliente varchar(40),
	paisCliente varchar(40)
)
CREATE table tb_carro(
	idCarro int primary key not null unique,
	classiCarro varchar(50),
	marcaCarro varchar(80),
	modeloCarro varchar(80),
	anoCarro int
)
CREATE table tb_combustivel (
	idcombustivel int primary key not null unique,
	tipoCombustivel varchar(20)
)
CREATE table tb_vendedor (
	idVendedor int primary key not null unique,
	nomeVendedor varchar(15),
	sexoVendedor smallint,
	estadoVendedor varchar(40)
)

-- Inserção de dados
insert into tb_cliente (idCliente,nomeCliente,cidadeCliente,estadoCliente,paisCliente)
select DISTINCT  
	idCliente,
	nomeCliente,
	cidadeCliente,
	estadoCliente,
	paisCliente
from tb_locacao 
order by idCliente
--
insert into tb_carro (idCarro,classiCarro,marcaCarro,modeloCarro,anoCarro)
select DISTINCT 
	idCarro,
	classiCarro,
	marcaCarro,
	modeloCarro,
	anoCarro
from tb_locacao 
order by idCarro
--
insert into tb_combustivel (idcombustivel, tipoCombustivel)
select DISTINCT 
	idcombustivel,
	tipoCombustivel
from tb_locacao
order by idcombustivel
--
insert into tb_vendedor (idVendedor,nomeVendedor,sexoVendedor,estadoVendedor)
select DISTINCT 
	idVendedor,
	nomeVendedor,
	sexoVendedor,
	estadoVendedor
from tb_locacao
order by idVendedor 

-- Remoção das colunas em tb_locacao
alter table tb_locacao drop column nomeCliente 
alter table tb_locacao drop column cidadeCliente
alter table tb_locacao drop column estadoCliente
alter table tb_locacao drop column paisCliente
alter table tb_locacao drop column classiCarro
alter table tb_locacao drop column marcaCarro
alter table tb_locacao drop column modeloCarro
alter table tb_locacao drop column anoCarro
alter table tb_locacao drop column tipoCombustivel
alter table tb_locacao drop column nomeVendedor
alter table tb_locacao drop column sexoVendedor
alter table tb_locacao drop column estadoVendedor

-- Criação das chaves estrangeiras
PRAGMA foreign_keys = ON
alter table tb_locacao rename to tb_locaca
create table tb_locacao (
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
	FOREIGN KEY (idCliente) references tb_cliente(idCliente)
	FOREIGN KEY (idCarro) references tb_carro(idCarro)
	FOREIGN KEY (idcombustivel) references tb_combustivel(idcombustivel)
	FOREIGN KEY (idVendedor) references tb_vendedor(idVendedor)
)
 insert into tb_locacao (idLocacao,idCliente,idCarro,kmCarro,idcombustivel,dataLocacao,horaLocacao,qtdDiaria,vlrDiaria,dataEntrega,horaEntrega,idVendedor)
 select * from tb_locaca
 drop table tb_locaca
 
 -- Tratamento das datas
update tb_locacao
set dataLocacao = (substr(dataLocacao, 1, 4) || '-' || substr(dataLocacao, 5, 2) || '-' || substr(dataLocacao, 7, 2)),
	dataEntrega = (substr(dataEntrega, 1, 4) || '-' || substr(dataEntrega, 5, 2) || '-' || substr(dataEntrega, 7, 2))

