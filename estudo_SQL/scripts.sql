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
	
)

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






