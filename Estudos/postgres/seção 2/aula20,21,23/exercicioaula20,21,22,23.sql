
create table fornecedor(
	id integer not null,
	nome varchar(50),
	constraint pk_forn_id primary key (id),
	constraint un_forn_nome unique (nome)
	
);
insert into fornecedor (id, nome) values (1, 'André');
insert into fornecedor (id, nome) values (2, 'Alisson');
insert into fornecedor (id, nome) values (3, 'José');



select * from fornecedor;

update fornecedor set nome = 'Cap.Computadores' where id = 1;
update fornecedor set nome = 'AA.Computadores' where id = 2;
update fornecedor set nome = 'BB.Máquinas' where id = 3;

create table vendedor(
	id integer not null,
	nome varchar(50),

	constraint pk_vend_id primary key(id),
	constraint un_vend_nome unique (nome)
);
insert into vendedor (id, nome) values (1, 'André');
insert into vendedor (id, nome) values (2, 'Alisson');
insert into vendedor (id, nome) values (3, 'José');
insert into vendedor (id, nome) values (4, 'Ailton');
insert into vendedor (id, nome) values (5, 'Maria');
insert into vendedor (id, nome) values (6, 'Suelem');
insert into vendedor (id, nome) values (7, 'Aline');
insert into vendedor (id, nome) values (8, 'Silvana');
select * from vendedor;

create table transportadora(
	id integer not null,
	idmunicipio integer not null,
	nome varchar (50) not null,
	logradouro varchar(40),
	numero varchar(10),

	constraint pk_transp_id primary key(id),
	constraint fk_transp_idmunicipio foreign key (idmunicipio) references municipio(idmunicipio),
	constraint un_transp_nome unique(nome)	
);
select * from municipio;
insert into transportadora (id, idmunicipio, nome, logradouro, numero) values (1, 2, 'BS. Transportes', 'Rua das limas', '01' );
insert into transportadora (id, idmunicipio, nome, logradouro, numero) values (2, 4, 'União Transportes', null, null);

select * from municipio

create table produto(
	idproduto integer not null,
	idfornecedor integer not null,
	nome varchar (50) not null,
	valor numeric(10,2) not null,
	constraint pk_prod_idproduto primary key (idproduto),
	constraint fk_prod_idfornecedor foreign key (idfornecedor) references fornecedor (id)
);
select * from fornecedor;
insert into produto (idproduto, idfornecedor, nome, valor) values (1, 1, 'Microcomputador', 800);
insert into produto (idproduto, idfornecedor, nome, valor) values (2, 1, 'Monitor', 500);
insert into produto (idproduto, idfornecedor, nome, valor) values (3, 2, 'Placa mãe', 200);
insert into produto (idproduto, idfornecedor, nome, valor) values (4, 2, 'HD', 150);
insert into produto (idproduto, idfornecedor, nome, valor) values (5, 2, 'Placa de Vídeo', 200);
insert into produto (idproduto, idfornecedor, nome, valor) values (6, 3,  'Mémoria RAM', 100);
insert into produto(idproduto, idfornecedor, nome, valor) values (7, 1, 'Gabinete', 35);

select * from produto;