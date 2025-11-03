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

create table pedido(
	idpedido integer not null,
	data_pedido date not null,
	valor numeric(10,2) not null,
	idcliente integer not null,
	idtransportadora integer,
	idvendedor integer,
	constraint pk_pedido_idpedido primary key (idpedido),
	constraint fk_pedido_idcliente foreign key (idcliente) references clientes(idcliente),
	constraint fk_pedido_idtransportadora foreign key (idtransportadora) references transportadora(id),
	constraint fk_pedido_idvendedor foreign key (idvendedor) references vendedor(id)
);
select * from clientes;
select * from transportadora;
select * from vendedor;
insert into pedido(idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (1, '01-04-2008', 1300, 1,  1, 1);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (2, '01-04-2008', 500, 1, 1, 1);
insert into pedido(idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (3, '02-04-2008', 300, 11, 2,  5);
insert into pedido(idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (4, '05-04-2008', 1000, 8, 1, 7);
insert into pedido(idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (5, '06-04-2008', 200, 9, 2, 6);
insert into pedido(idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (6, '06-04-2008', 1985, 10, 1, 6 );
insert into pedido(idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (7, '06-04-2008', 800, 3, 1, 7 );
insert into pedido(idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (8, '06-04-2008', 175, 3, null, 7);
insert into pedido(idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (9, '07-04-2008', 1300, 12, null, 8);
insert into pedido(idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (10, '10-04-2008', 200, 6, 1,  8);
insert into pedido(idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (11, '15-04-2008', 300, 15, 2, 1);
insert into pedido(idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (12, '20-04-2008', 500, 15, 2, 7);
insert into pedido(idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (13, '20-04-2008', 350, 9, 1, 7);
insert into pedido(idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (14, '23-04-2008', 300, 2, 1, 5);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor) values (15, '25-04-2008', 200, 11, null, 5);
select * from pedido;

create table pedido_produto(
	idpedido integer not null,
	idproduto integer not null,
	quantidade integer not null,
	valor_unitario decimal(10, 2) not null,
	constraint pk_pdp_idpedidoproduto primary key (idpedido, idproduto),
	constraint fk_pdp_idpedido foreign key (idpedido) references pedido(idpedido),
	constraint fk_pdp_idproduto foreign key (idproduto) references produto(idproduto)
);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (1, 1, 1, 800);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (1, 2, 1, 500);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (2, 2, 1, 500);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (3, 4, 2, 150);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (4, 1, 1, 800);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (4, 3, 1, 200);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (5, 3, 1, 200);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (6, 1, 2, 800);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (6, 7, 1, 35);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (6, 5, 1, 200);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (6, 4, 1, 150);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (7, 1, 1, 800);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (8, 7, 5, 35);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (9, 1, 1, 800);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (9, 2, 1, 500);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (10, 5, 1, 200);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (11, 5, 1, 200);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (11, 6, 1, 100);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (12, 2, 1, 500);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (13, 3, 1, 200);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (13, 4, 1, 150);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (14, 6, 3, 100);
insert into pedido_produto(idpedido, idproduto, quantidade, valor_unitario) values (15, 3, 1, 200);

select * from vendedor order by nome asc;
select * from produto where valor > 200 order by valor asc;
select nome, valor, round (valor * 1.10) from produto; 
select nome from municipio where iduf = 6;
select * from pedido where data_pedido between '10-04-2008' and '25-04-2008';
select * from pedido where valor between 1000 and 1500;
select * from pedido where valor not between 100 and 500;
select * from vendedor;
select * from pedido where idvendedor = 1 order by valor desc; 
select * from pedido where idcliente = 1 order by valor asc;
select * from clientes;
select * from pedido where idvendedor =1 and idcliente= 15; 
select * from pedido where idtransportadora = 2;
select * from vendedor;
select * from pedido where idvendedor = 5 or idvendedor = 7;
select * from municipio;
select * from clientes where idmunicipio = 2 or idmunicipio = 8;
select * from clientes where idmunicipio not in (2, 8);
select * from clientes where logradouro is null;
select * from clientes;
select * from clientes where logradouro like 'Av%';
select * from vendedor;
select * from vendedor where nome like 'S%';
select * from vendedor where nome like '%a';
select * from vendedor where nome not like 'A%';
select * from municipio;
select * from uf;
select * from municipio where nome like 'P%' and iduf = 3;
select * from transportadora where logradouro is not null;
select * from pedido_produto where idpedido= 1;
select * from pedido_produto where idpedido = 6 or idpedido= 10;
select avg(valor) from pedido;
select count(idmunicipio) from municipio;
select * from municipio;
select count(logradouro) from transportadora;
select count (id) from transportadora;
select count(*) from transportadora;
select count (idmunicipio) from municipio where iduf = 2;
select max(valor) from pedido;
select min(valor), max(valor) from pedido;
select sum(valor) from pedido;
select idcliente, sum(valor) from pedido group by idcliente having sum(valor) > 500;
select  round(avg(valor)), idvendedor from pedido group by idvendedor having sum(valor) > 200;
select sum(valor), idvendedor from pedido group by idvendedor;
select idvendedor, sum(valor) from pedido group by idvendedor having sum(valor) > 1500;
select * from municipio;
select count(idmunicipio) from municipio where iduf = 1 or iduf= 3;
select count(idmunicipio) from municipio group by iduf;
select count(idcliente) from clientes where logradouro is not null;
select count(idcliente) from clientes group by idmunicipio;
select count(id) from fornecedor;
select count(idproduto) from produto group by idfornecedor;
select round(avg(valor)) from produto where idfornecedor = 1;
select * from produto;
select sum(valor) from produto;
select nome, valor from produto where idproduto=1;
select nome, valor from produto where idproduto= 7;
select round(avg(valor)) from produto;
select * from pedido;
select idcliente, sum(valor) from pedido group by idcliente;
select idvendedor, sum(valor) from pedido group by idvendedor;
select idtransportadora, sum(valor) from pedido group by idtransportadora having idtransportadora is not null;
select data_pedido, sum(valor) from pedido group by data_pedido;
select sum(valor) from pedido group by data_pedido between '01-04-2008' and '10-12-2009' having sum(valor) > 200;
select * from vendedor;
select round(avg(valor)) from pedido where idvendedor = 1;
select * from clientes;
select round(avg(valor)) from pedido where idcliente = 15;
select * from pedido;
select count(idpedido) from pedido group by idtransportadora having idtransportadora = 1; 
select idvendedor, count(idpedido) from pedido group by idvendedor;
select idcliente, count(idpedido) from pedido group by idcliente;
select count(idpedido) from pedido where data_pedido between '15-04-2008' and '25-04-2008';
select count(idpedido) from pedido where valor > 1000;
select * from produto;
select * from pedido_produto;
select count(idpedido) from pedido_produto where idproduto = 1;
select idproduto, count(idpedido) from pedido_produto group by idproduto;
select idpedido, sum(valor_unitario) from pedido_produto group by idpedido;
select idpedido, count(idproduto) from pedido_produto group by idpedido;
select round(sum(valor_unitario)) from pedido_produto;
select round(avg(valor_unitario)) from pedido_produto where idpedido= 6;
select max(valor_unitario) from pedido_produto where idpedido=6;
select min(valor_unitario) from pedido_produto where idpedido=6;
select idpedido, sum(quantidade) from pedido_produto group by idpedido order by idpedido asc; 
select idproduto, sum(quantidade) from pedido_produto where idpedido= 6 group by idproduto order by sum(quantidade) asc;


select * from clientes;
select clientes.nome, profissao.nome from clientes left outer join profissao on clientes.idprofissao = profissao.idprofissao;
select clientes.nome, profissao.nome, nacionalidade.nome, complemento.nome, bairro.nome, municipio.nome, uf.nome from clientes left outer join  profissao on clientes.idprofissao = profissao.idprofissao left outer join nacionalidade on clientes.idnacionalidade = nacionalidade.idnacionalidade left outer join  complemento on clientes.idcomplemento = complemento.idcomplemento left outer join bairro on clientes.idbairro= bairro.idbairro left outer join municipio on clientes.idmunicipio = municipio.idmunicipio left outer join uf on clientes.iduf = uf.iduf;
select prd.nome as produto, valor, forn.nome as fornecedor from produto as prd left outer join fornecedor as forn on prd.idfornecedor = forn.id;
select trans.nome as transportadora, mun.nome as municipio from transportadora as trans left outer join municipio as micipio = mun.idmunicipio;un on trans.idmun
select
	data_pedido as data, 
	valor,
	cln.nome as cliente,
	trans.nome as transportadora,
	vend.nome as vendedor
from pedido as ped
left outer join clientes		as cln		on ped.idcliente = cln.idcliente
left outer join transportadora as trans		on ped.idtransportadora = trans.id
left outer join vendedor 		as vend		on ped.idvendedor = vend.id;

select
	idpedido,
	prod.nome as produto,
	quantidade,
	valor_unitario
from pedido_produto as pedpro
left outer join produto	as prod		on pedpro.idproduto = prod.idproduto
order by idpedido asc;
select
	cln.nome as cliente,
	idpedido,
	data_pedido
from pedido as ped
inner join clientes as cln		on ped.idcliente = cln.idcliente
order by cliente asc;

select
	cln.nome as cliente,
	idpedido,
	data_pedido
from pedido as ped
full outer join clientes as cln  on ped.idcliente = cln.idcliente
order by cliente asc;

select
	count(cln.idcliente) as quantidade,
	mun.nome as municipio
from clientes as cln
left outer join municipio as mun		on cln.idmunicipio = mun.idmunicipio
group by mun.nome;

select
	count(prod.idproduto) as produto,
	forn.nome as fornecedor
from produto as prod
left outer join fornecedor as forn		on prod.idfornecedor = forn.id
group by forn.nome;

select
	sum(valor) as valor,
	cln.nome as cliente
from pedido as ped
left outer join clientes as cln		on ped.idcliente = cln.idcliente
group by cln.nome;

select * from pedido;

select
	sum(valor) as valor,
	vend.nome as vendedor
from pedido as ped
left outer join vendedor as vend	on ped.idvendedor = vend.id
group by vend.nome;

select
	sum(valor) as valor,
	trans.nome as transportadora
from pedido as ped
inner join transportadora as trans		on ped.idtransportadora = trans.id
group by transportadora;

select
	count(idpedido) as quantidade,
	cln.nome as cliente
from pedido as ped
left outer join clientes as cln		on ped.idcliente = cln.idcliente
group by cln.nome;


select
	sum(quantidade) as quantidade,
	prod.nome as produto
from pedido_produto as pedpro
left outer join produto as prod		on pedpro.idproduto = prod.idproduto
group by prod.nome;

select 
	data_pedido as data,
	sum(valor) as valor
from pedido
group by data_pedido;


select
	data_pedido as data,
	count(quantidade) as quantidade
from pedido as ped
left outer join pedido_produto as pedpro	on pedpro.idpedido = ped.idpedido
group by data_pedido;

