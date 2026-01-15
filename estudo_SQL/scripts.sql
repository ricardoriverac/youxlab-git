-- Criando Tabela --

create table cliente(
	idcliente integer not null,
	nome varchar(50) not null,
	cpf char(11) not null,
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
+)

-- Inserção de Valores --

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (1, 'Manoel', '88828383821', '32323', '2001-10-10', 'M', 'Estudante', 'Brasileira', 'Rua Joaquim Nabuco', '23', 'Casa', 'Cidade Nova', 'Porto União', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (2, 'Geraldo', '12343299291', '56565', '1987-01-04', 'M', 'Engenheiro', 'Brasileira', 'Rua Das Limas', '200', 'Ap.', 'Centro', 'P.União', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (3, 'Carlos', '87732323227', '55463', '1967-10-01', 'M', 'Pedreiro', 'Brasileiro', 'Rua das Laranjas', '300', 'Apart.', 'Cto.', 'Canoinhas', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (4, 'Adriana', '12321222122', '98777', '1989-09-10', 'F', 'Jornalista', 'Brasileiro', 'Rua das Limas', '240', 'Casa', 'São Pedro', 'Porto Vitória', 'PR');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (5, 'Amanda', '99982838828', '28382', '1991-03-04', 'F', 'Jorn.', 'Italia', 'Av. Cetral', '100', null, 'São Pedro', 'General Carneiro', 'PR');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (6, 'Ângelo', '99982828181', '12323', '2000-01-01', 'M', 'Professor', 'Brasileiro', 'Av. Beira Mar', '300', null, 'Ctr.', 'São Paulo', 'SP');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (7, 'Anderson', null, null, null, 'M', 'Prof.', 'Italiano', 'AV. Brasil', '100', 'Apartamento', 'Santa Rosa', 'Rio de Janeiro', 'SP');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (8, 'Camila', '9998282828', null, '2001-10-10', 'F', 'Professora', 'Norte americana', 'Rua Central', '4333', null, 'Centro', 'Uberlância', 'MG');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (9, 'Cristiano', '9998282828', null, '2001-10-10', 'F', 'Professora', 'Norte americana', 'Rua Central', '4333', null, 'Centro', 'Uberlância', 'MG');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (10, 'Fabrício', '8828282828', '32323', null, 'M', 'Estudante', 'Brasileiro', null, null, null, null, 'PU', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (11, 'Fernanda', null, null, null, 'F', null, 'Brasileira', null, null, null, null, 'Posto União', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (12, 'Gilmar', '88881818181', '888', '2000-02-10', 'M', 'Estud.', null, 'Rua das Laranjas', '200', null, 'C. Nova', 'Canoinhas', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (13, 'Diego', '1010191919', '111939', null, 'M', 'Professor', 'Alemão', 'Rua Central', '455', 'Casa', 'Cidade N.', 'São Paulo', 'SP');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (14, 'Jeferson', null, null, '1983-07-01', 'M', null, 'Brasileiro', null, null, null, null, 'União Vitória', 'PR');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (15, 'Jessica', null, null, null, 'F', 'Estudante', null, null, null, null, null, 'União Vitória', 'PR');

-- Mostrar Tabela --
select * from cliente

-- Mudar o nome da tabela
select cpf as "CPF dos clientes" from cliente

-- Tabela Concatenada
select 'CPF: ' || cpf || ' RG: ' || rg as "CPF e RG  do cliente" from cliente

-- Limite de dados
select nome, cpf, data_nascimento from cliente limit 5;

-- Filtrar informações
select nome, numero from cliente where numero < '200';

--  like
select nome from cliente where nome like 'A';
-
-- %like
select nome from cliente where nome like '%b';

-- %like%
select nome from cliente where nome like '%a%'

-- like%
select nome from cliente where nome like 'a%'

-- between
select nome from cliente where data_nascimento between '2000-01-01' and  '1980-01-01;'

-- is null
select nome, rg from cliente where rg is null

-- order by 
select nome from cliente order by nome asc;

-- order by txt  desc 
select nome from cliente order by nome desc 

-- Exercícios -- 

-- Exercício 1° - O nome, o gênero e a profissão de todos os clientes, ordenado pelo nome em ordem decrescente 

select nome, genero, profissao from cliente order by nome desc;


-- Exercício 2° - Os clientes que tenham a letra “R” no nome 
select nome from cliente where nome like '%r%';


-- Exercícios 3° - Os clientes que o nome inicia com a letra “C”
select nome from cliente where nome like 'C%'

-- Exercício 4° -  Os clientes que o nome termina com a letra “A”
select nome from cliente where nome like '%a';

-- Exercícios 5° -  Os clientes que moram no bairro “Centro”
select nome, bairro from cliente where bairro like 'Centro' or bairro like 'Ctr.' or bairro like 'Cto.';

-- Exercício 6° -  Os clientes que moram em complementos que iniciam com a letra “A”
select nome, complemento from cliente where complemento is not null and nome like 'A%';

-- Exercício 7° -  Somente os clientes do sexo feminino
select nome from cliente where genero = 'F';

-- Exercícios 8° - Os clientes que não informaram o CPF
select nome, cpf from cliente where cpf is null

-- Exercícios 9° - O nome e a profissão dos clientes, ordenado em ordem crescente pelo nome da profissão
select nome, profissao from cliente order by profissao asc;

-- Exercícios 10° - Os clientes de nacionalidade “Brasileira”
select nome, nacionalidade from cliente where nacionalidade like 'Brasileiro' or nacionalidade like 'Brasileira';

-- Exercício 11° - Os clientes que informaram o número da residência
select nome, numero from cliente where numero is not null;

-- Exercício 12° -  Os clientes que moram em Santa Catarina
select nome, uf from cliente where uf like 'SC';

-- Exercício 13° - Os clientes que nasceram entre 01/01/2000 e 01/01/2002
select nome, data_nascimento from cliente where data_nascimento between '2000-01-01' and '2002-01-01';

-- Exercício 14° -  O nome do cliente e o logradouro, número, complemento, bairro, município e UF concatenado de todos os clientes
select 
'Nome: ' || nome || ' Endereço: ' || logradouro || ' N° da casa: ' || numero || ' Complemento: ' || complemento || ' Bairro: ' || bairro || ' Município: ' || municipio || ' UF: ' || uf from cliente

-- Update e  Delete -- 

-- update 
update cliente set nome = 'Teste' where idcliente = 1;

update cliente set nome = 'Adriano', genero = 'M', numero = '241' where idcliente = 4;

-- delete 
delete from cliente where idcliente = 17;

-- Criação de Tabelas --

-- profissao
create table profissao (
	idprofissao integer not null,
	nome varchar (30) not null,

	constraint pk_prf_idprofissao primary key (idprofissao),
	constraint un_prf_nome unique (nome)
);

insert into profissao (idprofissao, nome) values (1, 'Estudante');
insert into profissao (idprofissao, nome) values (2, 'Engenheiro');
insert into profissao (idprofissao, nome) values (3, 'Pedreiro');
insert into profissao (idprofissao, nome) values (4, 'Jornalista');
insert into profissao (idprofissao, nome) values (5, 'Professor');

select * from profissao;

-- nacionalidade
create table nacionalidade (
	idnacionalidade integer not null,
	nome varchar (30) not null,

	constraint pk_ncn_idnacionalidade primary key (idnacionalidade),
	constraint un_ncn_nome unique (nome)

);

insert into nacionalidade (idnacionalidade, nome) values (1, 'Brasileira');
insert into nacionalidade (idnacionalidade, nome) values (2, 'Italiana');
insert into nacionalidade (idnacionalidade, nome) values (3, 'Norte-americana');
insert into nacionalidade (idnacionalidade, nome) values (4, 'Alemã');

select * from nacionalidade;

-- complemento 
create table complemento (
	idcomplemento integer not null,
	nome varchar (30) not null,

	constraint pk_cpl_idcomplemento primary key (idcomplemento),
	constraint un_cpl_nome unique (nome)
	
);

insert into complemento (idcomplemento, nome) values (1, 'Casa');
insert into complemento (idcomplemento, nome) values (2, 'Apartamento');

select * from complemento;

-- bairro
create table bairro (
	idbairro integer not null,
	nome varchar(30) not null,

constraint pk_brr_idbairro primary key (idbairro),
constraint un_brr_idbairro unique (nome)

);

insert into bairro (idbairro, nome) values (1, 'Cidade Nova');
insert into bairro (idbairro, nome) values (2, 'Centro');
insert into bairro (idbairro, nome) values (3, 'São Pedro');
insert into bairro (idbairro, nome) values (4, 'Santa Rosa');

select * from cliente

-- Ligação das Colunas / profissao --
-- alter table - rename column

alter table cliente  rename column profissao to idprofissao;

-- alter table - drop
alter table cliente drop idprofissao;

-- alter table - add
alter table cliente add idprofissao integer;

alter table cliente add constraint fk_cln_idprofissao foreign key (idprofissao) references profissao (idprofissao);


-- Chave estrangeira - profissão --

-- Converção para os id das profissões 

-- Estudante -> 1, 9, 10, 12, 15, 17
-- Engenheiro -> 2
-- Pedreiro -> 3
-- Jornalista -> 4, 5
-- Professor -> 6, 7, 8, 13
-- Null -> 11, 14

update cliente set idprofissao = 1 where idcliente in (1, 9, 10, 12, 15, 17);
update cliente set idprofissao = 2 where idcliente = 2;
update cliente set idprofissao = 3 where idcliente = 3;
update cliente set idprofissao = 4 where idcliente in (4, 5);
update cliente set idprofissao = 5 where idcliente in (6, 7, 8, 13);

select * from profissao;

-- Ligação das Colunas / nacionalidade --
alter table cliente drop nacionalidade; 
alter table cliente add idnascionalidade integer;
alter table cliente add constraint fk_cln_idnacionalidade foreign key (idnascionalidade) references nacionalidade (idnacionalidade); 

update cliente set idnascionalidade = 1 where idcliente in (1,2,3,4,6,10,11,14);
update cliente set idnascionalidade = 2 where idcliente in (5,7);
update cliente set idnascionalidade = 3 where idcliente = 8;
update cliente set idnascionalidade = 4 where idcliente in (9,13);

select * from cliente;

-- Ligação das Colunas / complemento --
alter table cliente drop complemento;
alter table cliente add idcomplemento integer;
alter table cliente add constraint fk_cln_complemento foreign key (idcomplemento) references complemento (idcomplemento);

update cliente set idcomplemento = 1 where idcliente in (1,4,9,13);
update cliente set idcomplemento = 2 where idcliente in (2,3,7);

select * from cliente;

-- Ligação de colunas / bairro --
alter table cliente drop bairro;
alter table cliente add idbairro integer;
alter table cliente add constraint fk_brr_idbairro foreign key (idbairro) references bairro (idbairo);

update cliente set idbairro = 1 where idcliente in (1, 12, 13);
update cliente set idbairro = 2 where idcliente in (2, 3, 6, 8, 9);
update cliente set idbairro = 3 where idcliente in (4,5);
update cliente set idbairro = 4 where idcliente = 7;

select * from cliente;

-- Criação de tabela / uf --
create table uf (
	iduf integer not null,
	nome varchar (30) not null,
	sigla char (2) not null,

	constraint pk_ufd_idunidade_federativa primary key (iduf),
	constraint un_ufd_nome unique (nome),
	constraint un_ufd_sigla unique (sigla)
);

insert into uf (iduf, nome, sigla) values (1, 'Santa Catarina', 'SC');
insert into uf (iduf, nome, sigla) values (2, 'Paraná', 'PR');
insert into uf (iduf, nome, sigla) values (3, 'São Paulo', 'SP');
insert into uf (iduf, nome, sigla) values (4, 'Minas Gerais', 'MG');
insert into uf (iduf, nome, sigla) values (5, 'Rio Grande do Sul', 'RS');
insert into uf (iduf, nome, sigla) values (6, 'Rio de Janeiro', 'RJ');

-- Ligação de tabela / uf 



-- Criação de tabela / municipio --
create table municipio (
	idmunicipio integer not null,
	nome varchar (30) not null,
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

select * from uf;

-- Ligação de tabelar / municipios 
alter table cliente drop municipio;
alter table cliente add idmunicipio integer;
alter table cliente add constraint fk_cliente_idmunicipio foreign key (idmunicipio) references municipio (idmunicipio);

update cliente set idmunicipio = 1 where idcliente in (1, 2, 10, 11);
update cliente set idmunicipio = 2 where idcliente in (3,12);
update cliente set idmunicipio = 3 where idcliente = 4;
update cliente set idmunicipio = 4 where idcliente in (5);
update cliente set idmunicipio = 5 where idcliente in (6, 13);
update cliente set idmunicipio = 6 where idcliente in (7); 
update cliente set idmunicipio = 7 where idcliente in (8); 
update cliente set idmunicipio = 8 where idcliente in (9);
update cliente set idmunicipio = 9 where idcliente in (14, 15);

select * from cliente;

-- Exercício 

-- Criação de tabela / Fornecedor --
create table fornecedor (
	idfornecedor integer not null,
	nome varchar(30) not null,

	constraint pk_fnc_idfornecedor primary key (idfornecedor),
	constraint un_fnc_idfornecedor unique (nome)

);

insert into fornecedor (idfornecedor, nome) values (1, 'Cap. Computadores');
insert into fornecedor (idfornecedor, nome) values (2, 'AA. Computadores');
insert into fornecedor (idfornecedor, nome) values (3, 'BB. Computadores');

select * from fornecedor;


-- Criação de tabela / Vendedor --
create table vendedor(
	idvendedor integer not null, -- primary key
	nome varchar(50) not null, -- unique

	constraint pk_vnd_idvendedor primary key (idvendedor),
	constraint un_vnd_nome unique (nome)

);

insert into vendedor (idvendedor, nome) values (1, 'André');
insert into vendedor (idvendedor, nome) values (2, 'Alisson');
insert into vendedor (idvendedor, nome) values (3, 'José');
insert into vendedor (idvendedor, nome) values (4, 'Ailton');
insert into vendedor (idvendedor, nome) values (5, 'Maria');
insert into vendedor (idvendedor, nome) values (6, 'Suelem');
insert into vendedor (idvendedor, nome) values (7, 'Aline');
insert into vendedor (idvendedor, nome) values (8, 'Silvana');

select * from vendedor;

-- Criação de tabela / Transportadora --
create table transportadora (
	idtransportadora integer not null, -- primary key
	idmunicipio integer not null, -- foreign key
	nome varchar(50) not null, -- unique
	logradouro varchar(50),
	numero varchar(10),

	constraint pk_trp_idtransportadora primary key (idtransportadora),
	constraint fk_trp_idmunicipio foreign key (idmunicipio) references municipio (idmunicipio),
	constraint un_trp_nome unique (nome)
);

insert into transportadora (idtransportadora, idmunicipio, nome, logradouro, numero) values (1, '9', 'BS. Transportes', 'Rua das Limas', '01');
insert into transportadora (idtransportadora, idmunicipio, nome, logradouro, numero) values (2, '5', 'Uniao Transportes', null, null);

select * from municipio;

-- Criação da tabela / produto --
create table produto (
	idproduto integer not null, -- primery key
	idfornecedor integer not null, -- foreign key
	nome varchar(50) not null,
	valor numeric(10,2) not null,

	constraint pk_prd_idproduto primary key (idproduto),
	constraint fk_prd_idfornecedor foreign key (idfornecedor) references fornecedor (idfornecedor)

);

insert into produto (idproduto, idfornecedor, nome, valor)
values (1, 1, 'Microcomputador', '800');

insert into produto (idproduto, idfornecedor, nome, valor)
values (2, 1, 'Monitor', 500);

insert into produto (idproduto, idfornecedor, nome, valor)
values (3, 2, 'Placa mae', 200);

insert into produto (idproduto, idfornecedor, nome, valor)
values (4, 2, 'HD', 150);

insert into produto (idproduto, idfornecedor, nome, valor)
values (5, 2, 'Placa de Video', 200);

insert into produto (idproduto, idfornecedor, nome, valor)
values (6, 3, 'Memoria RAM', 100);

insert into produto (idproduto, idfornecedor, nome, valor)
values (7, 1, 'Gabinete', 35);

select * from produto;

-- Criação de tabela / Pedidos
create table pedido (
	idpedido integer not null, -- primery key
	idcliente integer not null, -- foreign key
	idtransportadora integer, -- foreign key 
	idvendedor integer not null, -- foreign key
	data_pedido date not null,
	valor numeric(10,2) not null,

	constraint pk_pdd_idpedido primary key (idpedido),
	constraint fk_pdd_idcliente foreign key (idcliente) references cliente (idcliente),
	constraint fk_pdd_idtransportadora foreign key (idtransportadora) references transportadora (idtransportadora),
	constraint fk_pdd_idvendedor foreign key (idvendedor) references vendedor (idvendedor) 
	
);

insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (1, '2008-04-01', 1300, 1, 1,  1);

insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (2, '2008-04-01', 500, 1, 1, 1);

insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (3, '2008-04-02', 300, 11, 2, 5);

insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (4, '2008-04-05', 1000, 8, 1, 7);

insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (5, '2008-04-06', 200, 9, 2, 6);

insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (6, '2008-04-06', 1985, 10, 1, 6);

insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (7, '2008-04-06', 800, 3, 1, 7);

insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (8, '2008-04-06', 175, 3, null, 7);

insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (9, '2008-04-07', 1300, 12, null, 8);

insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (10, '10-04-2008', 1300, 6, 1, 8);

insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (11, '2008-04-15', 300, 15, 2, 1);

insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (12, '2008-04-20', 500, 15, 2, 5);

insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (13, '2008-04-20', 350, 9, 2, 7);

insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (14, '2008-04-23', 300, 2, 1, 5);

insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (15, '2008-04-25', 200, 11, null, 5);


-- Criação de tabela / pedido_produto --

create table pedido_produto (
	idpedido integer not null, -- Primery key, Foreign key
	idproduto integer not null, -- Primery key, Foreing key
	quantidade integer not null,
	valor_unitario numeric(10,2) not null,

	constraint pk_pedido_produto_idpedidoidproduto primary key (idpedido, idproduto),
	
	constraint fk_pedido_produto_idpedido foreign key (idpedido) references pedido (idpedido),
	constraint fk_pedido_produto_idproduto foreign key (idproduto) references produto (idproduto)
	
);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (1, 1, 1, 800);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (1, 2, 1, 500);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (2, 2, 1, 500);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (3, 4, 2, 150);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (4, 1, 1, 800);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (4, 3, 1, 200);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (5, 3, 1, 200);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (6, 1, 2, 800);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (6, 7, 1, 35);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (6, 5, 1, 200);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (6, 4, 1, 200);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (7, 1, 1, 800);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (8, 7, 5, 35);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (9, 1, 1, 800);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (9, 2, 1, 500);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (10, 5, 1, 200);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (11, 5, 1, 200);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (11, 6, 1, 100);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (12, 2, 1, 500);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (13, 3, 1, 200);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (13, 4, 1, 150);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (14, 6, 3, 100);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (15, 3, 1, 200);

-- Exercício --

-- exercício 1
select nome from vendedor order by nome ASC;

-- exercício 2
select valor from produto where valor >= '200';

-- exercício 3
select nome, valor, valor * 1.10 as "produto 10%" from produto; 

-- exercícios 4
select nome  from municipio where iduf = 5

-- exercício 5
select *  from pedido where data_pedido between '2008-04-10' and '2008-04-25' order by valor DESC;

-- exercício 6
select * from pedido where valor between 1000.00 and 1500.00;

-- exercicio 7 
select * from pedido where valor not between  100 and 500;

-- exercicio 8
select * from pedido where idvendedor = 1 order by valor ASC;

-- exercicio 9
select * from pedido where idcliente = 1 order by valor ASC;

-- exercicio 10
select * from pedido where idcliente = 15 and idvendedor = 1

-- exercicio 11
select * from pedido where idtransportadora = 2

-- exercicios 12
select * from pedido where idvendedor in (5, 7);

-- exercicio 13
select * from cliente where idmunicipio in (1, 9);

-- exercicio 14 
select nome from cliente where idmunicipio in (1, 9);

-- exercicio 15
select * from cliente where logradouro is null or logradouro = '';

-- exercicio 16
select logradouro from cliente where logradouro like 'A%'

-- exercicio 17 
 select * from vendedor where nome like 's%';

-- exercicio 18 
select * from vendedor where nome like '%A'

-- exercicio 19 
select * from vendedor where nome not like 'A%'

-- exercicio 20
select * from municipio where iduf = 1;

-- exercicio 21 
select * from transportadora

-- exercicio 22
select * from produto where idproduto = 1

-- funções agregadas --

-- Função avg 
/* a função 'avg' soma todos os valores de uma
respequitiva tabela, e depois mostra a media 
da soma de todos os valores da tabela */

select avg(valor) from pedido

-- Função count 
/* Essa função conta somente aqueles que 
tem alguma informação (Somente os not null)*/

select count(logradouro) from transportadora

-- max, min, sum
/* MAX: serve para mostrar o maior valor da coluna de uma 
determinada tabela

MIN: serve para mostrar o menor valor de uma
coluna de uma determinada tabela 

SUM: ele soma todos os valores da coluna e 
mostra o resultado no final */

select max(valor) from pedido

select min(valor) from pedido

select sum(valor) from pedido

-- group by
/*Serve para agrupar colunas das tabelas,
mas só funciona se estiver usando uma função
agregada (max, min, sum, count e avg*/

select idcliente, sum(valor) from pedido group by idcliente having sum(valor) > 500;

-- Exercicios

-- 1.
select avg(valor), idvendedor from pedido GROUP BY idvendedor having sum(valor) > 200;

-- 2.
select idvendedor from pedido group by idvendedor having sum(valor) > 1500 

-- 3.
select idvendedor, sum(valor) from pedido group by idvendedor;

-- 4.
select count(idmunicipio) from municipio;

-- 5.
select count(idmunicipio) from municipio where iduf = 1 or iduf = 2;

-- 6.
select iduf, count(idmunicipio) from municipio group by iduf;

-- 7.
select count(idcliente) from cliente where logradouro is not null;

-- 8.
select idmunicipio, count(idcliente) from cliente group by idmunicipio;

-- 9.
select count(idfornecedor) from fornecedor;

-- 10.
select count(idproduto) from Produto group by idfornecedor;

-- 11.
select avg(valor) from produto where idfornecedor = 1 

-- 12.
select sum(valor) from produtos

-- 13.
select nome, valor from produto where idproduto = 2 

-- 14.
select nome, valor from produto where idproduto = 7

-- 15.
select avg(valor) from produto;

-- 16.
select count(idtransportadora) from transportadora;

-- 17.
select avg(valor) from produto;

-- 18.
select idcliente, sum(valor) from pedido group by idcliente;

-- 19.
select idvendedor, sum(valor) from pedido group by idvendedor;

-- 20.
select idtransportadora, sum(valor) from pedido group by idtransportadora

-- 21.
select data_pedido, sum(valor) from pedido group by data_pedido

-- 22.
select sum(valor) from pedido group by idcliente, idvendedor, idtransportadora;

-- 23.
select data_pedido, sum(valor) from pedido where valor > 200 and data_pedido between '2008-04-01' and '2008-12-10' group by data_pedido;

-- 24.
select sum(valor) from pedido where idvendedor = 1;

-- 25.
select sum(valor) from pedido where idcliente = 15;

-- 26.
select count(idtransportadora) from pedido where idtransportadora = 1;

-- 27.
select count(idpedido )from pedido group by idvendedor

-- 28.
select count(pedido) from pedido group by idcliente

-- 29.
select count(idpedido) from pedido where data_pedido between '2008-04-15' and '2008-04-25';

-- 30.
select count(valor) from pedido where valor > 1000

-- 31.
select sum(quantidade) from pedido_produto where idproduto = 1

-- 32.
select sum(quantidade) from pedido_produto group by idproduto;

-- 33.
select sum(valor) from pedido group by idpedido

-- 34.
select count(quantidade) from pedido_produto group by idpedido

-- 35.
select sum(valor_unitario) from pedido_produto;

-- 36.
select avg(idpedido) from pedido_produto where idpedido = 6;

-- 37.
select max(valor_unitario) from pedido_produto;

-- 38.
select sum(quantidade) from pedido_produto group by idpedido;

-- 39
select sum(quantidade) from pedido_produto;

-- Relacionamentos com joins --

-- left outer join 
select
	cliente.nome,
	profissao.nome
from
	cliente
left outer join
	profissao on profissao.idprofissao = cliente.idprofissao

-- inner join
select
	cliente.nome,
	profissao.nome
from
	cliente
inner join
	profissao on profissao.idprofissao = cliente.idprofissao

-- right outer join
select
	cliente.nome,
	profissao.nome
from
	cliente
right outer join
	profissao on profissao.idprofissao = cliente.idprofissao

-- Exercício

-- 1.
select
	cliente.nome,
	profissao.nome as profissao,
	nacionalidade.nome as nacionalidade,
	cliente.logradouro,
	cliente.numero,
	complemento.nome as complemento,
	bairro.nome as bairro,
	municipio.nome as municipio,
	uf.nome as unidade_federativa
from
	cliente
left outer join 
	profissao as profissao on profissao.idprofissao = cliente.idprofissao
left outer join
	nacionalidade on nacionalidade.idnacionalidade = cliente.idnacionalidade
left outer join 
	complemento on complemento.idcomplemento = cliente.idcomplemento
left outer join
	bairro on bairro.idbairro = cliente.idbairro
left outer join
	municipio on municipio.idmunicipio = cliente.idmunicipio
left outer join
	uf on uf.iduf = municipio.iduf

-- 2.
select 
	fornecedor.nome as fornecedor,
	produto.nome as produto,
	produto.valor as valor
from 
	produto
left outer join
	fornecedor on fornecedor.idfornecedor = produto.idfornecedor

-- 3.
select * from transportadora

select
	transportadora.nome as transportadora,
	municipio.nome as municipio
from 
	transportadora
right outer join
	municipio on municipio.idmunicipio = transportadora.idmunicipio

-- 4.
select
	pedido.data_pedido as data_pedido,
	pedido.valor as valor,
	cliente.nome as cliente,
	transportadora.nome as transportadora,
	vendedor.nome as vendedor
from 
	pedido
left outer join
	cliente on cliente.idcliente = pedido.idcliente
left outer join
	transportadora on transportadora.idtransportadora = pedido.idtransportadora
left outer join
	vendedor on vendedor.idvendedor = pedido.idvendedor

-- 5.
select
	produto.nome as produto,
	pedido_produto.quantidade, 
	pedido_produto.valor_unitario
from 
	pedido_produto
left outer join
	produto on produto.idproduto = pedido_produto.idproduto

-- 6.
select
	cliente.nome,
	pedido.data_pedido
from
	cliente 
inner join
	pedido  on cliente.idcliente = pedido.idcliente
group by
	cliente.nome,
	data_pedido

-- 7.
select
	cliente.nome,
	pedido.data_pedido
from
	cliente 
left join
	pedido  on cliente.idcliente = pedido.idcliente

-- 8.
select
	municipio.nome,
	count(*)
from
	municipio 
left outer join
	cliente  on municipio.idmunicipio = cliente.idmunicipio
group by
	municipio.nome

--  9.
select
	fornecedor.nome,
	count(idproduto)
from
	produto 
left outer join
	fornecedor  on pro.idfornecedor = fornecedor.idfornecedor
group by
	fornecedor.nome

-- 10.
select
	cliente.nome,
	sum(valor)
from
	pedido
left outer join
	cliente on pedido.idcliente = cliente.idcliente
group by
	cliente.nome

-- 11.
select 
	vendedor.nome as vendedor,
	sum(pedido.valor)
from 
	pedido
left outer join
	vendedor on vendedor.idvendedor = pedido.idvendedor
group by
	vendedor

-- 12.
select
	trasportadora.nome,
	sum(valor)
from
	pedido pdd
left outer join
	transportadora on pdd.idtransportadora = trasportadora.idtransportadora
group by
	trasportadora.nome
	
-- 13.
select
	cliente.nome,
	count(idpedido)
from
	pedido
left outer join
	cliente on pedido.idcliente = cliente.idcliente
group by
	cliente.nome

-- 14.
select
	produto.nome,
	sum(quantidade)
from
	pedido_produto
left outer join
	produto on pedido_produto.idproduto = produto.idproduto
group by
	produto.nome

-- 15
select
	data_pedido,
	sum(valor_unitario) as somatorio
from
	pedido_produto 
left outer join
	pedido on pedido_produto.idpedido = pedido.idpedido
group by
	data_pedido

-- 16.
select
	data_pedido,
	sum(quantidade) as 
from
	pedido_produto
left outer join
	pedido on pedido_produto.idpedido = pedido_produto.idpedido
group by
	data_pedido

-- Comandos adicionais

select
	data_pedido,
	extract(day from data_pedido),
	extract(month from data_pedido),
	extract(year from data_pedido)
from
	pedido

select   nome, substring(nome from 1 for 5), substring(nome, 2) from cliente 

select nome, upper(nome), lower(nome) from cliente;

select cpf, coalesce(cpf, 'Nenhuma informação adiquirida') from cliente

select 
	case sigla
		when 'PR' then 'Paraná'
		when 'SC' then 'Santa Catarina'
	else 'Outros'
	end as uf 
from
	uf

-- exercício

-- 1.
select
	nome,
	coalesce (extract(month from data_nascimento)::text, 'Não informado')
from
	cliente

-- 2.
select
	cliente.nome,
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
	else 'Data não informada'
	end as mes_de_nascimento
from 
	cliente
	
-- 3.
select
	nome,
	coalesce (extract(year from data_nascimento)::text, 'Informação não encontrada')
from
	cliente

-- 4.
select
	substring(nome from 5 for 10)
from
	municipio

-- 5.
select
	upper(nome)
from
	municipio

-- 6.
select
	nome,
	case genero
		when 'M' then 'Masculino'
		when 'F' then 'Feminino'
	else 'Não informado'
	end as Genero
from
	cliente;

-- 7.
select
	nome,
	valor,
	case
		when valor >= 500 then 'Acima ou igual a 500'
	else 'Abaixo de 500'
	end as faixa
from
	produto

-- Selecionar a data do pedido e o valor onde o valor seja maior que a média
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
	(select sum(quantidade) as total from pedido_produto pdp where pdp.idpedido = pdd.idpedido)
from
	pedido pdd

-- Exemplo com update
select * from pedido

update pedido set valor = valor + ((valor * 5 ) / 100)
where valor > (select avg(valor) from pedido)

-- Exercícios

-- 1.
select nome from cliente where idbairro = 1 and not left(nome, 1) = 'M';

-- 2.
select 
	data_pedido,
	valor
from
	pedido
where 
	(select avg(valor) from pedido) > valor

-- 3.
select 
	pdd.data_pedido,
	pdd.valor,
	cln.nome as nome_cliente,
	vnd.nome as nome_vendedor,
	pp.quantidade
from 
	pedido pdd
left outer join
	cliente cln on cln.idcliente = pdd.idcliente
left outer join
	vendedor vnd  on vnd.idvendedor = pdd.idvendedor
left outer join
	pedido_produto pp on pp.idpedido = pdd.idpedido
where
	not quantidade < 2 
	
-- 4.
select nome from cliente where idmunicipio = 9

-- 5.
select 
	cln.nome,
	cln.idmunicip
from 
	cliente cln
left outer join
	municipio mnc on mnc.idmunicipio = cln.idmunicipio
where 
	cln.idmunicipio = 5 and cln.idmunicipio = 9

--Views
create view cliente_profissao as
select
	cln.nome as clientes,
	prf.nome as profissao
from
	cliente cln
left outer join 
	profissao prf on cln.idprofissao = prf.idprofissao

select * from cliente_profissao

-- Exercico

-- 1.
select * from cliente;

create view informacoes_clientes as
select 
	cln.idcliente,
	cln.nome,
	prf.nome as profissao,
	ncn.nome as nacionalidade,
	cpl.nome as complemento,
	mnc.nome as municipio,
	cln.uf,
	brr.nome as bairro,
	cln.cpf,
	cln.rg,
	cln.data_nascimento,
	case genero
		when 'F' then 'Femenino'
		when 'M' then 'Masculino'
	else 'Genero não informado'
	end as genero,
	cln.numero,
	cln.logradouro
from
	cliente cln
left outer join
	profissao prf on prf.idprofissao = cln.idprofissao
left outer join
	nacionalidade ncn on ncn.idnacionalidade = cln.idnacionalidade
left outer join
	complemento cpl on cpl.idcomplemento = cln.idcomplemento
left outer join
	municipio mnc on mnc.idmunicipio = cln.idmunicipio
left  outer  join
	bairro brr on brr.idbairro = cln.idbairro

select * from informacoes_clientes

-- 2.

create view  endereco as
select
	mnc.nome as municipio,
	uf.nome as unidade_federativa,
	uf.sigla
from
	municipio mnc
left outer join
	uf on uf.iduf = mnc.iduf

-- 3.
create view pecas as
select
	frn.nome as nome_fornecedor,
	prd.nome as nome_componentes,
	prd.valor
from 
	produto prd
left outer join
	fornecedor frn on frn.idfornecedor = prd.idfornecedor

-- 4.
select * from transportadora

create view informacoes_transportadoras as
select 
	trn.nome,
	logradouro,
	numero,
	mnc.nome as nome_unidade_federativa,
	mnc.iduf as uf
from 
	transportadora trn
left outer join 
	municipio mnc on mnc.idmunicipio = trn.idmunicipio

-- 5.
select * from pedido

create view informacoes_pedido as
select
	data_pedido,
	valor,
	trn.nome as transportadora,
	cln.nome as cliente,
	vnd.nome as vendedor
from
	pedido pdd
left outer join 
	transportadora trn on trn.idtransportadora = pdd.idtransportadora
left outer join
	cliente cln on cln.idcliente = pdd.idcliente
left outer join
	vendedor vnd on vnd.idvendedor = pdd.idvendedor

-- 6
select * from produto

create view lista_produto as
select
	prd.nome,
	prd_pdd.quantidade,
	prd_pdd.valor_unitario,
	prd.valor
from
	produto prd
left outer join
	pedido_produto prd_pdd on prd_pdd.idproduto = prd.idproduto

-- Campos autoincremento 
create table exemplo(
	idexemplo serial not null,
	nome varchar (50) not null,

	constraint pk_exemplo_idexemplo primary key (idexemplo)
);

insert into exemplo (nome) values ('Exemplo 1');
insert into exemplo (nome) values ('Exemplo 2');
insert into exemplo (nome) values ('Exemplo 3');
insert into exemplo (nome) values ('Exemplo 4');
insert into exemplo (nome) values ('Exemplo 5');

select * from exemplo

select max (idbairro) + 1 from bairro
create sequence bairroxid_seq minvalue 5
alter table bairro alter idbairro set default nextval('bairroxid_seq')
alter sequence bairroxid_seq owned by bairro.idbairro

insert into bairro (nome) values ('Teste 1');
insert into bairro (nome) values ('Teste 2');

select * from bairro

-- Atividade

-- A.
select max(idcliente) + 1 from cliente

create sequence cliente_id_seq minvalue 18

alter table cliente alter idcliente set default nextval('cliente_id_seq')

alter sequence cliente_id_seq owned by cliente.idcliente

insert into cliente (nome) values ('Teste 1');
insert into cliente (nome) values ('Teste 2');

select * from cliente

delete from complemento
where idcomplemento = 3; 


-- B.
create sequence complemento_id_seq minvalue 3

alter table complemento alter idcomplemento set default nextval('complemento_id_seq')

alter sequence complemento_id_seq owned by complemento.idcomplemento

insert into complemento (nome) values ('Teste 1');
insert into complemento (nome) values ('Teste 2');

select * from complemento

-- C.
create sequence fornecedor_id_seq minvalue 4 

alter table fornecedor alter idfornecedor set default nextval('fornecedor_id_seq')

alter sequence fornecedor_id_seq owned by fornecedor.idfornecedor

-- D.
create sequence municipio_id_seq minvalue 10

alter table municipio alter idmunicipio set default nextval('municipio_id_seq')

alter sequence municipio_id_seq owned by municipio.idmunicipio

-- E
create sequence nacionalidade_id_seq minvalue 5

alter table nacionalidade alter idnacionalidade set default nextval('nacionalidade_id_seq')

alter sequence nacionalidade_id_seq owned by nacionalidade.idnacionalidade

-- F
create sequence pedido_id_seq minvalue 16

alter table pedido alter idpedido set default nextval('pedido_id_seq')

alter sequence pedido_id_seq owned by pedido.idpedido

-- G
create sequence produto_id_seq minvalue 8

alter table produto alter idproduto set default nextval('produto_id_seq')

alter sequence produto_id_seq owned by produto.idproduto

-- H
create sequence profissao_id_seq minvalue 6

alter table profissao alter idprofissao set default nextval('profissao_id_seq')

alter sequence profissao_id_seq owned by profissao.idprofissao

-- I

create sequence transportadora_id_seq minvalue 3

alter table transportadora alter idtransportadora set default nextval('transportadora_id_seq')

alter sequence transportadora_id_seq owned by transportadora.idtransportadora

-- J
create sequence uf_id_seq minvalue 7

alter table uf alter iduf set default nextval('uf_id_seq')

alter sequence uf_id_seq owned by uf.iduf

-- K
select max(idvendedor) + 1 from vendedor

create sequence vendedor_id_seq minvalue 9

alter table vendedor alter idvendedor set default nextval('vendedor_id_seq')

alter sequence vendedor_id_seq owned by vendedor.idvendedor

-- Campos default 

alter table pedido alter column data_pedido set default current_date;
alter table pedido alter column valor set default 0;

insert into pedido (idcliente, idvendedor) 
values (1, 1);

insert into pedido (idcliente, idvendedor, data_pedido, valor)
values (1, 1, '2022-10-10', 234);

select * from pedido

-- Exercicio
-- 1.

-- A.
alter table pedido_produto alter column quantidade set default 1;

-- B.
alter table pedido_produto alter column valor_unitario set default 0;

-- 2.
alter table produto alter column valor set default 0;

-- Indices

create index idx_cln_nome on cliente (nome);

-- Exercicio
create index idx_dt_data_pedido on pedido (data_pedido)

create index idx_prd_nome on produto (nome)


