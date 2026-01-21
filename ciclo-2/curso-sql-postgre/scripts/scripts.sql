pocreate table cliente(
	idcliente integer not null,
	nome varchar(50) not  null, -- Pedro 5, 45
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
values (3, 'Carlos', '87732323227','55463', '1967-01-10', 'M', 'Pedreiro', 'Brasileira', 'Rua das Laranjeiras', '300', 'Apat', 'Cto', 'Canoinhas', 'SC')

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (4, 'Adiana', '12321222122', '98777', '1989-09-10', 'F', 'Jornalista', 'Brasileira', 'Rua das Limas', '240', 'Casa', 'São Pedro', 'Porto Vitória', 'PR')

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (5, 'Amanda', '99982838828', '28382', '1991-03-04', 'F', 'Jorn', 'Italiana', 'Av. Central', '100', null, 'São Pedro', 'General Caneiro', 'PR')

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (6, 'Ângelo', '9982828181', '12323', '2000-01-01', 'M', 'Professor', 'Brasileiro', 'Av. Beira Mar', '300', null, 'Ctr', 'São Paulo', 'SP')

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (7, 'Anderson', null, null, null, 'M', 'Prof.', 'Italiano', 'Av. Brasil', '100', 'Apartamento', 'Santa Rosa', 'Rio de Janeiro', 'SP')

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (8, 'Camila', '9998282828', null, '2001-10-10', 'F', 'Professora', 'Norte Americana', 'Rua Central', '4333', null, 'Centro', 'Uberlândia', 'MG')

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (9, 'Cristiano', null, null, null, 'M', 'Estudante', 'Alemã', 'Ruan do Centro', '877', 'Casa', 'Centro', 'Porto Alegre', 'RS')

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (10, 'Fabrício', '8828282828', '32323', null, 'M', 'Estudante', 'Brasileiro', null, null, null, null, 'PU', 'SC')

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (11, 'Fernanda', null, null, null, 'F', null, 'Brasileira', null, null, null, null, 'Porto União', 'SC')

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (12, 'Glimar', '88881818181', '888', '2000-02-10', 'M', 'Estud', null, 'Rua das Laranjeiras', '200', null, 'C. Nova', 'Canoinhas', 'SC')

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (13, 'Diego', '1010191919', '111939', null, 'M', 'Professor', 'Alemão', 'Rua Central', '455', 'Casa', 'Cidade N.', 'São Paulo', 'SP')

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (14, 'Jeferson', null, null, '1983-07-01', 'M', null, 'Brasileiro', null, null, null, null, 'União da Vitória', 'PR')

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (15, 'Jessica', null, null, null, 'F', 'Estudante', null, null, null, null, null, 'União da Vitória', 'PR')

select * from cliente;		-- Retorna todos os dados dos clientes em tabela no "Terminal".

select nome, data_nascimento from cliente;		-- Retorna os nomes e data de nascimento de todos os clientes.

select nome, data_nascimento as "Data de nascimento" from cliente;		-- Muda o nome "data_nascimento" para "Data de nascimento".

select 'CPF: ' || cpf || 'RG: ' || rg as "CPF e RG" from cliente;		-- Concatena (adiciona) o "CPF" e o "RG" antes dos números e renomeia o início da tabela chamada "column".

select * from cliente limit 3;		-- Seleciona apenas pessoas da tabela de cliente.

select nome, data_nascimento from cliente where data_nascimento > '2000-01-01';		-- Retorna apenas os clientes que nasceram no dia 01-01-2000.

select nome from cliente where nome like 'C%';		-- Retorna todos os nomes que começam com a letra C.

select nome from cliente where nome like '%c%';		-- Retorna todos os nomes que possuem a letra C no meio.

select nome, data_nascimento from cliente where data_nascimento between '1990-01-01' and '1998-01-01';		-- Filtra todos os clientes que nasceram entre 01-01-1990 e 01-01-1998.

select nome, rg from cliente where rg is null;		--Retorna todos os clientes que possuem o rg nulo.

select nome from cliente order by nome asc;		--Retorna o nome dos clientes em ordem alfabética.

select nome from cliente order by nome desc;		--Retorna o nome dos clientes em ordem alfabética de trás para frente.

-- Exercícios – consultas simples

-- 1. O nome, o gênero e a profissão de todos os clientes, ordenado pelo nome em ordem decrescente

select nome, genero, profissao from cliente order by nome desc;

-- 2. Os clientes que tenham a letra “R” no nome

select nome from cliente where nome like '%r%';

-- 3. Os clientes que o nome inicia com a letra “C”

select nome from cliente where nome like 'C%';

-- 4. Os clientes que o nome termina com a letra “A”

select nome from cliente where nome like '%a';

-- 5. Os clientes que moram no bairro “Centro”

select nome, bairro from cliente where bairro like 'Centro' or bairro like 'Cto' or bairro like 'Ctr';

-- 6. Os clientes que moram em complementos que iniciam com a letra “A”

select nome, complemento from cliente where complemento like 'A%';

-- 7. Somente os clientes do sexo feminino

select nome, genero from cliente where genero like 'F';

-- 8. Os clientes que não informaram o CPF

select nome, cpf from cliente where cpf is null;

-- 9. O nome e a profissão dos clientes, ordenado em ordem crescente pelo nome da profissão

select nome, profissao from cliente order by profissao asc;

-- 10. Os clientes de nacionalidade “Brasileira”

select nome, nacionalidade from cliente where nacionalidade like 'Brasil%';

-- 11. Os clientes que informaram o número da residência

select nome, numero from cliente where numero is not null;

-- 12. Os clientes que moram em Santa Catarina

select nome, uf from cliente where uf like 'SC';

-- 13. Os clientes que nasceram entre 01/01/2000 e 01/01/2002

select nome, data_nascimento from cliente where data_nascimento between '2000-01-01' and '2002-01-01';

-- 14. O nome do cliente e o logradouro, número, complemento, bairro, município e UF concatenado de todos os clientes

select nome || ' - ' || logradouro || ' - ' || numero || ' - ' || bairro || ' - ' || municipio || ' - ' || uf as "Info Clientes" from cliente;


-- Comandos update e delete


select * from cliente;
update cliente set nome = 'Teste' where idcliente = 1;		-- Muda o nome do primeiro id para o nome "Teste".
update cliente set nome = 'Adriano', genero = 'M', numero = '241' where idcliente = 4;
insert into cliente (idcliente, nome) values (16, 'João')		-- Adiciona um novo cliente no final da lista (Com valores nulos).
delete from cliente where idcliente = 16;		-- Apaga o cliente de acordo com o id colocado.

-- Exercícios – comandos update e delete

-- 1. Insira os dados abaixo na tabela de clientes

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, municipio, uf)
values (16, 'Maicon', '12349596421', '1234', '1965-10-10', 'F', 'Empresário', 'Florianópolis', 'PR')

insert into cliente (idcliente, nome, rg, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (17, 'Getúlio', '4631', 'F', 'Estudante', 'Brasileira', 'Rua Central', '343', 'Apartamento', 'Centro', 'Curitiba', 'SC')

insert into cliente (idcliente, nome, genero, profissao, nacionalidade, numero, complemento)
values (18, 'Sandra', 'M', 'Professor', 'Italiana', '12', 'Bloco A')


-- 2. Altere os dados do cliente Maicon

select * from cliente;

-- a. O CPF para 45390569432
update cliente set cpf = '45390569432' where idcliente = 16;

-- b. O gênero para M
update cliente set genero = 'M' where idcliente = 16;

-- c. A nacionalidade para Brasileira
update cliente set nacionalidade = 'Brasileira' where idcliente = 16; 

-- d. O UF para SC
update cliente set uf = 'SC' where idcliente = 16;


-- 3. Altere os dados do cliente Getúlio

select * from cliente;

-- a. A data de nascimento para 01/04/1978
update cliente set data_nascimento = '1978-04-01' where idcliente = 17;

--  b. O gênero para M
update cliente set genero = 'M' where idcliente = 17;

-- 4. Altere os dados da cliente Sandra

select * from cliente;

-- a. O gênero para F
update cliente set genero = 'F' where idcliente = 18;

-- b. A profissão para Professora
update cliente set profissao = 'Professora' where idcliente = 18;

-- c. O número para 123
update  cliente set numero = '123' where idcliente = 18;


-- 5. Apague o cliente Maicon
delete from cliente where idcliente = 16;


-- 6. Apague a cliente Sandra
delete from cliente where idcliente = 18;


-- Criação de novas tabelas

create table profissao (
	idprofissao integer not null,
	nome varchar(30) not null,

	constraint pk_prf_idprofissao primary key (idprofissao),
	constraint un_prf_nome unique (nome)
);

insert into profissao (idprofissao, nome) values (1, 'Estudante');
insert into profissao (idprofissao, nome) values (2, 'Engenheiro');
insert into profissao (idprofissao, nome) values (3, 'Pedreiro');
insert into profissao (idprofissao, nome) values (4, 'Jornalista');
insert into profissao (idprofissao, nome) values (5, 'Professor');

select * from profissao;

create table nacionalidade (
	idnacionalidade integer not null,
	nome varchar(30) not null,

	constraint pk_ncn_idnacionalidade primary key (idnacionalidade),
	constraint un_ncn_nome unique (nome)
);

select nacionalidade from cliente;

insert into nacionalidade (idnacionalidade, nome) values (1, 'Brasileira');
insert into nacionalidade (idnacionalidade, nome) values (2, 'Italiana');
insert into nacionalidade (idnacionalidade, nome) values (3, 'Norte-americana');
insert into nacionalidade (idnacionalidade, nome) values (4, 'Alemã');

select * from nacionalidade;

create table complemento (
	idcomplemento integer not null,
	nome varchar(30) not null,

	constraint pk_cpl_idcomplemento primary key (idcomplemento),
	constraint un_cpl_nome unique (nome)
);

insert into complemento (idcomplemento, nome) values (1, 'Casa');
insert into complemento (idcomplemento, nome) values (2, 'Apartamento');

select * from complemento;

create table bairro (
	idbairro integer not null,
	nome varchar(30) not null,

	constraint pkl_brr_idbairro primary key (idbairro),
	constraint un_brr_nome unique (nome)
);

insert into bairro (idbairro, nome) values (1, 'Cidade Nova');
insert into bairro (idbairro, nome) values (2, 'Centro');
insert into bairro (idbairro, nome) values (3, 'São Pedro');
insert into bairro (idbairro, nome) values (4, 'Santa Rosa');

select * from bairro

select * from cliente;

alter table cliente rename column profissao to idprofissao;		-- Altera a estrutura da tabela.
alter table cliente alter column idprofissao type interger;

-- Posição de cada Profissão
-- Estudante -> 1, 9, 10, 12, 15, 17
-- Engenheiro -> 2
-- Pedreiro -> 3
-- Jornalista -> 4, 5
-- Professor -> 6, 7, 8, 13
-- Null -> 11, 14

alter table cliente drop idprofissao;
alter table cliente add idprofissao integer;
alter table cliente add constraint fk_cln_idprofissao foreign key (idprofissao) references profissao (idprofissao)		-- Foreign key (Chave estrangeira)

update cliente set idprofissao = 1 where idcliente in (1, 9, 10, 12, 15, 17);
update cliente set idprofissao = 2 where idcliente = 2;
update cliente set idprofissao = 3 where idcliente = 3;
update cliente set idprofissao = 4 where idcliente in (4, 5);
update cliente set idprofissao = 5 where idcliente in (6, 7, 8, 13);

select * from profissao;
delete from profissao where idprofissao = 10;
insert into profissao (idprofissao, nome) values (10, 'Teste');


select * from cliente;
alter table cliente drop nacionalidade;
alter table cliente add idnacionalidade integer;
alter table cliente add constraint fk_cln_idnacionalidade foreign key (idnacionalidade) references nacionalidade (idnacionalidade);

select * from nacionalidade
update cliente set idnacionalidade = 1 where idcliente in (1, 2, 3, 4, 6, 10, 11, 14);
update cliente set idnacionalidade = 2 where idcliente in (5, 7);
update cliente set idnacionalidade = 3 where idcliente = 8;
update cliente set idnacionalidade = 4 where idcliente in (9, 13);


select * from cliente;
alter table cliente drop complemento;
alter table cliente add idcomplemento integer;
alter table cliente add constraint fk_cln_idcomplemento foreign key (idcomplemento) references complemento (idcomplemento);

update cliente set idcomplemento = 1 where idcliente in (1, 4, 9, 13);
update cliente set idcomplemento = 2 where idcliente in (2, 3, 7);


select * from cliente;
alter table cliente drop bairro;
alter table cliente add idbairro integer;
alter table cliente add constraint fk_cln_idbairro foreign key (idbairro) references bairro (idbairro);

select * from bairro;
update cliente set idbairro = 1 where idcliente in (1, 12, 13);
update cliente set idbairro = 2 where idcliente in (2, 3, 6, 8, 9);
update cliente set idbairro = 3 where idcliente in (4, 5);
update cliente set idbairro = 4 where idcliente = 7;


select * from cliente;
create table uf (
	iduf integer not null,
	nome varchar(30) not null,
	sigla char(2) not null,

	constraint pk_ufd_idunidade_federacao primary key (iduf),
	constraint un_ufd_nome unique (nome),
	constraint un_ufd_sigla unique (sigla)
);

insert into uf (iduf, nome, sigla) values (1, 'Santa Catarina', 'SC');
insert into uf (iduf, nome, sigla) values (2, 'Paraná', 'PR');
insert into uf (iduf, nome, sigla) values (3, 'São Paulo', 'SP');
insert into uf (iduf, nome, sigla) values (4, 'Minas Gerais', 'MG');
insert into uf (iduf, nome, sigla) values (5, 'Rio Grande do Sul', 'RS');
insert into uf (iduf, nome, sigla) values (6, 'Rio de Janeiro', 'RJ');

select * from uf;

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
select * from municipio;

select * from cliente; 
alter table cliente drop municipio;
alter table cliente drop uf;
alter table cliente add idmunicipio integer;
alter table cliente add constraint fk_cliente_idmunicipio foreign key (idmunicipio) references municipio (idmunicipio);  

update cliente set idmunicipio = 1 where idcliente in (1, 2, 10, 11);
update cliente set idmunicipio = 2 where idcliente in (3, 12);
update cliente set idmunicipio = 3 where idcliente = 4;
update cliente set idmunicipio = 4 where idcliente = 5;
update cliente set idmunicipio = 5 where idcliente in (6, 13);
update cliente set idmunicipio = 6 where idcliente = 7;
update cliente set idmunicipio = 7 where idcliente = 8;
update cliente set idmunicipio = 8 where idcliente = 9;
update cliente set idmunicipio = 9 where idcliente in (14, 15);


-- #24 Exercício 
-- Criação de Tabelas e Inserção de Dados

create table fornecedor (
	idfornecedor integer not null,
	nome varchar(50) not null,

	constraint pk_fnc_idfornecedor primary key (idfornecedor),
	constraint un_fnc_nome unique (nome)
);

insert into fornecedor (idfornecedor, nome) values (1, 'Cap. Computadores');
insert into fornecedor (idfornecedor, nome) values (2, 'AA. Computadores');
insert into fornecedor (idfornecedor, nome) values (3, 'BB. Máquinas');
select * from fornecedor;

--

create table vendedor (
	idvendedor integer not null,
	nome varchar(50) not null,

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

--

create table transportadora (
	idtransportadora integer not null,
	idmunicipio integer not null,
	nome varchar(50) not null,
	logradouro varchar(50),
	numero varchar(10),

	constraint pk_tpt_idtransportadora primary key (idtransportadora),
	constraint un_tpt_nome unique (nome),
	constraint fk_tpt_idmunicipio foreign key (idmunicipio) references municipio (idmunicipio)
);

insert into transportadora (idtransportadora, idmunicipio, nome, logradouro, numero) values (1, 9, 'BS. Transporte', 'Rua das Limas', 1);
insert into transportadora (idtransportadora, idmunicipio, nome, logradouro, numero) values (2, 5, 'União Transporte', null, null);
select * from transportadora;

--

create table produto (
	idproduto integer not null,
	idfornecedor integer not null,
	nome varchar(50) not null,
	valor numeric(10,2) not null,

	constraint pk_pdt_idproduto primary key (idproduto),
	constraint fk_pdt_idfornecedor foreign key (idfornecedor) references fornecedor (idfornecedor)
);

insert into produto (idproduto, idfornecedor, nome, valor) values (1, 1, 'Microcomputador', 800);
insert into produto (idproduto, idfornecedor, nome, valor) values (2, 1, 'Monitor', 500);
insert into produto (idproduto, idfornecedor, nome, valor) values (3, 2, 'Placa Mãe', 200);
insert into produto (idproduto, idfornecedor, nome, valor) values (4, 2, 'HD', 150);
insert into produto (idproduto, idfornecedor, nome, valor) values (5, 2, 'Placa de Vídeo', 200);
insert into produto (idproduto, idfornecedor, nome, valor) values (6, 3, 'Memória RAM', 100);
insert into produto (idproduto, idfornecedor, nome, valor) values (7, 1, 'Gabinete', 35);
select * from produto;

--

-- Tabelas de Pedido
create table pedido (
	idpedido integer not null,
	idcliente integer not null,
	idtransportadora integer,
	idvendedor integer not null,
	data_pedido date not null,
	valor numeric not null,

	constraint pk_pdd_idpedido primary key (idpedido),
	constraint fk_pdd_idcliente foreign key (idcliente) references cliente (idcliente),
	constraint fk_pdd_idtransportadora foreign key (idtransportadora) references transportadora (idtransportadora),
	constraint fk_pdd_idvendedor foreign key (idvendedor) references vendedor (idvendedor)
);

select * from cliente;
select * from transportadora;
select * from vendedor;

insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (1, '2008-04-01', 1300, 1, 1, 1);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (2, '2008-04-01', 500, 1, 1, 1);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (3, '2008-04-02', 300, 11, 2, 5);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (4, '2008-04-05', 1000, 8, 1, 7);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (5, '2008-04-06', 200, 9, 2, 6);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (6, '2008-04-06', 1985, 10, 1, 6);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (7, '2008-04-06', 800, 3, 1, 7);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (8, '2008-04-06', 175, 3, null, 6);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (9, '2008-04-07', 1300, 12, null, 8);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (10, '2008-04-10', 200, 6, 1, 8);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (11, '2008-04-15', 300, 15, 2, 1);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (12, '2008-04-20', 500, 15, 2, 5);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (13, '2008-04-20', 350, 9, 1, 7);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (14, '2008-04-23', 300, 2, 1, 5);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (15, '2008-04-25', 200, 11, null, 5);
select * from pedido;


create table pedido_produto (
	idpedido integer not null,
	idproduto integer not null,
	quantidade integer not null,
	valor_unitario numeric not null,

	constraint pk_pdp_idpedidoproduto primary key (idpedido, idproduto),
	constraint fk_pdp_idproduto foreign key (idproduto) references produto (idproduto),
	constraint fk_pdp_idpedido foreign key (idpedido) references pedido (idpedido)
);


select * from pedido;

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
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (6, 4, 1, 150);
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
select * from pedido_produto;


-- Exercícios – consultas simples

-- 1. Somente o nome de todos os vendedores em ordem alfabética.

select nome from vendedor order by nome asc;

-- 2. Os produtos que o preço seja maior que R$200,00, em ordem crescente pelo preço.

select nome, valor from produto where valor > 200;

-- 3. O nome do produto, o preço e o preço reajustado em 10%, ordenado pelo nome do produto.

select nome, valor, valor + (valor * 10) / 100 as Reajuste from produto;

-- 4. Os municípios do Rio Grande do Sul.
select nome from municipio where iduf = 5;

-- 5. Os pedidos feitos entre 10/04/2008 e 25/04/2008 ordenado pelo valor.
select * from pedido where data_pedido between '2008-04-10' and '2008-04-25' order by valor asc;

-- 6. Os pedidos que o valor esteja entre R$1.000,00 e R$1.500,00.
select * from pedido where valor between '1000' and '1500';

-- 7. Os pedidos que o valor não esteja entre R$100,00 e R$500,00.
select * from pedido where valor not between '100' and '500';

-- 8. Os pedidos do vendedor André ordenado pelo valor em ordem decrescente.
select * from pedido where idvendedor = 1 order by valor desc;

-- 9. Os pedidos do cliente Manoel ordenado pelo valor em ordem crescente.
select * from pedido where idcliente = 1 order by valor asc;

-- 10. Os pedidos da cliente Jéssica que foram feitos pelo vendedor André.
select * from pedido where idvendedor = 1 and idcliente = 15;

-- 11. Os pedidos que foram transportados pela transportadora União Transportes.
select * from pedido where idtransportadora = 2;

-- 12. Os pedidos feitos pela vendedora Maria ou pela vendedora Aline.
select * from pedido where idvendedor = 5;
select * from pedido where idvendedor = 7;

-- 13. Os clientes que moram em União da Vitória ou Porto União.
select * from cliente where idmunicipio in (1, 9);

-- 14. Os clientes que não moram em União da Vitória e nem em Porto União.
select * from cliente where not idmunicipio in (1, 9);

-- 15. Os clientes que não informaram o logradouro.
select * from cliente where logradouro is null;

-- 16. Os clientes que moram em avenidas.
select * from cliente where logradouro like 'Av%';

-- 17. Os vendedores que o nome começa com a letra S.
select * from vendedor where nome like 'S%';

-- 18. Os vendedores que o nome termina com a letra A.
select * from vendedor where nome like '%a'

--19. Os vendedores que o nome não começa com a letra A.
select * from vendedor where nome not like 'A%';

-- 20. Os municípios que começam com a letra P e são de Santa Catarina.
select * from municipio where nome like 'P%' and iduf = 1;

-- 21. As transportadoras que informaram o endereço.
select * from transportadora where logradouro is not null;

-- 22. Os itens do pedido 01.
select * from pedido_produto where idpedido = 1; 

-- 23. Os itens do pedido 06 ou do pedido 10.
select * from pedido_produto where idpedido in (6, 10);

--

-- Funções agregadas 

select avg(valor) from pedido;		-- Faz a média de todos os valores na parte de "valor" na tabela "pedido".

select count(idmunicipio) from municipio;		-- Faz a contagem da quantidade de colunas que o "idmunicipio" possui.

select count(*) from municipio;		-- Retorna a contagem total de registros.

select count(logradouro) from transportadora;		-- Retorna todos os valores nulos.

select count(idtransportadora) from transportadora;			-- Retorna todos os valores registrados.

select count(idmunicipio) from municipio where iduf = 2;		-- Retorna todos os valores registrados com o "iduf" 2.

select min(valor), max(valor) from pedido;		-- Retorna o menor e o maior número da tabela "pedido".

select sum(valor) from pedido;		-- Soma todos os valores da coluna de "valor" da tabela "pedido".

select idcliente, sum(valor) from pedido group by idcliente;		-- Faz o agrupamento de todos os registros.

select idcliente, sum(valor) from pedido group by idcliente having sum(valor) > 500;		-- Faz agrupamento permitindo condições.


-- Exercícios – funções agregadas

-- 1. A média dos valores de vendas dos vendedores que venderam mais que R$ 200,00.
select idvendedor, round(avg(valor),2) from pedido group by idvendedor;

-- 2. Os vendedores que venderam mais que R$ 1500,00.
select idvendedor, sum(valor) from pedido group by idvendedor having sum(valor) > 1500;

-- 3. O somatório das vendas de cada vendedor.
select idvendedor, sum(valor) from pedido group by idvendedor;

-- 4. A quantidade de municípios.
select count(idmunicipio) from municipio;

-- 5. A quantidade de municípios que são do Paraná ou de Santa Catarina.
select count(idmunicipio) from municipio where iduf = 1 or iduf = 2;

-- 6. A quantidade de municípios por estado.
select iduf, count(idmunicipio) from municipio group by iduf;

-- 7. A quantidade de clientes que informaram o logradouro.
select count(idcliente) from cliente group by logradouro is not null; 

-- 8. A quantidade de clientes por município.
select idmunicipio, count(idcliente) from cliente group by idmunicipio;

-- 9. A quantidade de fornecedores.
select count(idfornecedor) from fornecedor;

-- 10. A quantidade de produtos por fornecedor.
select idfornecedor, count(idproduto) from produto group by idfornecedor;

-- 11. A média de preços dos produtos do fornecedor Cap. Computadores.
select round(avg(valor), 2) from produto where idfornecedor = 1;

-- 12. O somatório dos preços de todos os produtos.
select sum(valor) from produto;

-- 13. O nome do produto e o preço somente do produto mais caro.
select nome, valor from produto order by valor desc limit 1;

-- 14. O nome do produto e o preço somente do produto mais barato.
select nome, valor  from produto order by valor asc limit 1;

-- 15. A média de preço de todos os produtos.
select round(avg(valor), 2) from produto;

-- 16. A quantidade de transportadoras.
select count(idtransportadora) from transportadora;

-- 17. A média do valor de todos os pedidos.
select round(avg(valor), 2) from pedido;

-- 18. O somatório do valor do pedido agrupado por cliente.
select idcliente, sum(valor) from pedido group by idcliente;

-- 19. O somatório do valor do pedido agrupado por vendedor.
select idvendedor, sum(valor) from pedido group by idvendedor;

-- 20. O somatório do valor do pedido agrupado por transportadora.
select idtransportadora, sum(valor) from pedido group by idtransportadora;

-- 21. O somatório do valor do pedido agrupado pela data.
select data_pedido, sum(valor) from pedido group by data_pedido;

-- 22. O somatório do valor do pedido agrupado por cliente, vendedor e transportadora.
select idcliente, idvendedor, idtransportadora, sum(valor) from pedido group by idcliente, idvendedor, idtransportadora;

-- 23. O somatório do valor do pedido que esteja entre 01/04/2008 e 10/12/2009 e que seja maior que R$ 200,00.
select sum(valor) from pedido where data_pedido between '2008-04-01' and '2009-12-10' and valor > 200;

-- 24. A média do valor do pedido do vendedor André.
select round(avg(valor), 2) from pedido where idvendedor = 1;

-- 25. A média do valor do pedido da cliente Jéssica.
select round(avg(valor), 2) from pedido where idcliente = 15;

-- 26. A quantidade de pedidos transportados pela transportadora BS. Transportes.
select count(idpedido) from pedido where idtransportadora = 2;

-- 27. A quantidade de pedidos agrupados por vendedor.
select idvendedor, count(idpedido) from pedido group by idvendedor;

-- 28. A quantidade de pedidos agrupados por cliente.
select idcliente, count(idpedido) from pedido group by idcliente;

-- 29. A quantidade de pedidos entre 15/04/2008 e 25/04/2008.
select count(idpedido) from pedido where data_pedido between '2008-04-15' and '2008-04-25';

-- 30. A quantidade de pedidos que o valor seja maior que R$ 1.000,00.
select count(idpedido) from pedido where valor > 1000;

-- 31. A quantidade de microcomputadores vendida.
select count(idproduto) from pedido_produto where idproduto = 1;

-- 32. A quantidade de produtos vendida agrupado por produto.
select idproduto, count(idproduto) from pedido_produto group by idproduto;

-- 33. O somatório do valor dos produtos dos pedidos, agrupado por pedido.
select idpedido, sum(valor_unitario) from pedido_produto group by idpedido;

-- 34. A quantidade de produtos agrupados por pedido.
select idpedido, count(idproduto) from pedido_produto group by idpedido;

-- 35. O somatório dos valores unitários de todos os produtos.
select sum(valor_unitario) from pedido_produto;

-- 36. A média dos produtos do pedido 6.
select round(avg(valor_unitario), 2) from pedido_produto where idpedido = 6;

-- 37. O valor do maior produto do pedido.
select max(valor_unitario) from pedido_produto;

-- 38. O valor do menor produto do pedido.
select min(valor_unitario) from pedido_produto;

-- 39. O somatório da quantidade de produtos por pedido.
select idpedido, sum(quantidade) from pedido_produto group by idpedido;

-- 40. O somatório da quantidade de todos os produtos do pedido.
select sum(quantidade) from pedido_produto;


-- Relacionamentos com joins

select
	cliente.nome,
	profissaidprofissao
from 
	cliente
left outer join
	profissao on cliente.idprofissao = profissao.idprofissao;

select
	cln.nome,
	prf.nome
from 
	cliente as cln
inner join
	profissao as prf on cln.idprofissao = prf.idprofissao;

select
	cln.nome,
	prf.nome
from 
	cliente as cln
right outer join
	profissao as prf on cln.idprofissao = prf.idprofissao;


-- Exercícios – joins

-- 1. O nome do cliente, a profissão, a nacionalidade, o logradouro, o número, o complemento, o bairro, o município e a unidade de federação.

select 
	cln.nome as cliente,
	prf.nome as profissao,
	ncl.nome as nacionalidade,
	cln.logradouro,
	cln.numero,
	cmp.nome as complemento,
	brr.nome as bairro,
	mnc.nome as municipio,
	uf.nome as estado, 
	uf.sigla as sigla
from
	cliente as cln
left outer join
	profissao as prf on cln.idprofissao = prf.idprofissao
left outer join
	nacionalidade ncl on cln.idnacionalidade = ncl.idnacionalidade
left outer join
	complemento cmp on cln.idcomplemento = cmp.idcomplemento
left outer join
	bairro brr on cln.idbairro = brr.idbairro
left outer join
	municipio mnc on cln.idmunicipio = mnc.idmunicipio
left outer join
	uf on mnc.iduf = uf.iduf


-- 2. O nome do produto, o valor e o nome do fornecedor.

select
	prd.nome as produto,
	prd.valor,
	fnc.nome as fornecedor
from
	produto prd
left outer join
	fornecedor fnc on prd.idfornecedor = fnc.idfornecedor


-- 3. O nome da transportadora e o município.

select 
	tpt.nome as transportadora,
	mnc.nome
from
	transportadora tpt
left outer join
	municipio mnc on tpt.idmunicipio = mnc.idmunicipio


-- 4. A data do pedido, o valor, o nome do cliente, o nome da transportadora e o nome do vendedor.

select
	pdd.data_pedido as pedido,
	cln.nome as cliente,
	tpt.nome as transportadora,
	vdr.nome as vendedor
from
	pedido pdd
left outer join
	cliente cln on pdd.idcliente = cln.idcliente
left outer join
	transportadora tpt on pdd.idtransportadora = tpt.idtransportadora
left outer join
	vendedor vdr on pdd.idvendedor = vdr.idvendedor


-- 5. O nome do produto, a quantidade e o valor unitário dos produtos do pedido.

select
	pdt.nome as produto,
	pdp.quantidade,
	pdp.valor_unitario
from
	pedido_produto pdp
left outer join
	produto pdt on pdp.idproduto = pdt.idproduto


-- 6. O nome dos clientes e a data do pedido dos clientes que fizeram algum pedido (ordenado pelo nome do cliente).

select
	cln.nome,
	pdd.data_pedido
from
	cliente cln
right outer join
	pedido pdd on cln.idcliente = pdd.idcliente
order by 
	cln.nome asc
	

-- 7. O nome dos clientes e a data do pedido de todos os clientes, independente se tenham feito pedido (ordenado pelo nome do cliente).

select
	cln.nome,
	pdd.data_pedido
from
	cliente cln
left outer join
	pedido pdd on cln.idcliente = pdd.idcliente
order by
	cln.nome asc


-- 8. O nome da cidade e a quantidade de clientes que moram naquela cidade.

select
	idmunicipio,
	count(idcliente)	
from
	cliente
group by
	idmunicipio

	
-- 9. O nome do fornecedor e a quantidade de produtos de cada fornecedor.

select
	idfornecedor,
	count(idfornecedor)
from
	produto
group by
	idfornecedor


-- 9. 10.O nome do cliente e o somatório do valor do pedido (agrupado por cliente).

select
	cln.nome as cliente,
	sum(pdd.valor) as total
from
	pedido pdd
left outer join
	cliente cln on cln.idcliente = pdd.idcliente
group by
	cln.idcliente

	
-- 11.O nome do vendedor e o somatório do valor do pedido (agrupado por vendedor).


select
	vdr.nome as vendedor,
	sum(pdd.valor) as total
from
	pedido pdd
left outer join
	vendedor vdr on vdr.idvendedor = pdd.idvendedor
group by
	vdr.idvendedor


-- 12.O nome da transportadora e o somatório do valor do pedido (agrupado por transportadora).

select
	tpt.nome as transportadora,
	sum(pdd.valor)
from
	pedido pdd
inner join
	transportadora tpt on tpt.idtransportadora = pdd.idtransportadora
group by
	tpt.idtransportador


-- 13.O nome do cliente e a quantidade de pedidos de cada um (agrupado por cliente).

select
	cln.nome as cliente,
	count(pdd.idpedido)
from
	pedido pdd
left outer join
	cliente cln on cln.idcliente = pdd.idcliente
group by
	cln.idcliente


-- 14.O nome do produto e a quantidade vendida (agrupado por produto).

select
	pdt.nome as produto,
	count(pdd.idpedido)
from
	pedido pdd
left outer join
	produto pdt on pdt.idproduto = pdt.idproduto
group by
	pdt.idproduto


-- 15.A data do pedido e o somatório do valor dos produtos do pedido (agrupado pela data do pedido).
	
select
	pdd.data_pedido,
	sum(pdp.valor_unitario) as total 
from
	pedido_produto pdp
left outer join
	pedido pdd on pdp.idpedido = pdp.idpedido
group by
	pdd.data_pedido


-- 16.A data do pedido e a quantidade de produtos do pedido (agrupado pela data do pedido).

select
	pdt.data_pedido,
	sum(pdp.quantidade) as total
from
	pedido_produto pdp
left outer join
	pedido pdt on pdt.idpedido = pdp.idpedido
group by
	pdt.data_pedido


--


-- Comandos adicionais
select * from pedido;
select 
	data_pedido,
	extract (day from data_pedido),
	extract (month from data_pedido),
	extract (year from data_pedido)
from 
	pedido;

--

select
	nome, substring(nome from 1 for 5) from cliente		-- Retorna apenas as primeiras 5 letras do nome do cliente.

select nome, upper(nome) from cliente		-- Retorna o nome dos clientes em Caps Lock.

select nome, cpf, coalesce(cpf, 'Não informado') from cliente		-- Caso o "CPF" não tenha sido informado retorna a frase "Não informado".

select
	case sigla 
		when 'PR' then 'Paraná'
		when 'SC' then 'Santa Catarina'
	else 'Outros'
	end as uf
from
	uf


-- Exercícios – comandos adicionais

-- 1. O nome do cliente e somente o mês de nascimento. Caso a data de nascimento não esteja preenchida mostrar a mensagem “Não informado”.

select
	nome,
	coalesce(extract(month from data_nascimento), 0)
from
	cliente


-- 2. O nome do cliente e somente o nome do mês de nascimento (Janeiro, Fevereiro etc). Caso a data de nascimento não esteja preenchida mostrar a mensagem “Não informado”.

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
	else 'Não informado'
	end as mes
from
	cliente


-- 3. O nome do cliente e somente o ano de nascimento. Caso a data de nascimento não esteja preenchida mostrar a mensagem “Não informado”.

select
	nome,
	coalesce(extract(year from data_nascimento), 0)
from 
	cliente


-- 4. O caractere 5 até o caractere 10 de todos os municípios.

select
	nome, substring(nome from 5 for 10) from municipio


-- 5. O nome de todos os municípios em letras maiúsculas.

select
	upper(nome) from municipio


-- 6. O nome do cliente e o gênero. Caso seja M mostrar “Masculino”, senão mostrar “Feminino”.

select 
	nome,
	case genero
		when 'M' then 'Masculino'
		when 'F' then 'Feminino'
	end as genero
from
	cliente


-- 7. O nome do produto e o valor. Caso o valor seja maior do que R$ 500,00 mostrar a mensagem “Acima de 500”, caso contrário, mostrar a mensagem “Abaixo de 500”.

select 
	nome,
	case
		when valor >= 500 then 'Acima ou igual a 500'
	else 
		'Abaixo de 500'
	end as valor
from
	produto


-- Subconsultas

-- Seleciona a data do pedido e o valor onde o valor seja maior que a média dos valores de todos os pedidos

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


-- Exemplo com update

select * from pedido

update pedido set valor = valor + ((valor * 5) / 100)
where valor > (select avg(valor) from pedido) 


-- 1. O nome dos clientes que moram na mesma cidade do Manoel. Não deve ser mostrado o Manoel.
select
	nome,
	idmunicipio
from
	cliente
where 
	idmunicipio = (select idmunicipio from cliente where nome = 'Manoel')
and
	idcliente <> 1


-- 2. A data e o valor dos pedidos que o valor do pedido seja menor que a média de todos os pedidos.

select
	data_pedido
	valor
from
	pedido
where 
	valor < (select avg(valor) from pedido)


-- 3. A data, o valor, o cliente e o vendedor dos pedidos que possuem 2 ou mais produtos.

select
	pdd.data_pedido,
	pdd.valor,
	cln.nome as cliente,
	vdr.nome as vendedor,
	(select sum(quantidade) from pedido_produto pdp where pdp.idpedido = pdd.idpedido)
from
	pedido pdd
left outer join
	cliente cln on cln.idcliente = pdd.idcliente
left outer join
	vendedor vdr on vdr.idvendedor = pdd.idvendedor
where
	(select sum(quantidade) from pedido_produto pdp where pdp.idpedido = pdd.idpedido) >= 2


-- 4. O nome dos clientes que moram na mesma cidade da transportadora BSTransportes.

select 
	nome,
	idmunicipio
from
	cliente
where
	idmunicipio = (select idmunicipio from transportadora where idtransportadora = 1)


-- 5. O nome do cliente e o município dos clientes que estão localizados no mesmo município de qualquer uma das transportadoras.

select
	nome,
	idmunicipio
from
	cliente
where
	idmunicipio in (select idmunicipio from transportadora)


-- 6. Atualizar o valor do pedido em 5% para os pedidos que o somatório do valor total dos produtos daquele pedido seja maior que a média do valor total

update
	pedido
set 

select 
	valor + ((valor * 5) / 100)
from
	pedido
where 
	(select sum(valor_unitario) from pedido_produto pdp where pdp.idpedido = idpedido) > (select avg(valor_unitario) from pedido_produto pdp where pdp.idpedido = idpedido)

select
	idpedido,
	(select sum(valor_unitario) from pedido_produto pdp where pdp.idpedido = pdd.idpedido)
from
	pedido pdd


-- 7. O nome do cliente e a quantidade de pedidos feitos pelo cliente.

select
	cln.nome,
	(select count(idpedido) from pedido pdd where pdd.idcliente = cln.idcliente)
from
	cliente cln
	

-- 8. Para revisar, refaça o exercício anterior (número 07) utilizando group by e mostrando somente os clientes que fizeram pelo menos um pedido.

select
	cln.nome as cliente,
	count(pdd.idpedido) as total
from
	pedido pdd
left outer join
	cliente cln on pdd.idcliente = cln.idcliente
group by
	cln.nome


-- Views

drop view cliente_profissao		-- Apaga a "View"

create view cliente_profissao as 
select
	cln.nome as cliente,
	cln.cpf,
	prf.nome as profissao
from
	cliente cln
left outer join
	profissao prf on cln.idprofissao = prf.idprofissao

select cliente from cliente_profissao where profissao = 'Professor'		-- Retorna os clientes que são da profissão "Professor".
select * from cliente_profissao


-- Exercícios views

-- 1. O nome, a profissão, a nacionalidade, o complemento, o município, a unidade de federação, o bairro, o CPF,o RG,
-- a data de nascimento, o gênero (mostrar “Masculino” ou “Feminino”), o logradouro, o número e as observações dos clientes.
create view cliente_dados as
select
	cln.nome as cliente,
	prf.nome as profissao,
	ncn.nome as nacionalidade,
	cmp.nome as complemento,
	mnc.nome as municipio,
	uf.nome as uf,
	brr.nome as bairro,
	cln.cpf,
	cln.rg,
	cln.data_nascimento,
	cln.logradouro,
	cln.numero,
	cln.observacoes,
	case cln.genero
		when 'M' then 'Masculino'
		when 'F' then 'Feminino'
	end as genero
from
	cliente cln
left outer join
	profissao prf on cln.idprofissao = prf.idprofissao
left outer join
	nacionalidade ncn on cln.idnacionalidade = ncn.idnacionalidade
left outer join
	complemento cmp on cln.idcomplemento = cmp.idcomplemento
left outer join
	municipio mnc on cln.idmunicipio = mnc.idmunicipio
left outer join
	uf on mnc.iduf = uf.iduf
left outer join
	bairro brr on cln.idbairro = brr.idbairro

select * from cliente_dados

-- 2. O nome do município e o nome e a sigla da unidade da federação.
create view municipio_uf as
select
	mnc.nome as municipio,
	uf.nome as unidade_federacao,
	uf.sigla as uf
from
	municipio mnc
left outer join
	uf on mnc.iduf = uf.iduf


-- 3. O nome do produto, o valor e o nome do fornecedor dos produtos.
create view produto_fornecedor as
select 
	pdt.nome as produto,
	pdt.valor,
	fnc.nome as fornecedor
from
	produto pdt
left outer join
	fornecedor fnc on pdt.idfornecedor = fnc.idfornecedor

select * from municipio_uf

-- 4. O nome da transportadora, o logradouro, o número, o nome da unidade de federação e a sigla da unidade de federação das transportadoras.
create view transportadora_uf as
select
	tpt.nome as transportadora,
	tpt.logradouro,
	tpt.numero,
	uf.nome as uf,
	uf.sigla
from
	transportadora tpt
left outer join
	municipio mnc on tpt.idmunicipio = mnc.idmunicipio
left outer join
	uf on mnc.iduf = uf.iduf

select * from transportadora_uf

-- 5. A data do pedido, o valor, o nome da transportadora, o nome do cliente e o nome do vendedor dos pedidos.
create view dados_pedido as
select
	pdd.data_pedido as pedido,
	pdd.valor,
	tpt.nome as transportadora,
	cln.nome as cliente,
	vdr.nome as vendedor
from
	pedido pdd
left outer join
	transportadora tpt on pdd.idtransportadora = tpt.idtransportadora
left outer join
	cliente cln on pdd.idcliente = cln.idcliente
left outer join
	vendedor vdr on pdd.idvendedor = vdr.idvendedor


-- 6. O nome do produto, a quantidade, o valor unitário e o valor total dos produtos do pedido.
create view produto_pedido as
select
	pdp.idpedido,
	string_agg(prd.nome, ', ') as produtos,		-- Agrupa os nomes dos produtos em uma unica string
	sum(pdp.quantidade * pdp.valor_unitario) as valor_total		-- Calcula o valor total do pedido
from
	pedido_produto pdp
left outer join
	produto prd on pdp.idproduto = prd.idproduto
group by
	pdp.idpedido;		-- Agrupa por idpedido para calcular o valor total por pedido ate view produto_pedido as
	
select * from produto_pedido


-- Autoincremento

create table exemplo (
	idexemplo serial not null,
	nome varchar(50) not null,

	constraint pk_exemplo_idexemplo primary key (idexemplo)
);

insert into exemplo (nome) values ('Exemplo 1');
insert into exemplo (nome) values ('Exemplo 2');
insert into exemplo (nome) values ('Exemplo 3');
insert into exemplo (nome) values ('Exemplo 4');
insert into exemplo (nome) values ('Exemplo 5');

select * from exemplo

select max(idbairro) + 1 from bairro
create sequence bairro_id_seq minvalue 5
alter table bairro alter idbairro set default nextval('bairro_id_seq') 
alter sequence bairro_id_seq owned by bairro.idbairro
insert into bairro (nome) values ('Teste 1');
insert into bairro (nome) values ('Teste 2');
select * from bairro


-- Exercícios sequences – auto incremento

-- 1. Criar sequências para todas as outras tabelas da base de dados
-- a. Cliente

select max(idcliente) + 1 from cliente
create sequence cliente_id_seq minvalue 18
alter table cliente alter idcliente set default nextval('cliente_id_seq')
alter sequence cliente_id_seq owned by cliente.idcliente

-- b. Complemento

select max(idcomplemento) + 1 from complemento
create sequence complemento_id_seq minvalue 3
alter table complemento alter idcomplemento set default nextval('complemento_id_seq')
alter sequence complemento_id_seq owned by complemento.idcomplemento

-- c. Fornecedor

select max(idfornecedor) + 1 from fornecedor
create sequence fornecedor_id_seq minvalue 4
alter table fornecedor alter idfornecedor set default nextval('fornecedor_id_seq')
alter sequence fornecedor_id_seq owned by fornecedor.idfornecedor

-- d. Município

select max(idmunicipio) + 1 from municipio
create sequence municipio_id_seq minvalue 10
alter table municipio alter idmunicipio set default nextval('municipio_id_seq')
alter sequence municipio_id_seq owned by municipio.idmunicipio

-- e. Nacionalidade

select max(idnacionalidade) + 1 from nacionalidade
create sequence nacionalidade_id_seq minvalue 5
alter table nacionalidade alter idnacionalidade set default nextval('nacionalidade_id_seq')
alter sequence nacionalidade_id_seq owned by nacionalidade.idnacionalidade

-- f. Pedido

select max(idpedido) + 1 from pedido
create sequence pedido_id_seq minvalue 16
alter table pedido alter idpedido set default nextval('pedido_id_seq')
alter sequence pedido_id_seq owned by pedido.idpedido

-- g. Pedido produto

-- (Não é necessário)

-- h. Profissão

select max(idprofissao) + 1 from profissao
create sequence profissao_id_seq minvalue 6
alter table profissao alter idprofissao set default nextval('profissao_id_seq')
alter sequence profissao_id_seq owned by profissao.idprofissao

-- i. Transportadora

select max(idtransportadora) + 1 from transportadora
create sequence transportadora_id_seq minvalue 3
alter table transportadora alter idtransportadora set default nextval('transportadora_id_seq')
alter sequence transportadora_id_seq owned by transportadora.idtransportadora 

-- j. UF
select max(iduf) + 1 from uf
create sequence uf_id_seq minvalue 7
alter table uf alter iduf set default nextval('uf_id_seq')
alter sequence uf_id_seq owned by uf.iduf

-- k. Vendedor

select max(idvendedor) + 1 from vendedor
create sequence vendedor_id_seq minvalue 9
alter table vendedor alter idvendedor set default nextval('vendedor_id_seq')
alter sequence vendedor_id_seq owned by vendedor.idvendedor


-- l. Produto

select max(idproduto) + 1 from produto
create sequence produto_id_seq minvalue 8
alter table produto alter idproduto set default nextval('produto_id_seq')
alter sequence produto_id_seq owned by produto.idproduto


-- Campos default
alter table pedido alter column data_pedido set default current_date;
alter table pedido alter column valor set default 0;
insert into pedido (idcliente, idvendedor) values (1, 1):
insert into pedido (idcliente, idvendedor, dta_pedido, valor)
values (1, 1, '2022-10-10', 234);

select * from pedido


-- Exercícios valores default

-- 1. Adicione valores default na tabela de produtos do pedido
	-- a. Quantidade com o valor 1
	-- b. Valor unitário com o valor 0
alter table pedido_produto alter column quantidade set default 1;
alter table pedido_produto alter column valor_unitario set default 0;

insert into pedido_produto (idpedido, idproduto) values (1, 3);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values(1, 4, 5, 100)
select * from pedido_produto

-- 2. Adicione valor default na tabela de produtos
	-- a. Valor com o valor 0
alter table produto alter column valor set default 0;
insert into produto (nome) values ('Teste default 1')


-- Índices
create index idx_cln_nome on cliente (nome);


-- Exercícios índices

-- 1. Adicione índices nas seguintes tabelas e campos
	-- a. Pedido – data do pedido
	-- b. Produto – nome
create index idx_pdd_data_pedido on pedido (data_pedido);
create index idx_pdt_nome on produto (nome);