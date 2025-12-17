create table cliente (
    idcliente integer not null,
    nome varchar(50) not null, -- pedro 5, 45
	cpf char(11),
	rg varchar(15),
    data_nascimento date,
	genero char(1),
	profissao varchar(30),
	nascionalidade varchar(30),
	logradouro varchar(30),
	numero varchar (10),
	complemento varchar(30),
	bairro varchar(30),
	municipio varchar(30),
	uf varchar(30),
	observacoes text,

	--primary key 
	constraint pk_cln_idcliente primary key (idcliente)
);

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nascionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (2, 'gerald', '88828383821', '32323', '2001-01-30', 'M', 'estudante', 'brasileira', 'rua joaquim nabuco', '23', 'casa', 'cidade nova', 'porto unuão', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nascionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (3, 'carlos', '87732323227', '55463', '01/10/1967', 'M', 'pedreiro', 'brasileira', 'rua das laranjeiras', '200', 'ap.', 'centro', 'p. união', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nascionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (4, 'adriana', '12321222122', '98777', '10/09/1989', 'f', 'jornalista', 'brasileira', 'rua das ', '200', 'ap.', 'centro', 'p. união', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nascionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (5, 'amanda', '99982838828', '28382', '04/03/1991', 'f', 'jorn.', 'italiana', 'av. central', '100', null, 'são pedro', 'general cameiro', 'pr');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nascionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (6, 'ãgelo', '99982828181', '12323', '01/01/2000', 'm', 'professor', 'brasileiro', 'av. beira mar', '300', null, 'ctr.', 'são paulo', 'sp');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nascionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (7, 'anderson', null, null, null, 'm', 'prof.', 'italiano', 'av. brasil', '100', 'apartamento', 'santa rosa', 'rio de janeiro', 'sp');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nascionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (8, 'camila', '9998282828', null, '10/10/2001', 'f', 'professora', 'norte americana', 'rua central', '4333', null, 'centro', 'rio de janeiro', 'sp');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nascionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (9, 'cristiano', null, null, null, 'm', 'estudante', 'alemã', 'rua do centro', '877', 'casa', 'centro', 'porto alegre', 'sp');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nascionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (10, 'fabrício', '8828282828', '32323', null, 'm', 'estudante', 'brasileiro', null, null, null, null, 'pu', 'sc');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nascionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (11, 'fernanda', null, null, null, 'f', null, 'brasileira', null, null, null, null, 'porto união', 'sc');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nascionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (12, 'gilmar', '88881818181', '888', '10/02/2000', 'm', 'estud.', null, 'rua das laranjeiras', '200', null, 'c. nova', 'coroinhas', 'sc');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nascionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (13, 'diego', '1010191919', '111939', null, 'm', 'professor', 'alemão', 'rua central', '455', 'casa', 'cidade n.' , 'são paulo', 'sp');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nascionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (14, 'jeferson', null, null, '01/07/1983', 'm', null, 'brasileiro',	 null, null, null, null, 'união da vitoria', 'pr');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nascionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (15, 'jesica', null, null, null, 'f', 'estudante', null, null, null, null, null, 'união da vitoria', 'pr');

select * from client;

select nome, data_nascimento from cliente;

select nome, data_nascimento as "data de nascimento" from cliente;

select ' CPF: ' || cpf || ' RG: ' || rg as "CPF e RG" from cliente;

select * from cliente limit 3;

select nome, data_nascimento from cliente where data_nascimento > '2000-01-01';

select nome from cliente where nome like 'c%';

select nome from cliente where nome like '%c%';

select nome, data_nascimento from cliente where data_nascimento between '1990-01-01' and '1998-01-01';

select nome, rg from cliente where rg is null;

select nome from cliente order by nome asc;

select nome from cliente order by nome desc;

select nome, genero, profissao from cliente order by nome desc;

select nome from cliente where nome like '%r%';

select nome from cliente where nome like 'c%';

select nome from cliente where nome like '%a';

select nome, bairro from cliente where bairro = 'centro' or bairro = 'Cto.' or bairro = 'Ctr.';

select nome, complemento from cliente where complemento like 'a%';

select nome, genero from cliente where genero like 'f';

select nome, profissao from cliente order by profissao;

select nome, nascionalidade from cliente where nascionalidade like 'brasil%'; 

select nome, numero from cliente where numero is not null;

select nome, uf from  cliente where uf like 'sc';

select nome, data_nascimento from cliente where data_nascimento between '2000-01-01' and '2002-01-01';

select nome || ' - ' || logradouro || ' - ' || numero || ' - ' || complemento || ' - ' || bairro || ' - ' || municipio || ' - ' || uf from cliente;

select * from cliente;
update cliente set nome = 'teste' where idcliente = 1;
update cliente set nome = 'adriano', genero =  'm', numero = '241' where idcliente = 4;
insert into cliente (idcliente,nome) values (16, 'joão');
delete from cliente where idcliente = 16;

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, municipio, uf)
values (16, 'maicon', '12349596421', '1234', '1965-10-10', 'f', 'empresário', 'florianópolis', 'PR');

insert into cliente (idcliente, nome, rg, genero, profissao, nascionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (17, 'getúlio', '4631', 'f', 'estudante', 'brasileira', 'rua central', '343', 'apartamento', 'centro', 'curitiba', 'SC');

insert into cliente (idcliente, nome, genero, profissao, nascionalidade, numero, complemento)
values (18,'sandra', 'm', 'professor', 'italiana', '12', 'bloco a');

select * from cliente
update cliente set cpf = '45390569432', genero = 'm', nascionalidade = 'brasileira', uf = 'sc' where idcliente = 16

update cliente set data_nascimento = '1978-04-01', genero = 'm' where idcliente = 17;

update cliente set genero = 'f', profissao = 'professora', numero = '123' where idcliente = 18;

delete from cliente where idcliente = 16; 

delete from cliente where idcliente = 18;

create table profissao (
    idprofissao integer not null,
	nome varchar(30) not null,	

	constraint pk_prf_idprofissao primary key (idprofissao),
	constraint un_prf_nome unique (nome)
);

insert into profissao (idprofissao, nome) values (1, 'estudante');
insert into profissao (idprofissao, nome) values (2, 'engenheiro');
insert into profissao (idprofissao, nome) values (3, 'pedreiro');
insert into profissao (idprofissao, nome) values (4, 'jornalista');
insert into profissao (idprofissao, nome) values (5, 'professsor');

select * from profissao;

create table nacionalidade (
    idnacionalidade integer not null,
	nome varchar(30) not null,

	constraint pk_ncn_idnacionalidade primary key (idnacionalidade),
	constraint un_ncn_nome unique (nome)
);

select nascionalidade from cliente;

insert into nacionalidade (idnacionalidade, nome) values (1, 'brasileira');
insert into nacionalidade (idnacionalidade, nome) values (2, 'italiana');
insert into nacionalidade (idnacionalidade, nome) values (3, 'norte-americana');
insert into nacionalidade (idnacionalidade, nome) values (4, 'alemã');

select * from nacionalidade;

create table complemento (
    idcomplemento integer not null,
	nome varchar(30) not null,

	CONSTRAINT pk_cpl_idcomplemento primary key (idcomplemento),
	constraint un_cpl_nome unique (nome)
);

insert into complemento (idcomplemento, nome) values (1, 'casa');
insert into complemento (idcomplemento, nome) values (2, 'apartamento')

select * from complemento;

create table bairro (
    idbairro integer not null,
	nome varchar (30) not null,

	constraint pk_brr_idbairro primary key (idbairro),
	constraint un_brr_nome unique (nome)
);

insert into bairro (idbairro, nome) values (1, 'cidade nova');
insert into bairro (idbairro, nome) values (2, 'centro');
insert into bairro (idbairro, nome) values (3, 'sao pedro');
insert into bairro (idbairro, nome) values (4, 'santa rosa');

select *from bairro 

select * from cliente;

alter table cliente rename column profissao to idprofissao;
alter table cliente alter column idprofissao type integer;

alter table cliente drop idprofissao;
alter table cliente add idprofissao integer;
alter table cliente add constraint fk_cln_idprofissao foreign key (idprofissao) references profissao (idprofissao);

update cliente set idprofissao = 1 where idcliente in (1, 9, 10, 12, 15, 17);
update cliente set idprofissao = 2 where idcliente = 2;
update cliente set idprofissao = 3 where idcliente = 3;
update cliente set idprofissao = 4 where idcliente in (4, 5);
update cliente set idprofissao = 5 where idcliente in (6, 7, 8, 13);

select * from profissao
delete from profissao where idprofissao = 10;
insert into profissao (idprofissao, nome) values (10, 'teste');

select * from cliente;
alter table cliente drop nascionalida;
alter table cliente add idnacionalidade integer;
alter table cliente add constraint fk_cln_idnacionalidade foreign key (idnacionalidade) references nacionalidade (idnacionalidade);
select * from nacionalidade
update cliente set idnacionalidade = 1 where idcliente in (1,2,3,4,6,10,11,14);
update cliente set id nacionalidade = 2 where idcliente in (5,7);
update cliente set id nacionalidade = 3 where idclient
update cliente set idnacionalidade = 4 where idcliente  in (9,13);

select * from cliente;
alter table cliente drop complemento;
alter table cliente add idcomplemento integer;
alter table cliente add constraint fk_cln_idcomplemento foreign key (idcomplemento) references complemento (idcomplemento);
select * from complemento 
update cliente set idcomplemento = 1 where idcliente in (1,4,9,13);
update cliente set idcomplemento = 2 where idcliente in (2,3,7);

select * from cliente 

alter table cliente drop bairro;
alter table cliente add idbairro integer;
alter table cliente add constraint fk_cln_idbairro foreign key (idbairro) references bairro (idbairro);

select * from bairro 
update cliente set idbairro = 1 where idcliente in (1, 12, 13);
update cliente set idbairro = 2 where idcliente in (3, 3, 6, 8, 9);
update cliente set idbairro = 3 where idcliente in (4,5);
update cliente set idbairro = 4 where idcliente = 7;

select * from cliente 
create table uf (
    iduf integer not null,
	nome varchar(30) not null,
	sigla char(2) not null,

	constraint pk_ufd_idunidade_federecao primary key (iduf), 
	constraint un_ufd_nome unique (nome),
	constraint un_ufd_sigla unique (sigla)
);

insert into uf (iduf, nome, sigla) values (1, 'santa catarina','sc');
insert into uf (iduf, nome, sigla) values (2, 'parana','pr');
insert into uf (iduf, nome, sigla) values (3, 'são paulo','sp');
insert into uf (iduf, nome, sigla) values (4, 'minas gerais','mg');
insert into uf (iduf, nome, sigla) values (5, 'rio grande do sul','rs');
insert into uf (iduf, nome, sigla) values (6, 'rio de janeiro','rj');
select * from uf

create table municipio (
    idmunicipio integer not null,
	nome varchar(30) not null,
	iduf integer not null,

	constraint pk_mnc_idmunicipio primary key (idmunicipio),
	constraint un_mnc_nome unique (nome),
	constraint fk_mnc_iduf foreign key (iduf) references uf (iduf)	
);

insert into municipio (idmunicipio, nome, iduf) values (1, 'porto união', 1);
insert into municipio (idmunicipio, nome, iduf) values (2, 'canoinhas', 1);
insert into municipio (idmunicipio, nome, iduf) values (3, 'porto vitoria', 2);
insert into municipio (idmunicipio, nome, iduf) values (4, 'general carneiro', 2);
insert into municipio (idmunicipio, nome, iduf) values (5, 'são paulo', 3);
insert into municipio (idmunicipio, nome, iduf) values (6, 'rio de janeiro', 6);
insert into municipio (idmunicipio, nome, iduf) values (7, 'uberlâdia', 4);
insert into municipio (idmunicipio, nome, iduf) values (8, 'porto alegre ', 5);
insert into municipio (idmunicipio, nome, iduf) values (9, 'união vitoria', 2);
select * from municipio

select * from cliente
alter table cliente drop municipio;
alter table cliente drop uf;
alter table cliente add idmunicipio integer;
alter table cliente add constraint fk_cliente_idmunicipio foreign key (idmunicipio) references municipio (idmunicipio)

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

create table fornecedor (
    idfornecedor integer not null,
	nome varchar(50) not null,

	constraint pk_frn_idfornecedor primary key (idfornecedor),
	constraint un_frn_nome unique (nome)
);

insert into fornecedor (idfornecedor, nome) values (1, 'cap. computadores'); 
insert into fornecedor (idfornecedor, nome) values (2, 'AA. computadores');
insert into fornecedor (idfornecedor, nome) values (3, 'BB. maquinás');
select * from fornecedor

create table vendedor (
    idvendedor integer not null,
	nome varchar(50) not null,

	constraint pk_vnd_idvendedor primary key (idvendedor),
	constraint un_vnd_nome unique (nome)
);

insert into vendedor (idvendedor, nome) values (1, 'andré');
insert into vendedor (idvendedor, nome) values (2, 'alisson');
insert into vendedor (idvendedor, nome) values (3, 'josé');
insert into vendedor (idvendedor, nome) values (4, 'ailton');
insert into vendedor (idvendedor, nome) values (5, 'maria');
insert into vendedor (idvendedor, nome) values (6, 'suelem');
insert into vendedor (idvendedor, nome) values (7, 'aline');
insert into vendedor (idvendedor, nome) values (8, 'silvana');
select * from vendedor

create table transportadora (
    idtransportadora integer not null,
	idmunicipio integer,
	nome varchar(50) not null,
	logradouro varchar(50),
	numero varchar(10),

	constraint pk_trn_idtransportadora primary key (idtransportadora),
	constraint fk_trn_idmunicipio foreign key (idmunicipio) references municipio (idmunicipio),
	constraint un_trn_nome unique (nome)
);

select * from municipio

insert into transportadora (idtransportadora, idmunicipio, nome, logradouro, numero)
values(1, 9, 'BS. transportes', 'rua das limas', '01')
insert into transportadora (idtransportadora, idmunicipio, nome)
values(2, 5, 'união transportes')
select * from transportadora 

create table produto(
    idproduto integer not null,
	idfornecedor integer not null,
	nome varchar(50) not null,
	valor float not null,
	
	constraint pk_prd_idproduto primary key (idproduto),
	constraint fk_prd_idfornecedor foreign key (idfornecedor) references fornecedor (idfornecedor)
);

select * from fornecedor

insert into produto (idproduto, idfornecedor, nome, valor)
values (1, 1, 'microcomputador', 800);
insert into produto (idproduto, idfornecedor, nome, valor)
values (2, 1, 'monitor', 500);
insert into produto (idproduto, idfornecedor, nome, valor)
values (3, 2, 'placa mãe', 200);
insert into produto (idproduto, idfornecedor, nome, valor)
values (4, 2, 'HD', 150);
insert into produto (idproduto, idfornecedor, nome, valor)
values (5, 2, 'placa de video', 200);
insert into produto (idproduto, idfornecedor, nome, valor)
values (6, 3, 'memória ram', 100);
insert into produto (idproduto, idfornecedor, nome, valor)
values (7, 1, 'gabinete', 35);

select * from produto

create table pedido (
    idpedido integer not null,
	idcliente integer not null,
	idtransportadora integer,
	idvendedor integer not null,
	data_pedido date not null,
	valor float not null,

	constraint pk_pdd_idpedido primary key (idpedido),
	constraint fk_pdd_idcliente foreign key (idcliente) references cliente (idcliente),
	constraint fk_pdd_idtransportadora foreign key (idtransportadora) references transportadora (idtransportadora),
	constraint fk_pdd_idvendedora foreign key (idvendedor) references vendedor (idvendedor)
);

select * from cliente
select * from transportadora
select * from vendedor
update cliente set nome = 'Manoel' where idcliente = 1

insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (1, '2008-04-01', 1300, 1, 1, 1);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (2, '2008-04-01', 500, 1, 1, 1);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) 
values (3, '2008-04-02', 300, 11, 2, 5);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) 
values (4, '2008-04-05', 1000, 8, 1, 7);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) 
values (5, '2008-04-06', 200, 9, 2, 6);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) 
values (6, '2008-04-06', 1985, 10, 1, 6);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) 
values (7, '2008-04-06', 800, 3, 1, 7);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (8, '2008-04-06', 175, 3, null, 7);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (9, '2008-04-07', 1300, 12, null, 5);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (10, '2008-04-10', 200, 6, 1, 8);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (11, '2008-04-15', 300, 15, 2, 1);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (12, '2008-04-20', 300, 15, 2, 5);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (13, '2008-04-20', 350, 9, 1, 7);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (14, '2008-04-23', 300, 2, 1, 5);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor)
values (15, '2008-04-25', 200, 11, null, 5);

select * from pedido

create table pedido_produto(
    idpedido integer not null,
	idproduto integer not null,
	quantidade integer not null,
	valor_unitario float not null,

	constraint pk_pdp_idpedidoproduto primary key (idpedido, idproduto),
	constraint fk_pdp_idpedido foreign key (idpedido) references pedido (idpedido),
	constraint fk_pdp_idproduto foreign key (idproduto) references produto (idproduto)
);

select * from produto 
select * from pedido_produto

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(1, 1, 1, 800);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(1, 2, 1, 500);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(2, 2, 1, 500);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(3, 4, 2, 150);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(4, 1, 1, 800);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(4, 3, 1, 200);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(5, 3, 1, 200);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(6, 1, 2, 800);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(6, 7, 1, 35);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(6, 5, 1, 200);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(6, 4, 1, 150);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(7, 1, 1, 800);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(8, 7, 5, 35);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(9, 1, 1, 800);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(8, 2, 1, 500);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(10, 5, 1, 200);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(11, 5, 1, 200);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(11, 6, 1, 100);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(12, 2, 1, 500);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(13, 3, 1, 200);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(13, 4, 1, 150);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(14, 6, 3, 100);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values 
(15, 3, 1, 200);

select nome from vendedor order by nome asc

select nome, valor from produto where valor > 200 order by valor

select nome, valor, valor + (valor * 10) / 100 as reajuste from produto order by nome 

select * from uf
select * from municipio where iduf = 5 

select * from pedido where data_pedido between '2008-04-10' and '2008-04-25' order by valor

select * from pedido where valor between 100 and 500

select * from pedido where valor not between 100 and 500

select * from vendedor
select * from pedido where idvendedor = 1 order by valor desc

select * from cliente
select * from pedido where idcliente = 1 order by valor asc

select * from pedido where idcliente = 15 and idvendedor = 1

select * from transportadora 
select * from pedido where idtransportadora = 2

select * from vendedor 
select * from pedido where idvendedor = 5 or idvendedor = 7

select * from municipio
select * from cliente where idmunicipio = 1 or idmunicipio = 9

select * from cliente where idmunicipio <> 1 and idmunicipio <> 9

select * from cliente where logradouro is null

select * from cliente where logradouro like 'av%'

select * from vendedor where nome like 's%'

select * from vendedor where nome like '%a'

select * from vendedor where nome not like 'a%'

select * from uf 
select * from municipio where nome like 'p%' and iduf = 1 	

select * from transportadora where logradouro is not null

select * from pedido_produto where 	idpedido = 6 or idpedido = 10

select * from pedido_produto where idpedido = 6 or idpedido = 10 

select avg(valor) from pedido 

select count(idmunicipio) from municipio

select count(*) from municipio

select * from transportadoura 
select count(logradouro) from transportadora
select count(idtransportadora) from transportadora

select * from municipio 
select count(idmunicipio) from  municipio where iduf = 2

select max(valor) from pedido

select min(valor), max(valor) from  pedido

select sum(valor) from pedido

select idcliente, valor from pedido

select idcliente, sum(valor) from pedido group by idcliente

select idcliente, sum(valor) from pedido group by idcliente having sum(valor) > 500

select idvendedor, avg(valor) from pedido group by idvendedor having avg(valor) > 200

select idvendedor, sum(valor) from pedido group by idvendedor having sum(valor) > 1500

select idvendedor, sum(valor) from pedido group by idvendedor 

select count(idmunicipio) from municipio

select * from uf
select count(idmunicipio) from municipio where iduf = 1 or iduf = 2

select iduf, count(idmunicipio) from municipio group by iduf

select count(idcliente) from cliente where logradouro is not null

select idmunicipio, count(idcliente) from cliente group by idmunicipio

select count(idfornecedor) from fornecedor 

select idfornecedor, count (idproduto) from produto group by idfornecedor 

select * from fornecedor 
select avg(valor) from produto where idfornecedor = 1

select sum(valor) from produto

select nome, valor from produto order by valor desc limit 1 

select nome, valor from produto order by valor asc limit 1 

select avg(valor) from produto 

select count(idtransportadora) from transportadora 

select avg(valor) frompedido

select idcliente, sum(valor) from pedido group by idcliente 

select idvendedor, sum (valor) from pedido group by idvendedor 

select idtransportadora, sum(valor) from pedido group by idtransportadora 

select data_pedido, sum(valor) from pedido group by data_pedido

select idcliente, idvendedor, sum(valor) from pedido group by idcliente, idvendedor

select sum(valor) from pedido where data_pedido between '2008-04-01' and '2009-12-10' and valor > 200

select avg(valor) from pedido where idvendedor = 1

select avg(valor) from pedido where idvendedor = 15

select count(idpedido) from pedido where idtransportadora = 1

select idvendedor, count(idpedido) from pedido group by idvendedor

select idcliente, count(idpedido) from pedido group by idcliente

select count(idpedido) from pedido where data_pedido between '2008-04-15' and '2008-04-25'

select * from pedido where valor > 1000

select sum(quantidade) from pedido_produto where idproduto = 1

select idproduto, sum(quantidade) from pedido_produto group by idproduto

select idpedido, sum(valor_unitario) from pedido_produto group by idpedido 

select sum(valor_unitario) from pedido_produto

select avg(valor_unitario) from pedido_produto where idpedido = 6 

select max(valor_unitario) from pedido_produto

select min(valor_unitario) from pedido_produto

select idpedido, sum(quantidade) from pedido_produto group by idpedido

select sum(valor_unitario) from pedido_produto

select 
    cln.nome as cliente,
	prf.nome as profissao
from
    cliente as cln
left outer join
    profissao as prf on cln.idprofissao = prf.idprofissao

select 
    cln.nome as cliente,
	prf.nome as profissao
from
    cliente as cln
inner join
    profissao as prf on cln.idprofissao = prf.idprofissao

select 
    cln.nome as cliente,
	prf.nome as profissao
from
    cliente as cln
right outer join
    profissao as prf on cln.idprofissao = prf.idprofissao


select 
    cln.nome as cliente,
	prf.nome as profissao,
	ncn.nome as nacionalidade,
    cln.logradouro,
	cln.numero,
    cmp.nome as complemento,
    brr.nome as bairro,
	mnc.nome as municipio,
	uf.nome as estado,
	uf.sigla
from
    cliente as cln
left outer join
    profissao as prf on cln.idprofissao = prf.idprofissao
left outer join 
   nacionalidade ncn on cln.idnacionalidade = ncn.idnacionalidade
left outer join 
   complemento cmp on cln.idcomplemento = cmp.idcomplemento 
left outer join 
   bairro brr on cln.idbairro = brr.idbairro
left outer join 
   municipio mnc on cln.idmunicipio = mnc.idmunicipio
left outer join 
   uf on mnc.iduf = uf.iduf

select 
    prd.nome,
	prd.valor
from
    produto prd
left outer join 
    fornecedor frn on prd.idfornecedor = frn.idfornecedor 

select 
    trs.nome as transportadora,
	mnc.nome  as municipio 
from
    transportadora trs
left outer join 
    municipio mnc on trs.idmunicipio = mnc.idmunicipio

select 
    pdd.data_pedido,
	pdd.valor,
	cln.nome as cliente,
	trn.nome as transportadora,
	vnd.nome as vendedor
from
    pedido pdd
left outer join
    cliente cln on pdd.idcliente = cln.idcliente 
left outer join 
    transportadora trn on pdd.idtransportadora = trn.idtransportadora 
left outer join 
    vendedor vnd on pdd.idvendedor = vnd.idvendedor 

select 
    pdt.nome as produto,
    pdp.quantidade,
	pdp.valor_unitario
from
    pedido_produto pdp 
left outer join
    produto pdt on pdp.idproduto = pdt.idproduto

select
    cln.nome, 
	pdd.data_pedido
from 
    cliente cln
inner join 
    pedido pdd on pdd.idcliente = cln.idcliente 
order by 
    cln.nome

select
    cln.nome, 
	pdd.data_pedido
from 
    cliente cln
left outer join 
    pedido pdd on pdd.idcliente = cln.idcliente 
order by 
    cln.nome

select
    idmunicipio,
	count(id)
from 
    cliente cln 
inner join 
    municipio mnc on cln.idmunicipio = mnc.idmunicipio
group by 
    mnc.nome

select 
    frn.nome as fornecedor,
	count(pdd.idproduto)
from
    produto pdd
left outer join
    fornecedor frn on pdd.idfornecedor = frn.idfornecedor  
group by 
    frn.nome 

select
    cln. nome as cliente,
	sum(pdd.valor) as total
from 
    pedido pdd
left outer join
    cliente cln on pdd.idcliente = cln.idcliente 
group by
    cln.nome

select 
    vnd.nome,
	sum(pdd.valor)
from
    pedido pdd
left join
    vendedor vnd on pdd.idvendedor = vnd.idvendedor
group by
    vnd.nome 

select
    trn.nome as transportadora,
    sum(pdd.valor) as total 
from
    pedido pdd
left outer join
    transportadora trn on pdd.idtransportadora = trn.idtransportadora
group by
    trn.nome 

select 
    cln.nome as cliente,
	count(pdd.idpedido) as total
from
    pedido pdd
left outer join
    cliente cln on pdd.idcliente = cln.idcliente 
group by 
    cln.nome  

select 
    pdt.nome as produto,
	sum(pdp.quantidade) as total
from
    pedido_produto pdp
left outer join
    produto pdt on pdp.idproduto = pdt.idproduto
group by
    pdt.nome

select
    pdd.data_pedido,
	sum(pdp.valor_unitario) as total 
from
    pedido_produto pdp
left outer join
   pedido pdd on pdp.idpedido = pdd.idpedido
group by 
    pdd.data_pedido 

select
    pdd.data_pedido,
	sum(pdp.quantidade) as quantidade
from
    pedido_produto pdp
left outer join
   pedido pdd on pdp.idpedido = pdd.idpedido
group by 
    pdd.data_pedido 


select * from pedido
select 
    data_pedido, 
	extract(day from data_pedido),
	extract(month from data_pedido),
	extract(year from data_pedido)
from
   pedido

select nome, substring(nome from 1 for 5), substring(nome, 2)from cliente

select nome, upper (nome) from cliente 

select nome, cpf, coalesce(cpf, 'não informado') from cliente

select
   case sigla 
       when 'pr' then 'parána'
	   when 'sc' then 'santa catarina'
   else 'outros'
   end as uf
from
   uf

select
    nome,
	case extract(month from data_nascimento)
	when 1 then 'janeiro'
	when 2 then 'fevereiro'
	when 3 then 'março'
	when 4 then 'abril'
	when 5 then 'maio'
	when 6 then 'junho'
	when 7 then 'julho'
	when 8 then 'agosto'
	when 9 then 'setembro'
	when 10 then 'outubro'
	when 11 then 'novembro'
	when 12 then 'dezembro'
   else
       'não informado'
   end as mes
from 
    cliente 

select
    nome,
	coalesce(extract(year from data_nascimento),0)
from
    cliente

select nome, substring(nome from 5 for 10) from municipio

select nome, upper(nome) from municipio

select 
    nome,
	case genero
	    when 'm' then 'masculino'
		when 'f' then 'feminino'
		end as genero
from
    cliente

select
    nome,
	valor,
	case 
	    when valor >= 500 then 'acima de 500'
		else 
		    'abaixo de 500'
	end as faixa 
from
    produto

select 
     data_pedido,
	 valor
from
    pedido
where 
    valor > (select avg(valor) from pedido)

select 
    pdd.data_pedido,
	pdd.valor,
	(select sum(quantidade) from pedido_produto pdp where pdp.idpedido = pdd.idpedido) as total
from
    pedido pdd

update pedido set valor = valor + ((valor * 5) / 100)
where valor > (select avg(valor) from pedido)

select 
    nome,
	idmunicipio
from
    cliente 
where   
	idmunicipio = (select idmunicipio from cliente where nome = 'manoel')
and
    idcliente <> 1

select 
    data_pedido,
	valor
from
    pedido
where 
    valor < (select avg(valor) from pedido)

select 
    pdd.data_pedido,
	pdd.valor,
	cln.nome as cliente
from
    pedido pdd
left outer join
    cliente cln on  pdd.idcliente = cln.idcliente
left outer join
    vendedor vnd onpdd.idcliente = cln.idcliente
left outer join
    vendedor vnd on pdd.idvendedor = vnd.idvendedor
where 
    (select count(quantidade) from pedido_produto pdp where pdp.idpedido = pdd.idpedido) >= 2

select
    nome,
	idmunicipio
from
    cliente
where
	idmunicipio = (select idmunicipio from transportadora where idtransportadora = 1 )

select 
    nome,
	idmunicipio
from
    cliente 
where 
    idmunicipio in (select idmunicipio from transportadora )

update 
     pedido
set 
     valor = valor + ((valor * 5) / 100)
where 
     (select sum(pdp.valor_unitario)from pedido_produto pdp where pdp.idpedido = idpedido) > (select avg(valor_unitario) from pedido_produto)



select 
     pdd.idpedido,
	 (select sum(v)lor_unitario) from pedido_produto pdp where pdp.idpedido = pdp.idpedido )
from 
    pedido pdd
	
select avg(valor_unitario) from pedido_produto

select
    cln.nome,
	(select count(idpedido) from pedido pdd where pdd.idcliente = cln.idcliente) as total
from
    cliente cln


select
    cln.nome as cliente,
	count(pdd.idpedido) as total
from 
    pedido pdd
left outer join
    cliente cln on  pdd.idcliente =  cln.idcliente 
group by 
    cln.nome

drop view cliente_profissao;

create view cliente_profissao as 
select
    cln.nome as cliente,
	cln.cpf,
	prf.nome as profissao
from
    cliente cln
left outer join
    profissao prf on cln.idprofissao = prf.idprofissao

select cliente from cliente_profissao where profissao = 'professor'


create view cliente_dados as 
select
    cln.nome as cliente,
	prf.nome as profissao,
	ncn.nome as nacionalidade,
	cmp.nome as complemento,
	mnc.nome as municipio,
	uf.nome as unidade_federacao,
	brr.nome as bairro,
	cln.rg,
	cln.cpf,
	cln.data_nascimento,
	case cln.genero
	   when 'm' then 'masculino'
	   when 'f' then 'feminino'
	end as genero,
	cln.logradouro,
	cln.numero,
	cln.observacoes
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


create view muicipio_uf as
select
    mnc.nome as municipio,
	uf.nome as unidade_federacao,
	uf.sigla 
from
    municipio mnc
left outer join
    uf on mnc.iduf = uf.iduf



create view produto_fornecedor as
select
	prd.nome as produto,
	prd.valor
from
    produto prd 
left outer join
    fornecedor frn on prd.idfornecedor  = frn.idfornecedor  

create view trnasportadora_uf as 
select
    trn.nome as transportadora,
	trn.logradouro,
	trn.numero
from
   	transportadora trn
left outer join
	municipio mnc on trn.idmunicipio = mnc.idmunicipio
left outer join
	uf on mnc.iduf = uf.iduf

create view dados_pedido as 
select 
	pdd.data_pedido,
	pdd.valor,
	trn.nome as trasnportadora,
	cln.nome as cliente,
	vnd.nome as vendedor 
from
	pedido pdd
left outer join
	transportadora trn on pdd.idtransportadora = trn.idtransportadora 
left outer join 
	cliente cln on pdd.idcliente = cln.idcliente 
left outer join
	vendedor vnd on pdd.idvendedor = vnd.idvendedor 


create view produto_pedido as 
select
	prd.nome as produto,
	pdp.quantidade,
	pdp.valor_unitario
from
	pedido_produto pdp
left outer join
	produto prd on pdp.idproduto = prd.idproduto
	

create table exemplo (
	idexemplo serial not null,
	nome varchar(50) not null,

	constraint pk_exemplo_idexemplo primary key (idexemplo)
);

insert into exemplo(nome) values ('exemplo 1 ');
insert into exemplo(nome) values ('exemplo 2 ');
insert into exemplo(nome) values ('exemplo 3 ');
insert into exemplo(nome) values ('exemplo 4 ');
insert into exemplo(nome) values ('exemplo 5 ');

select max(idbairro) +1 from bairro
create sequence bairro_id_seq minvalue 5
alter table bairro alter idbairro set default nextval('bairro_id_seq')
alter sequence bairro_id_seq owned by bairro.idbairro
insert into bairro (Nome) values ('teste 1');
insert into bairro (Nome) values ('teste 2');



select max(idcliente) + 1 from cliente 
create sequence cliente_id_seq minvalue 18
alter table cliente alter idcliente set default nextval ('cliente_id_seq')
alter sequence cliente_id_seq owned by cliente.idcliente


select max(idcomplemento) + 1 from complemento
create sequence complemento_id_seq minvalue 3
alter table complemento alter idcomplemento set default nextval('complemento_id_seq')
alter sequence complemento_id_seq owned by complemento.idcomplemento
insert into complemento (nome) values ('teste sequencia ')


select max(idfornecedor) + 1 from fornecedor  
create sequence fornecedor_id_seq minvalue 4
alter table fornecedor alter idfornecedor set default nextval('fornecedor_id_seq')
alter sequence fornecedor_id_seq owned by fornecedor.idfornecedor
insert into fornecedor (nome) values ('teste sequencia ')



select max(idmunicipio) + 1 from municipio  
create sequence municipio_id_seq minvalue 10
alter table municipio alter idmunicipio set default nextval('municipio_id_seq')
alter sequence municipio_id_seq owned by municipio.idmunicipio
insert into municipio (nome, iduf) values ('teste sequencia', 1)



select max(idnacionalidade) + 1 from nacionalidade
create sequence nacionalidade_id_seq minvalue 5
alter table nacionalidade alter idnacionalidade set default nextval('nacionalidade_id_seq')
alter sequence nacionalidade_id_seq owned by nacionalidade.idnacionalidade
insert into nacionalidade (nome) values ('teste sequencia')


select max(idpedido) + 1 from pedido  
create sequence pedido_id_seq minvalue 16
alter table pedido alter idpedido set default nextval('pedido_id_seq')
alter sequence pedido_id_seq owned by pedido.idpedido
insert into pedido (data_pedido, valor, idcliente,idvendedor)
values (current_date, 130, 1, 1)


select max(idprofissao) + 1 from profissao
create sequence profissao_id_seq minvalue 6
alter table profissao alter idprofissao set default nextval('profissao_id_seq')
alter sequence nacionalidade_id_seq owned by profissao.idprofissao
insert into profissao (nome) values ('teste sequencia')


select max(idtransportadora) + 1 from transportadora
create sequence transportadora_id_seq minvalue 3
alter table transportadora alter idtransportadora set default nextval('transportadora_id_seq')
alter sequence transportadora_id_seq owned by transportadora.idtransportadora
insert into transportadora (nome) values ('teste sequencia')


select max(iduf) + 1 from uf
create sequence uf_id_seq minvalue 7
alter table uf alter iduf set default nextval('uf_id_seq')
alter sequence uf_id_seq owned by uf.iduf
insert into uf (nome, sigla) values ('teste sequencia', 'TE')


select max(idvendedor) + 1 from vendedor
create sequence vendedor_id_seq minvalue 9
alter table vendedor alter idvendedor set default nextval('vendedor_id_seq')
alter sequence vendedor_id_seq owned by vendedor.idvendedor
insert into vendedor (nome) values ('teste sequencia')

select max(idproduto) + 1 from produto
create sequence produto_id_seq minvalue 8
alter table produto alter idproduto set default nextval('produto_id_seq')
alter sequence produto_id_seq owned by produto.idproduto



alter table pedido alter column data_pedido set default current_date;
alter table pedido alter column valor set default 0;
insert into pedido (idcliente, idvendedor) values (1, 1)
insert into pedido (idcliente, idvendedor, data_pedido, valor) 
values (1, 1, '2022-10-10', 234)



alter table pedido_Produto alter column quantidade set default 1;
alter table pedido_produto alter column valor_unitario set default 0;

insert into pedido_produto (idpedido, idproduto) values (1, 3)
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario)
values (1, 4, 5, 100)



alter table produto alter column valor set default 0;
insert into produto (nome, idfornecedor) values ('teste default 1', 1)
insert into produto (nome, idfornecedor, valor) values ('teste default 1', 1, 50)



create index idx_cln_nome on cliente (nome);


drop index idx_pdd_data_pedido 
create index idx_pdd_data_pedido on pedido (data_pedido)
create index idx_pdr_nome on produto (nome)











































