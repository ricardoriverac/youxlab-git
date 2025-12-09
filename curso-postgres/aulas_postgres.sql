create table cliente (
	idcliente integer not null,
	nome varchar(50) not null, -- Pedro
	cpf char(11),
	rg varchar(15),
	data_nascimento date,
	genero char(1),
	profissao varchar(30),
	nacionalidade varchar(30),
	logradouro varchar(30),
	numero varchar(10),
	complemento varchar(30),
	bairro varchar(30),
	municipio varchar(30),
	uf varchar(30),
	observacoes text,

	-- primary key
	constraint pk_cln_idcliente primary key (idcliente)
);

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (1, 'Manoel', '88828383821', '32323', '2001-01-30', 'M', 'Estudante', 'Brasileira', 'Rua joaquim Nabuco', '23', 'Casa', 'Cidade Nova', 'Porto União', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (2, 'Geraldo', '12343299929', '56565', '1987-01-04', 'M', 'Engenheiro', 'Brasileira', 'Rua das Limas', '200', 'Ap', 'Centro', 'Porto União', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (3, 'Carlos', '87732323227', '55463', '1967-01-10', 'M', 'Pedreiro', 'Brasileira', 'Rua das Laranjeiras', '300', 'Ap', 'Centro', 'Porto Vitória', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (4, 'Adriana', '12321222122', '98777', '1989-09-10', 'F', 'Jornalista', 'Brasileira', 'Rua das Limas', '240', 'Casa', 'São Pedro', 'Porto Vitória', 'PR');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (5, 'Amanda', '99982838828', '28382', '1991-03-04', 'F', 'Jornalista', 'Italiana', 'Avenida Central', '100', null, 'São Pedro', 'General Cameiro', 'PR');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (6, 'Ângelo', '99982828181', '12323', '2000-01-01', 'M', 'Professor', 'Brasileiro', 'Avenida Beira Mar', '300', null, 'Centro', 'São Paulo', 'SP');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (7, 'Anderson','null', 'null', 'null', 'null',  'null', 'M', 'Professor', 'Italiano', 'Avenida Brasil', '100', 'AP', 'São Rosa ', 'Rio de Janeiro', 'SP');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (8, 'Camila', '9998282828', '2001-10-10', 'F', 'Professora', 'Norte Americana', 'Rua Centro', '4333', 'Centro', 'n', 'PR');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (9, 'Cristiano', null, null, null, 'M', 'Estudante', 'Alemã', 'Rua do Centro', '877', 'Casa', 'Centro', 'Porto Alegre', 'RS');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (10, 'Fabricio', '8828282828', '32323', null, 'M', 'Estudante', 'Brasileiro', null, null, null, null, 'PU', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (11, 'Fernanda', null, null, null, 'F', null, 'Brasileira', null, null, null, null, 'Porto União', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (12, 'Gilmar', '88881818181', '888', '2000-02-10', 'M', 'Estud.', null, 'Rua das Laranjeiras', '200', null, 'C. Nova', 'Canoinhas', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (13, 'Diego', '1010191919', '111939', null, 'M', 'Professor', 'Alemão', 'Rua Central', '455', 'Casa', 'Cidade N.', 'São Paulo', 'SP');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (14, 'Jeferson', null, null, '1983-07-01', 'M', null, 'Brasileiro', null, null, null, null, 'União da Vitória', 'PR');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (15, 'Jessica', null, null, null, 'F', 'Estudante', null, null, null, null, null, 'União da Vitória', 'PR');

select * from cliente;

select nome, data_nascimento from cliente;

select nome, data_nascimento as "Data de Nascimento" from cliente;

select 'CPF: ' || cpf || ' RG: ' || rg as "CPF e RG" from cliente;

select * from cliente limit 3;

select nome, data_nascimento from cliente where data_nascimento > '2000-01-01';

select nome from cliente where nome like 'C%';

select nome from cliente where nome like '%c%';

select nome, data_nascimento from cliente where data_nascimento between '1990-01-01' and '1998-01-01';

select nome, rg from cliente where rg is null;

select nome from cliente order by nome asc;

select nome from cliente order by nome desc;

select nome, genero, profissao from cliente order by nome desc;

select nome from cliente where nome like '%r%';

select nome from cliente where nome like 'C%';

-- 1. O nome, o gênero e a profissão de todos os clientes, ordenado pelo nome em ordem decrescente
select nome, genero, profissao from cliente order by nome desc;

-- 2. Os clientes que tenham a letra "R" no nome
select nome from cliente where nome like '%r%';

-- 3. Os clientes que o nome inicia com a letra "C"
select nome from cliente where nome like 'C%';

-- 4. Os clientes que o nome termina com a letra "A"
select nome from cliente where nome like '%a';

-- 5 Os clientes que moram no bairro "Centro"
select nome, bairro from cliente where bairro  = 'Centro' or bairro = 'Cto.' or bairro = 'Ctr.' 

-- 6. Os clientes que moram em complementos que iniciam com a letra "A" 
select nome, complemento from cliente where complemento like 'A%';

-- 7. Somente os clientes do sexo feminino
select nome, genero from cliente where genero like 'F'

-- 8. Os clientes que não informaram o CPF
select nome, cpf from cliente where cpf is null;

-- 9. O nome e a profissão dos clientes, ordenado em ordem crescente pelo nome da profissão 
select nome, profissao from cliente order by profissao;

-- 10. Os clientes de nacionalidade "Brasileira"
select nome, nacionalidade from cliente where nacionalidade like 'Brasil%';

-- 11. Os clientes que informaram o número da resisdência 
select nome, numero from cliente where numero is not null;

-- 12. Os clientes que moram em Santa Catarina 
select nome, uf from cliente where uf like 'SC';

-- 13. Os clientes que nasceram entre 01/01/2002
select nome, data_nascimento from cliente where data_nascimento between '2000-01-01' and '2002-01-01';

-- 14. O nome do cliente e o logradouro, número, complemento, bairro, município e UF concatenado de todos os clientes 
select nome || ' - ' || logradouro ||' - '|| numero || ' - ' || complemento || ' - ' || bairro || ' - ' || municipio || ' - ' || uf from cliente;

select * from cliente;
select * from cliente order by idcliente asc;

-- Mostrando como adicionar, atualizar e apagar informações com insert, update e delete

update cliente set nome = 'Teste' where idcliente ='1'
update cliente set nome = 'Adriano', genero = 'M', numero = '241' where idcliente = 4;
insert into cliente (idcliente, nome) values (16, 'João');
delete from cliente where idcliente = 16

-- Exercícios - comandos update e delete

-- Inserindo 3 clientes diferentes
insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, municipio, uf)
values (16, 'Maicon', '12349596421', '1234', '1965-10-10', 'F', 'Empresário', 'Florianópolis', 'PR');
insert into cliente (idcliente, nome, rg, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (17, 'Getúlio', '4631', 'F', 'Estudante', 'Brasileira', 'Rua Central', '343', 'Apartamento', 'Centro', 'Curitiba', 'SC');
insert into cliente (idcliente, nome, genero, profissao, nacionalidade, numero, complemento)
values (18, 'Sandra', 'M', 'Professor', 'Italiana', '12', 'Bloco A');

-- Atualizando os valores dos clientes adicionados

update cliente set cpf = '45390569432', genero = 'M', nacionalidade = 'Brasileira', uf = 'SC' where idcliente = 16;

update cliente set data_nascimento = '1978-04-01', genero = 'M' where idcliente = 17;

update cliente set genero = 'F', profissao = 'Professora', numero = '123' where idcliente = 18;

-- Apagando clientes

delete from cliente where idcliente = 16;
delete from cliente where idcliente = 18;

-- Criação da tabela "profissao" e definindo constraints

create table profissao (
	idprofissao integer not null,
	nome varchar(30) not null,

	constraint pk_prf_idprofissao primary key (idprofissao),
	constraint un_prf_nome unique(nome)
);

select profissao from cliente

-- Adicionando valores na tabela "profissao"
insert into profissao (idprofissao, nome) values (1, 'Estudante');
insert into profissao (idprofissao, nome) values (2, 'Engenheiro');
insert into profissao (idprofissao, nome) values (3, 'Pedreiro');
insert into profissao (idprofissao, nome) values (4, 'Jornalista');
insert into profissao (idprofissao, nome) values (5, 'Professor');

select * from profissao;

-- Criação da tabela "nacionalidade" e definindo constraints

create table nacionalidade (
	idnacionalidade integer not null,
	nome varchar(30) not null,

	constraint pk_ncn_idnacionalidade prim
select * from Produto;
ary key (idnacionalidade),
	constraint un_ncn_nome unique (nome)
);

select nacionalidade from cliente

insert into nacionalidade (idnacionalidade, nome) values (1, 'Brasileira');
insert into nacionalidade (idnacionalidade, nome) values (2, 'Italiana');
insert into nacionalidade (idnacionalidade, nome) values (3, 'Norte-americana');
insert into nacionalidade (idnacionalidade, nome) values (4, 'Alemã');

select * from nacionalidade

-- Criação da tabela "complemento" e definindo constraints

create table complemento (
	idcomplemento integer not null,
	nome varchar(30) not null,

	constraint pk_cpl_idcomplemento primary key (idcomplemento),
	constraint un_cpl_nome unique (nome)
);

select complemento from cliente;

insert into complemento (idcomplemento, nome) values (1, 'Casa');
insert into complemento (idcomplemento, nome) values (2, 'Apartamento');

select * from complemento

-- Criação da tabela "bairro" e definindo constraints

create table bairro (
	idbairro integer not null,
	nome varchar(30) not null,

	constraint pk_brr_idbairro primary key (idbairro),
	constraint un_brr_nome unique (nome)
)

select bairro from cliente;

insert into bairro (idbairro, nome) values (1, 'Centro');
insert into bairro (idbairro, nome) values (2, 'São Paulo');
insert into bairro (idbairro, nome) values (3, 'Santa Rosa');
insert into bairro (idbairro, nome) values (4, 'Cidade Nova');

select * from bairro;

select * from cliente order by idcliente;

-- Adicionando os valores das tabelas secundárias na principal

alter table cliente rename column profissao to idprofissao;
alter table cliente alter column idprofissao type integer;

-- Estudante -> 1, 9, 10, 12, 15, 17
-- Engenheiro -> 2
-- Pedreiro -> 3
-- Jornalista ->  4, 5
-- Professor -> 6, 7, 8, 13
-- Null -> 11, 14

alter table cliente drop idprofissao;
alter table cliente add idprofissao integer; -- foreign key
alter table cliente add constraint fk_cln_idprofissao foreign key (idprofissao) references profissao (idprofissao);

update cliente set idprofissao = 1 where idcliente in (1, 9, 10, 12, 15, 17);
update cliente set idprofissao = 2 where idcliente = 2;
update cliente set idprofissao = 3 where idcliente = 3;
update cliente set idprofissao = 4 where idcliente in (4, 5);
update cliente set idprofissao = 5 where idcliente in (6, 7, 8, 13);

-- Só é possível apagar linhas que não são referenciadas
select * from profissao;
delete from profissao where idprofissao = 10;
insert into profissao (idprofissao, nome) values (10, 'Teste');

select * from nacionalidade;
alter table cliente drop nacionalidade;
alter table cliente add idnacionalidade integer;
alter table cliente add constraint fk_cln_idnacionalidade foreign key (idnacionalidade) references nacionalidade (idnacionalidade);

update cliente set idnacionalidade = 1 where idcliente in (1, 2, 3, 4, 6, 10, 11, 14);
update cliente set idnacionalidade = 2 where idcliente in (5, 7);
update cliente set idnacionalidade = 3 where idcliente = 8;
update cliente set idnacionalidade = 4 where idcliente in (9, 13);

select * from complemento;

alter table cliente drop complemento;
alter table cliente add idcomplemento integer;
alter table cliente add constraint fk_cln_idcomplemento foreign key (idcomplemento) references complemento (idcomplemento);

update cliente set idcomplemento = 1 where idcliente in (1,4,9,13);
update cliente set idcomplemento = 2 where idcliente in (2,3,7);

select * from bairro;

alter table cliente drop bairro;
alter table cliente add idbairro integer;
alter table cliente add constraint fk_cln_idbairro foreign key (idbairro) references bairro (idbairro);

update cliente set idbairro = 1 where idcliente in (1, 12, 13);
update cliente set idbairro = 2 where idcliente in (2, 3, 6, 8, 9);
update cliente set idbairro = 3 where idcliente in (4, 5);
update cliente set idbairro = 4 where idcliente = 7;

create table uf (select Data_Pedido from Pedido where Data_Pedido '2008-04-10' between '2008-04-25';
	iduf integer not null,
	nome varchar(30) not null,
	sigla char(2) not null,

	constraint pk_ufd_idunidade_federecao primary key (iduf),
	constraint un_ufd_nome unique (nome),
	constraint un_ufd_sigla unique (sigla)
);

insert into uf (iduf, nome, sigla) values (1, 'Santa Catarina', 'SC');
insert into uf (iduf, nome, sigla) values (2, 'Paraná', 'PR');
insert into uf (iduf, nome, sigla) values (3, 'São Paulo', 'SP');
insert into uf (iduf, nome, sigla) values (4, 'Minas Gerais', 'MG');
insert into uf (iduf, nome, sigla) values (5, 'Rio Grande do Sul', 'RS');
insert into uf (iduf, nome, sigla) values (6, 'Rio de Janeiro', 'RJ');
select * from uf

create table municipio (
	idmunicipio integer not null,
	nome varchar(30) not null,
	iduf integer not null,

	constraint pk_mnc_idmunicipio primary key (idmunicipio),
	constraint un_mnc_nome unique (nome),
	constraint fk_mnc_iduf foreign key (iduf) references uf (iduf)
);

insert into municipio (idmunicipio, nome, iduf) values (1, 'Porto União', 1);
insert into municipio (idmunicipio, nome, iduf) values (2, 'Canoinhas', 1);
insert into municipio (idmunicipio, nome, iduf) values (3, 'Porto Vitória', 2);
insert into municipio (idmunicipio, nome, iduf) values (4, 'General Carneiro', 2);
insert into municipio (idmunicipio, nome, iduf) values (5, 'São Paulo', 3);
insert into municipio (idmunicipio, nome, iduf) values (6, 'Rio de Janeiro', 6);
insert into municipio (idmunicipio, nome, iduf) values (7, 'Uberlândia', 4);
insert into municipio (idmunicipio, nome, iduf) values (8, 'Porto Alegre', 5);
insert into municipio (idmunicipio, nome, iduf) values (9, 'União da Vitória', 2);
select * from municipio

select * from cliente;
alter table cliente drop municipio;
alter table cliente drop uf;
alter table cliente add idmunicipio integer;
alter table cliente add constraint fk_cliente_idmunicipio foreign key (idmunicipio) references municipio (idmunicipio);

update cliente set idmunicipio = 1 where idcliente in (1, 2, 10, 11);
update cliente set idmunicipio = 2 where idcliente in (3, 12);
update cliente set idmunicipio = 3 where idcliente = 4;
update cliente set idmunicipio = 4 where idcliente in (5);
update cliente set idmunicipio = 5 where idcliente in (6, 13);
update cliente set idmunicipio = 6 where idcliente in (7);
update cliente set idmunicipio = 7 where idcliente in (8);
update cliente set idmunicipio = 8 where idcliente in (9);
update cliente set idmunicipio = 9 where idcliente in (14, 15);

select * from cliente

-- Exercício da parte 24

-- Criação das tabelas
create table Fornecedor (
	IdFornecedor integer not null,
	nome varchar(50) not null,

	constraint pk_for_IdFornecedor primary key (IdFornecedor),
	constraint un_for_nome unique (nome)
);

create table Vendedor (
	IdVendedor integer not null,
	nome varchar(50) not null,

	constraint pk_ven_IdVendedor primary key (IdVendedor),
	constraint un_ven_nome unique (nome)
);

create table Transportadora (
	IdTransportadora integer not null,
	IdMunicipio integer not null,
	Nome varchar(50),
	Logradouro varchar(50),
	Numero varchar(10),

	constraint pk_trs_IdTransportadora primary key (IdTransportadora),
	constraint fk_mun_IdMunicipio foreign key (IdMunicipio) references municipio (idmunicipio),
	constraint un_nom_nome unique (nome)
);

create table Produto (
	IdProduto integer not null,
	IdFornecedor integer not null,
	Nome varchar(50) not null,
	Valor numeric(10,2) not null,

	constraint pk_pro_IdProduto primary key (IdProduto),
	constraint fk_for_IdFornecedor foreign key (IdFornecedor) references Fornecedor (IdFornecedor)
);

-- Inserção de valores nas tabelas

insert into Vendedor (IdVendedor, Nome) values (1,'André');
insert into Vendedor (IdVendedor, Nome) values (2,'Alisson');
insert into Vendedor (IdVendedor, Nome) values (3,'José');
insert into Vendedor (IdVendedor, Nome) values (4,'Ailton');
insert into Vendedor (IdVendedor, Nome) values (5,'Maria');
insert into Vendedor (IdVendedor, Nome) values (6,'Suelem');
insert into Vendedor (IdVendedor, Nome) values (7,'Aline');
insert into Vendedor (IdVendedor, Nome) values (8,'Silvana');

select * from Vendedor;

insert into Fornecedor (IdFornecedor, Nome) values (1,'Cap. Computadores');
insert into Fornecedor (IdFornecedor, Nome) values (2,'AA. Computadores');
insert into Fornecedor (IdFornecedor, Nome) values (3,'BB. Máquinas');

select * from Fornecedor;

insert into Transportadora (IdTransportadora, IdMunicipio, Nome, Logradouro, Numero) values (1, 9, 'BS. Transportes', 'Rua das Limas', 01);
insert into Transportadora (IdTransportadora, IdMunicipio, Nome) values (2, 5, 'União Transportes');

select * from Transportadora;

insert into Produto (IdProduto, IdFornecedor, Nome, Valor) values (1, 1, 'Microcomputador', 800);
insert into Produto (IdProduto, IdFornecedor, Nome, Valor) values (2, 1, 'Monitor', 500);
insert into Produto (IdProduto, IdFornecedor, Nome, Valor) values (3, 2, 'Placa mãe', 200);
insert into Produto (IdProduto, IdFornecedor, Nome, Valor) values (4, 2, 'HD', 150);
insert into Produto (IdProduto, IdFornecedor, Nome, Valor) values (5, 2, 'Placa de vídeo', 200);
insert into Produto (IdProduto, IdFornecedor, Nome, Valor) values (6, 3, 'Memória RAM', 100);
insert into Produto (IdProduto, IdFornecedor, Nome, Valor) values (7, 1, 'Gabinete', 35);

select * from Produto;

create table Pedido (
	IdPedido integer not null,
	IdCliente integer not null,
	IdTransportadora integer,
	IdVendedor integer not null,
	Data_Pedido date not null,
	Valor numeric(10,2) not null,

	constraint pk_ped_IdPedido primary key (IdPedido),
	constraint fk_cli_IdCliente foreign key (IdCliente) references cliente(idcliente),
	constraint fk_trs_IdTransportadora foreign key (IdTransportadora) references Transportadora(IdTransportadora),
	constraint fk_ven_IdVendedor foreign key (IdVendedor) references Vendedor(IdVendedor)
)

create table Pedido_Produto (
	IdPedido integer not null,
	IdProduto integer not null,
	Quantidade integer not null,
	Valor_Unitario numeric(10,2) not null,

	constraint pk_ped_IdPedido_IdProduto primary key (IdPedido, IdProduto),
	constraint fk_ped_IdPedido foreign key (IdPedido) references Pedido (IdPedido),
	constraint fk_pro_IdProduto foreign key (IdProduto) references Produto (IdProduto)
)

insert into Pedido (IdPedido, Data_Pedido, Valor, IdCliente, IdTransportadora, IdVendedor) values (1, '2008-04-01', 1300, 1, 1, 1);
insert into Pedido (IdPedido, Data_Pedido, Valor, IdCliente, IdTransportadora, IdVendedor) values (2, '2008-04-01', 500, 1, 1, 1);
insert into Pedido (IdPedido, Data_Pedido, Valor, IdCliente, IdTransportadora, IdVendedor) values (3, '2008-04-02', 300, 11, 2, 5);
insert into Pedido (IdPedido, Data_Pedido, Valor, IdCliente, IdTransportadora, IdVendedor) values (4, '2008-04-05', 1000, 8, 1, 7);
insert into Pedido (IdPedido, Data_Pedido, Valor, IdCliente, IdTransportadora, IdVendedor) values (5, '2008-04-06', 200, 9, 2, 6);
insert into Pedido (IdPedido, Data_Pedido, Valor, IdCliente, IdTransportadora, IdVendedor) values (6, '2008-04-06', 1985, 10, 1, 6);
insert into Pedido (IdPedido, Data_Pedido, Valor, IdCliente, IdTransportadora, IdVendedor) values (7, '2008-04-06', 800, 3, 1, 7);
insert into Pedido (IdPedido, Data_Pedido, Valor, IdCliente, IdVendedor) values (8, '2008-04-06', 175, 3, 7);
insert into Pedido (IdPedido, Data_Pedido, Valor, IdCliente, IdVendedor) values (9, '2008-04-07', 1300, 12, 8);
insert into Pedido (IdPedido, Data_Pedido, Valor, IdCliente, IdTransportadora, IdVendedor) values (10, '2008-04-10', 200, 6, 1, 8);
insert into Pedido (IdPedido, Data_Pedido, Valor, IdCliente, IdTransportadora, IdVendedor) values (11, '2008-04-15', 300, 15, 2, 1);
insert into Pedido (IdPedido, Data_Pedido, Valor, IdCliente, IdTransportadora, IdVendedor) values (12, '2008-04-20', 500, 15, 2, 5);
insert into Pedido (IdPedido, Data_Pedido, Valor, IdCliente, IdTransportadora, IdVendedor) values (13, '2008-04-20', 350, 9, 1, 7);
insert into Pedido (IdPedido, Data_Pedido, Valor, IdCliente, IdTransportadora, IdVendedor) values (14, '2008-04-23', 300, 2, 1, 5);
insert into Pedido (IdPedido, Data_Pedido, Valor, IdCliente, IdVendedor) values (15, '2008-04-23', 200, 11, 5);

insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (1,1,1,800);
insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (1,2,1,500);
insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (2,2,1,500);
insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (3,4,2,150);
insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (4,1,1,800);
insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (4,3,1,200);
insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (5,3,1,200);
insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (6,1,2,800);
insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (6,7,1,35);
insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (6,5,1,200);
insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (6,4,1,150);
insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (7,1,1,800);
insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (8,7,5,35);
insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (9,1,1,800);
insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (9,2,1,500);
insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (10,5,1,200);
insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (11,5,1,200);
insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (11,6,1,100);
insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (12,2,1,500);
insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (13,3,1,200);
insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (13,4,1,150);
insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (14,6,3,100);
insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
values (15,3,1,200);

/*-- MANO TU PODIA TER FEITO MAIS FÁCIL

 insert into Pedido_Produto (IdPedido, IdProduto, Quantidade, Valor_Unitario)
 values (algumas coisa), (outras coisas), (mais coisas)
 
*/

-- Exercícios da parte 29

-- 1
select nome from Vendedor order by nome ASC;

-- 2
select nome from Produto where valor > 200;

-- 3
select nome, valor, valor*0.9 as valor_descontado from Produto order by valor ASC;

-- 4
select nome from municipio where iduf = 5;

-- 5
select IdPedido, Data_Pedido from Pedido where Data_Pedido between '2008-04-10' and '2008-04-25' order by valor ASC;

-- 6
select IdPedido from Pedido where valor between 1000 and 1500;

-- 7
select IdPedido from Pedido where valor not between 100 and 500;

-- 8
select IdPedido from Pedido where IdVendedor = 1 order by valor DESC;

-- 9
select IdPedido from Pedido where IdCliente = 1 order by valor ASC;

-- 10
select IdPedido from Pedido where IdCliente = 15 and IdVendedor = 1;

-- 11
select IdPedido from Pedido where IdTransportadora = 2;

-- 12
select IdPedido from Pedido where IdVendedor = 5 or IdVendedor = 7;

-- 13
select IdCliente from cliente where IdMunicipio = 1 or IdMunicipio = 9;

-- 14
select IdCliente from cliente where IdMunicipio != 1 and IdMunicipio != 9; 

-- 15
select IdCliente from cliente where logradouro is null;

-- 16
select IdCliente from cliente where logradouro like 'Av.%';

-- 17
select IdVendedor from Vendedor where nome like 'S%';

-- 18
select IdVendedor from Vendedor where nome like '%a';

-- 19
select IdVendedor from Vendedor where nome not like 'A%';

-- 20
select * from municipio where nome like 'P%' and iduf = 1;

-- 21
select * from Transportadora where logradouro is not null;

-- 22
select * from Pedido_Produto where IdPedido = 1;

-- 23
select * from Pedido_Produto where IdPedido = 6 or IdPedido = 10;

-- Funções agregadas

select avg(valor) from pedido;

select count(IdMunicipio) from municipio;

select count(*) from municipio;

select * from transportadora;
select count(logradouro) from transportadora;
select count(*) from transportadora;
select count(IdTransportadora) from transportadora;

select * from municipio;
select count(IdMunicipio) from municipio where iduf = 2;

select max(valor) from pedido;
select min(valor), max(valor) from pedido;
select sum(valor) from pedido;

select idcliente, sum(valor) from pedido group by idcliente;

select idcliente, sum(valor) from pedido group by idcliente having sum(valor) > 500;

-- Exercícios - Funções agregadas

-- 1
select IdVendedor, avg(valor) from pedido group by IdVendedor having sum(valor) > 200;

-- 2
select IdVendedor from pedido group by IdVendedor having sum(valor) > 1500

-- 3
select IdVendedor, sum(valor) from pedido group by IdVendedor;

-- 4
select count(IdMunicipio) from municipio;

-- 5
select count(IdMunicipio) from municipio where iduf = 1 or iduf = 2;

-- 6
select iduf, count(IdMunicipio) from municipio group by iduf;

-- 7
select count(idcliente) from cliente where logradouro is not null;

-- 8
select IdMunicipio, count(idcliente) from cliente group by IdMunicipio;

-- 9
select count(IdFornecedor) from Fornecedor;

-- 10
select count(IdProduto) from Produto group by IdFornecedor;

-- 11
select avg(valor) from produto where IdFornecedor = 1;

-- 12
select sum(valor) from produto;

-- 13
select nome, valor from produto order by valor desc limit 1;

-- 14
select nome, valor from produto order by valor asc limit 1;

-- 15
select avg(valor) from produto;

-- 16
select count(IdTransportadora) from Transportadora;

-- 17
select avg(valor) from pedido;

-- 18
select idcliente, sum(valor) from pedido group by idcliente;

-- 19
select idvendedor, sum(valor) from pedido group by idvendedor;

-- 20
select idtransportadora, sum(valor) from pedido group by idtransportadora;

-- 21
select data_pedido, sum(valor) from pedido group by data_pedido;

-- 22
select idcliente, idvendedor, idtransportadora, sum(valor) from pedido group by idcliente, idvendedor, idtransportadora;

-- 23
select data_pedido, sum(valor) from pedido where valor > 200 and data_pedido between '2008-04-01' and '2008-12-10' group by data_pedido;

-- 24
select avg(valor) from pedido where idvendedor = 1;

-- 25
select avg(valor) from pedido where idcliente = 15;

-- 26
select count(idpedido) from pedido where idtransportadora = 1;

-- 27
select idvendedor, count(idpedido) from pedido group by idvendedor;

-- 28
select idcliente, count(idpedido) from pedido group by idcliente;

-- 29
select count(idpedido) from pedido where data_pedido between '2008-04-15' and '2008-04-25';

-- 30
select count(idpedido) from pedido where valor>1000;

-- 31
select idproduto, sum(quantidade) from pedido_produto where idproduto = 1;

-- 32
select idproduto, sum(quantidade) from pedido_produto group by idproduto;

-- 33
select idpedido, sum(valor_unitario) from pedido_produto group by idpedido;

-- 34
select idpedido, sum(quantidade) from pedido_produto group by idpedido;

-- 35
select sum(valor_unitario) from pedido_produto;

-- 36
select avg(valor_unitario) from pedido_produto where idpedido=6;

-- 37
select max(valor_unitario) from pedido_produto;

-- 38
select min(valor_unitario) from pedido_produto;

-- 39
select idpedido, sum(quantidade) from pedido_produto group by idpedido;

-- 40
select sum(quantidade) from pedido_produto;

-- Relacionamentos com joins

select 
	cliente.nome,
	profissao.nome
from 
	cliente
left outer join
	profissao on cliente.idprofissao = profissao.idprofissao;

select
	cln.nome,
	prf.idprofissao
from
	cliente as cln
inner join
	profissao as prf on cln.idprofissao = prf.idprofissao

select 
	cliente.nome,
	profissao.nome
from 
	cliente
right outer join
	profissao on cliente.idprofissao = profissao.idprofissao;

-- Exercício - joins

-- 1
select
	cln.nome,
	prf.nome as profissao,
	nac.nome as nacionalidade,
	logradouro,
	numero,
	com.nome as complemento,
	bai.nome as bairro,
	mun.nome as municipio,
	uf.nome as estado,
	uf.sigla as sigla
from
	cliente as cln
left outer join
	profissao as prf on cln.idprofissao = prf.idprofissao
left outer join
	nacionalidade as nac on cln.idnacionalidade = nac.idnacionalidade
left outer join
	complemento as com on cln.idcomplemento = com.idcomplemento
left outer join
	bairro as bai on cln.idbairro = bai.idbairro
left outer join
	municipio as mun on cln.idmunicipio = mun.idmunicipio
left outer join
	uf on mun.iduf = uf.iduf;

-- 2
select
	pro.nome as produto,
	pro.valor,
	frn.nome as fornecedor
from
	produto as pro
left outer join
	fornecedor as frn on pro.idfornecedor = frn.idfornecedor;

-- 3
select
	trs.nome,
	mun.nome
from
	transportadora as trs
left outer join
	municipio as mun on trs.idmunicipio = mun.idmunicipio;

-- 4
select
	data_pedido,
	valor,
	cln.nome as cliente,
	trs.nome as transportadora,
	vdd.nome as vendedor
from
	pedido as pdd
left outer join
	cliente as cln on pdd.idcliente = cln.idcliente
left outer join
	transportadora as trs on pdd.idtransportadora = trs.idtransportadora
left outer join
	vendedor as vdd on pdd.idvendedor = vdd.idvendedor;

-- 5
select
	pro.nome,
	quantidade,
	valor_unitario
from
	pedido_produto pdd_pro
left outer join
	produto as pro on pdd_pro.idproduto = pro.idproduto;

-- 6 O nome dos clientes e a data do pedido dos clientes que fizeram algum pedido (ordenado pelo nome do cliente).
select
	cln.nome,
	pdd.data_pedido
from
	cliente cln
inner join
	pedido pdd on cln.idcliente = pdd.idcliente
group by
	cln.nome,
	data_pedido

-- 7 O nome dos clientes e a data do pedido de todos os clientes, independente se tenham feito pedido (ordenado pelo nome do cliente).
select
	cln.nome,
	pdd.data_pedido
from
	cliente cln
left join
	pedido pdd on cln.idcliente = pdd.idcliente
group by
	cln.nome,
	data_pedido

-- 8 O nome da cidade e a quantidade de clientes que moram naquela cidade.
select
	mun.nome,
	count(*)
from
	municipio mun
left outer join
	cliente cln on mun.idmunicipio = cln.idmunicipio
group by
	mun.nome

-- 9
select
	frn.nome,
	count(idproduto)
from
	produto pro
left outer join
	fornecedor frn on pro.idfornecedor = frn.idfornecedor
group by
	frn.nome

-- 10
select
	cln.nome,
	sum(valor)
from
	pedido pdd
left outer join
	cliente cln on pdd.idcliente = cln.idcliente
group by
	cln.nome

-- 11
select
	vdd.nome,
	sum(valor)
from
	pedido pdd
left outer join
	vendedor vdd on pdd.idvendedor = vdd.idvendedor
group by
	vdd.nome

-- 12
select
	trs.nome,
	sum(valor)
from
	pedido pdd
left outer join
	transportadora trs on pdd.idtransportadora = trs.idtransportadora
group by
	trs.nome

-- 13
select
	cln.nome,
	count(idpedido)
from
	pedido pdd
left outer join
	cliente cln on pdd.idcliente = cln.idcliente
group by
	cln.nome

-- 14
select
	pro.nome,
	sum(quantidade)
from
	pedido_produto pdd_pro
left outer join
	produto pro on pdd_pro.idproduto = pro.idproduto
group by
	pro.nome
	
-- 15
select
	data_pedido,
	sum(valor_unitario) as somatorio
from
	pedido_produto pdd_pro
left outer join
	pedido pdd on pdd_pro.idpedido = pdd.idpedido
group by
	data_pedido

-- 16
select
	data_pedido,
	sum(quantidade)
from
	pedido_produto pdd_pro
left outer join
	pedido pdd on pdd_pro.idpedido = pdd.idpedido
group by
	data_pedido

-- Comandos adicionais
select * from pedido

select
	data_pedido,
	extract(day from data_pedido) as dia,
	extract(month from data_pedido) as mês,
	extract(year from data_pedido) as ano
from
	pedido

select
	nome,
	substring(nome from 1 for 5),
	substring(nome,2)
from
	cliente

select
	nome,
	upper(nome),
	lower(nome)
from
	cliente

select
	nome,
	cpf,
	coalesce(cpf, 'Não informado')
from
	cliente

select
	case sigla
		when 'PR' then 'Paraná'
		when 'SC' then 'Santa Catarina'
	else 'Outros'
	end as uf
from
	uf

-- Exercícios - comandos adicionais

-- 1
select
	nome,
	coalesce(extract(month from data_nascimento), 0)
from
	cliente

-- 2
select
	nome,
	case extract(month from data_nascimento)
		when 1 then 'Janeiro'
		when 2 then 'Fevereiro'
		when 3 then 'Março'
		when 4 then 'Abril'
		when 5 then 'Maio'
		when 6 then 'Junho'
		when 7 then 'Julho'
		when 8 then 'Agosto'
		when 9 then 'Setembro'
		when 10 then 'Outubro'
		when 11 then 'Novembro'
		when 12 then 'Dezembro'
	else
		'Não informado'
	end as mes
from
	cliente

-- 3
select
	nome,
	coalesce(extract(year from data_nascimento), 0)
from cliente

-- 4
select
	nome,
	substring(nome from 5 for 10)
from
	municipio

-- 5
select
	nome,
	upper(nome) as municipio
from
	municipio

-- 6
select
	nome,
	case genero
		when 'M' then 'Masculino'
		when 'F' then 'Feminino'
	end as genero
from
	cliente

-- 7
select
	nome,
	valor,
	case
		when valor >= 500 then 'Acima ou igual a 500'
	else 'Abaixo de 500'
	end as faixa
from
	produto

-- Subconsultas

-- Selecionr a data do pedido e o valor onde o valor seja maior que a média
-- dos valores de todos os pedido
select
	data_pedido,
	valor
from
	pedido
where
	valor > (select avg(valor) from pedido)

-- Exemplo com count
select
	pdd.data_pedido,
	pdd.valor,
	(select sum(quantidade) from pedido_produto pdp where pdp.idpedido = pdd.idpedido) as total
from
	pedido pdd

select * from pedido_produto

-- Exemplo com update
select * from pedido

update pedido set valor = valor * 1.05
where valor > (select avg(valor) from pedido)

select avg(valor) from pedido

-- Exercícios - Subconsultas
-- 1
select
	nome,
	(select nome from municipio mun where cln.idmunicipio = mun.idmunicipio)
from
	cliente cln
where
	idcliente != 1 and idmunicipio = 1

-- 2
select
	data_pedido,
	valor
from
	pedido
where
	valor < (select avg(valor) from pedido)

-- 3
select
	pdd.data_pedido,
	pdd.valor,
	cln.nome as cliente,
	vdd.nome as vendedor,
	(select sum(quantidade) from pedido_produto pdd_pro where pdd_pro.idpedido = pdd.idpedido)
from
	pedido pdd
left outer join
	cliente cln on pdd.idcliente = cln.idcliente
left outer join
	vendedor vdd on pdd.idvendedor = vdd.idvendedor
where
	
	(select sum(quantidade) from pedido_produto pdd_pro group by idpedido having sum(quantidade) > 2) 

select * from pedido_produto

select idpedido, sum(quantidade) from pedido_produto pdd_pro group by idpedido having sum(quantidade) > 2

-- 4
select
	nome,
	(select nome from transportadora trs where cln.idmunicipio = trs.idmunicipio)
from
	cliente cln
where
	idmunicipio = 9

-- 5
select
	nome,
	(select nome from transportadora trs where cln.idmunicipio = trs.idmunicipio)
from
	cliente cln
where
	idmunicipio = 9 or idmunicipio = 5

-- 6
update 
	pedido pdd set pdd.valor = pdd.valor * 1.05 where pdd.valor > (select avg(valor) from pedido)
where (select sum(pdd_pro.valor_unitario) )



-- 7
select
	nome,
	(select count(idpedido) from pedido where  )

-- Views
create view cliente_profissao as
select
	cln.nome as cliente,
	cln.cpf,
	prf.nome as profissao
from
	cliente cln
left outer join
	profissao prf on cln.idprofissao = prf.idprofissao

select * from cliente_profissao where profissao = 'Professor'

-- drop view "nome_da_coluna"

-- Exercícios views
-- 1
drop view info_cliente
create view info_cliente as
select
	cln.nome as cliente,
	prf.nome as profissao,
	nac.nome as nacionalidade,
	com.nome as complemento,
	mun.nome as municipio,
	uf.nome as unidade_federativa,
	bai.nome as bairro,
	cln.cpf,
	cln.rg,
	cln.data_nascimento,
	case cln.genero
		when 'F' then 'Feminino'
		when 'M' then 'Masculino'
	end as Genero,
	cln.logradouro,
	cln.numero,
	cln.observacoes
from
	cliente cln
left outer join
	profissao prf on prf.idprofissao = cln.idprofissao
left outer join
	nacionalidade nac on nac.idnacionalidade = cln.idnacionalidade
left outer join
	complemento com on com.idcomplemento = cln.idcomplemento
left outer join
	municipio mun on mun.idmunicipio = cln.idmunicipio
left outer join
	uf on uf.iduf = mun.iduf
left outer join
	bairro bai on bai.idbairro = cln.idbairro

-- 2
create view mun_uf_sigla as
select
	mun.nome as municipio,
	uf.nome as uf,
	uf.sigla as sigla
from
	municipio mun
left outer join
	uf on uf.iduf = mun.iduf

-- 3
create view pro_vlr_for as
select
	pro.nome as produto,
	pro.valor as valor,
	frn.nome as fornedor
from
	produto pro
left outer join
	fornecedor frn on frn.idfornecedor = pro.idfornecedor

-- 4
create view info_transportadora as
select
	trs.nome as transportadora,
	trs.logradouro,
	trs.numero,
	uf.nome as unidade_federativa,
	uf.sigla
from
	transportadora trs
left outer join
	municipio mun on mun.idmunicipio = trs.idmunicipio
left outer join
	uf on uf.iduf = mun.iduf

-- 5
create view pedidos_feitos as
select
	pdd.data_pedido,
	pdd.valor,
	trs.nome as transportadora,
	cln.nome as cliente,
	vdd.nome as vendedor
from
	pedido pdd
left outer join
	transportadora trs on trs.idtransportadora = pdd.idtransportadora
left outer join
	cliente cln on cln.idcliente = pdd.idcliente
left outer join
	vendedor vdd on vdd.idvendedor = pdd.idvendedor

-- 6
create view pro_quan_valor_uni_valor as
select
	pro.nome,
	pdd_pro.quantidade,
	pdd_pro.valor_unitario,
	pdd.valor
from
	pedido_produto pdd_pro
left outer join
	produto pro on pro.idproduto = pdd_pro.idproduto
left outer join
	pedido pdd on pdd.idpedido = pdd_pro.idpedido

-- Campos autoincremento
create table exemplo (
	idexemplo serial not null,
	nome varchar(50) not null,

	constraint pk_exemplo_idexemplo primary key (idexemplo)
)

insert into exemplo (nome) values ('Exemplo 1'), ('Exemplo 2'), ('Exemplo 3'), ('Exemplo 4'), ('Exemplo 5')

select * from exemplo

select * from bairro

select max(idbairro) + 1 from bairro
create sequence bairro_id_seq minvalue 5
alter table bairro alter idbairro set default nextval('bairro_id_seq')
alter sequence bairro_id_seq owned by bairro.idbairro
insert into bairro (nome) values ('Teste 1');
insert into bairro (nome) values ('Teste 2');

select * from bairro

-- Exercícios sequences - auto incremento

-- A- Cliente

select * from cliente

create sequence cliente_id_seq minvalue 18
alter table cliente alter idcliente set default nextval('cliente_id_seq')
alter sequence cliente_id_seq owned by cliente.idcliente

-- B- Complemento

select * from complemento

create sequence complemento_id_seq minvalue 3
alter table complemento alter idcomplemento set default nextval('complemento_id_seq')
alter sequence complemento_id_seq owned by complemento.idcomplemento

-- C- Fornecedor

select * from fornecedor

create sequence fornecedor_id_seq minvalue 4
alter table fornecedor alter idfornecedor set default nextval('fornecedor_id_seq')
alter sequence fornecedor_id_seq owned by fornecedor.idfornecedor

-- D- Município

select * from municipio

create sequence municipio_id_seq minvalue 10
alter table municipio alter idmunicipio set default nextval('municipio_id_seq')
alter sequence municipio_id_seq owned by municipio.idmunicipio

-- E- Nacionalidade

select * from nacionalidade

create sequence nacionalidade_id_seq minvalue 5
alter table nacionalidade alter idnacionalidade set default nextval('nacionalidade_id_seq')
alter sequence nacionalidade_id_seq owned by nacionalidade.idnacionalidade

-- F- Pedido

select * from pedido

create sequence pedido_id_seq minvalue 16
alter table pedido alter idpedido set default nextval('pedido_id_seq')
alter sequence pedido_id_seq owned by pedido.idpedido

-- G- Pedido Produto

-- H- Profissão

select * from profissao

create sequence profissao_id_seq minvalue 6
alter table profissao alter idprofissao set default nextval('profissao_id_seq')
alter sequence profissao_id_seq owned by profissao.idprofissao

-- I- Transportadora

select * from transportadora

create sequence transportadora_id_seq minvalue 3
alter table transportadora alter idtransportadora set default nextval('transportadora_id_seq')
alter sequence transportadora_id_seq owned by transportadora.idtransportadora

-- J- UF

select * from uf

create sequence uf_id_seq minvalue 7
alter table uf alter iduf set default nextval('uf_id_seq')
alter sequence uf_id_seq owned by uf.iduf

-- K- Vendedor

select * from vendedor

create sequence vendedor_id_seq minvalue 9
alter table vendedor alter idvendedor set default nextval('vendedor_id_seq')
alter sequence vendedor_id_seq owned by vendedor.idvendedor
alter sequence vendedor_id_seq owned by vendedor.idvendedor

-- Campos Default
alter table pedido alter column data_pedido set default current_date;
alter table pedido alter column valor set default 0;
insert into pedido (idcliente, idvendedor) values (1,1);
insert into pedido (idcliente, idvendedor, data_pedido, valor)
values (1, 1, '2022-10-10', 234);

select * from pedido

-- Exercícios valores default

-- 1

-- A
alter table pedido_produto alter column quantidade set default 1;

-- B
alter table pedido_produto alter column valor_unitario set default 0;

-- 2
alter table produto alter column valor set default 0;

-- Índices
create index idx_cln_nome on cliente (nome)

-- Exercícios índices
-- 1
create index idx_pdd_data_pedido on pedido (data_pedido)

-- 2
create index idx_pro_nome on produto (nome)

----------------------------------------------------------------------
