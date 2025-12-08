create table cliente (
	idcliente integer not null,
	nume varchar(50) not null, 
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

	constraint pk_clnt_idcliente primary key(idcliente)
	
);
insert into cliente (idcliente, nume, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (1, 'Manoel', '88828383821', '32323', '2001-01-30', 'M', 'Estudante', 'Brasileira', 'Rua Joaquim Nabuco', '23', 'Casa', 'Cidade Nova', 'Porto União', 'SC');
insert into cliente (idcliente, nume, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (2, 'Geraldo', '89760234567', '9292', '2002-02-28', 'M', 'Policial', 'Brasileira', 'Rua das Limas', '200', 'Ap', 'Centro', 'Porto União', 'SC');
insert into cliente (idcliente, nume, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (3, 'Carlos', '89768590321', '9494', '2008-02-10', 'M', 'Estudante', 'Brasileira', 'Alameidas', '42', 'Ap', 'Centro', 'São Paulo', 'SP');
insert into cliente (idcliente, nume, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (4, 'Arnaldo', '45870932433', '4562', '1998-02-18', 'M', 'Engenheiro', 'Brasileira', 'Rua de Maranhão', '330', 'Ap', 'Centro', 'Macedônia', 'CE');
insert into cliente (idcliente, nume, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (5, 'Aruan', '23433254657', '9276', '2000-10-12', 'M', 'Psicólogo', 'Brasileira', 'Avenida Rima', '30', null, 'Centro', null, null);
insert into cliente (idcliente, nume, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (6, 'Alan', '12233454612', '3045', '1990-12-10', 'M', 'Advogado', null, null, '160', 'Casa', 'Ademir', 'Aviagem', 'CE');
insert into cliente (idcliente, nume, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (7, 'João', '47382910398', '6868', '1980-04-28', 'M', 'Espião', 'Brasileira', null, null, 'Ap', null, 'Porto União', 'SC');
insert into cliente (idcliente, nume, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (8, 'Sandra', '23532364578', '9898', '2001-11-30', 'F', 'Bombeiros', 'Brasileira', 'Ademir', '12', 'Ap', 'Centro', 'Distrito Federal', 'DF');
insert into cliente (idcliente, nume, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (9, 'Darian', '97675608589', '8585', '2009-02-22', 'M', 'Estudante', 'Italiano', null, null, 'Ap', 'Centro', 'Roma', null);
insert into cliente (idcliente, nume, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (10, 'Fernanda', null, null, null, 'F', 'Estudante', 'Brasileira', null, null, null, null, 'Lavras', 'MG');
insert into cliente (idcliente, nume, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (11, 'Maria Eduarda', null, null, '2009-08-09', 'F', 'Estudante', 'Brasileira', null, null, null, null, 'Lavras', 'MG');
insert into cliente (idcliente, nume, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (12, 'Lary', null, null, null, 'F', 'Estudante', 'Brasileira', null, null, null, null, 'Lavras', 'MG');

select * from cliente;

select nume, data_nascimento from cliente;

select nume, data_nascimento as "Data de Nascimento" from cliente;

select 'CPF: ' || cpf || ' RG: ' || rg as "CPF e RG" from cliente;

select nume, data_nascimento from cliente where data_nascimento > '2000-01-01';

select nume from cliente where nume like 'C%';

select nume from cliente where nume like '%C%';

select nume, data_nascimento from cliente where data_nascimento between '1990-01-01' and '1998-01-01';

select nume, rg from cliente where rg is null;

select nume from cliente order by nume asc;

select nume from cliente order by nume desc;
--1. O nome, o gênero e a profissão de todos os clientes, odenado peo nome em ordem decrescente
select nume, genero, profissao from cliente order by nume desc;
--2. Os clientes que tenham a letra "R" no nome
select nume from cliente where nume like '%R%';
--3. Os clientes que o nome inicia com a letra "C"
select nume from cliente where nume like 'C%';
--4. Os clientes que o nome termina com a letra "A"
--ilike 
select nume from cliente where nume ilike '%A';
--5. Os clientes que moram no bairro "Centro"
select nume, bairro from cliente where bairro = 'Centro';
--6. Os clientes que moram em complementos que iniciam com a letra "A"
select nume, complemento from cliente where complemento ilike '%A%';
--7. Somente os clientes do sexo feminino 
select nume, genero from cliente where genero ilike 'M';
--8. Os clientes que não informaram o CPF
select nume, cpf from cliente where CPF is null;
--9. O nome e a profissão dos clientes, ordenado em ordem crescente pelo nome da profissão
select nume, profissao from cliente order by profissao asc;
--10. Os clientes de nacionalidade "Brasileira"
select nume from cliente where nacionalidade ilike 'Brasil%';
--11. O clientes que informaram o número da residência
select nume, numero from cliente where numero is not null;
--12. Os clientes que moram em Santa Catarina
select nume, uf from cliente where uf ilike 'SC';
--13. Os clientes que nasceram entre 01/01/2000 e 01/01/2002
select nume, data_nascimento from cliente where data_nascimento between '2000-01-01' and '2002-01-01';
--14. O nome do cliente e o logradouro, número, complemento, bairro, município e UF concatenamnte
select '< NOME >: ' || nume || ' < LOGRADOURO >: ' || logradouro || ' < NÚMERO >: ' || numero || ' < BAIRRO >: ' || bairro || ' < MUNICÍPIO >:  ' || municipio || ' < UF >: ' || uf as "informações" from cliente;
--Trocando os valores dentro da variável 'nume' por 'nome'
update cliente set nume = 'nome' where idcliente = 2;
select * from cliente
update cliente set nume = 'Adriano', genero = 'M', numero = '241' where idcliente = 2;
insert into cliente (idcliente, nume) values (16, 'João');
delete from cliente where idcliente = 16;
select * from cliente

--1. Insira os dados abaixo na tabela de clientes

insert into cliente (idcliente, nume, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf) values (16, 'Maicon', '12323445653', '2132', '2009-01-01', 'F', 'Empresário', null, null, null, null, null, 'Florianópolis', 'PR' );
insert into cliente (idcliente, nume, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf) values (17, 'Getúlio', null, '4355', null, 'F', 'Estudante', 'Brasileira', 'Rua Central', '343', 'Apartamento', 'Centro', 'Curitiba', 'PR' );
insert into cliente (idcliente, nume, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf) values (18, 'Sandra', null, null, null, 'M', 'Professor', 'Italiana', null, 12, 'Bloco A', null, null, null );
--2. ALterando os dados do Maicon
update cliente set cpf = '45390569432', genero = 'M', nacionalidade = 'Brasileira', uf = 'SC' where idcliente = 16;
--3. Altere os dados do cliente Getúlio
update cliente set data_nascimento = '1978-04-01', genero = 'M' where idcliente = 17;
--4. Altere os dados da cliente Sandra
update cliente set genero = 'F', profissao = 'Professora', numero = '123' where idcliente = 18;
--5. Apague o cliente Maicon
delete from cliente where idcliente = 16;
--6. Apague a cliente Sandra
delete from cliente where idcliente = 18;
select * from cliente



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

select * from profissao

create table nacionalidade (
	idnacionalidade integer not null,
	nome varchar(30) not null,

	constraint pk_ncn_idnacionalidade primary key (idnacionalidade),
	constraint un_ncn_nome unique (nome)
);

insert into nacionalidade (idnacionalidade, nome) values (1, 'Brasileira');
insert into nacionalidade (idnacionalidade, nome) values (2, 'Italiana');
insert into nacionalidade (idnacionalidade, nome) values (3, 'NOrte-americana');
insert into nacionalidade (idnacionalidade, nome) values (4, 'Alemã');

select * from nacionalidade;

create table complemento (
	idcomplemento integer not null, 
	nome varchar(30) not null,

	constraint pk_cpl_idcomplemento primary key (idcomplemento),
	constraint un_cpl_nome unique (nome)
	
);
insert into complemento (idcomplemento, nome) values (1, 'Casa');
insert into complemento (idcomplemento, nome) values(2, 'Apartamento');

select * from complemento;

create table bairro (
	idbairro integer not null,
	nome varchar(30) not null,

	constraint pk_brr_idbairro primary key (idbairro),
	constraint un_brr_nome unique (nome)
);

insert into bairro (idbairro, nome) values (1, 'Cidade Nova');
insert into bairro (idbairro, nome) values (2, 'Centro');
insert into bairro (idbairro, nome) values (3, 'São Pedro');

select * from bairro;

select * from cliente;

alter table cliente rename column nume to nome;

alter table cliente rename column profissao to idprofissao;
alter table cliente drop idprofissao;
alter table cliente add idprofissao integer; -- foreign key
alter table cliente add constraint fk_cln_idprofissao foreign key (idprofissao) references profissao (idprofissao);
update cliente set idprofissao = 1 where idcliente in (1, 9, 10, 12, 15, 17);
update cliente set idprofissao = 2 where idcliente = 2;
update cliente set idprofissao = 3 where idcliente = 3;
update cliente set idprofissao = 4 where idcliente in (4, 5);
update cliente set idprofissao = 5 where idcliente in (6, 7, 8, 13);
select * from cliente;

alter table cliente drop nacionalidade;
alter table cliente add idnacionalidade integer;
alter table cliente add constraint fk_cln_idnacionalidade foreign key(idnacionalidade) references nacionalidade (idnacionalidade);
update cliente set idnacionalidade = 1 where idcliente in (1, 2, 3, 4, 6, 10, 11, 14);
update cliente set idnacionalidade = 2 where idcliente in (5,7);
update cliente set idnacionalidade = 3 where idcliente = 8;
update cliente set idnacionalidade = 4 where idcliente in (9, 13);

select * from cliente;
alter table cliente drop complemento;
alter table cliente add idcomplemento integer;
alter table cliente add constraint fk_cln_idcomplemento foreign key (idcomplemento) references complemento (idcomplemento);
select * from complemento;
update cliente set idcomplemento = 1 where idcliente in (1, 4, 9, 13);
update cliente set idcomplemento = 2 where idcliente in (2, 3, 7);

alter table cliente drop bairro;
alter table cliente add idbairro integer;
alter table cliente add constraint fk_cln_idbairro foreign key (idbairro) references bairro (idbairro)
update cliente set idbairro = 1 where idcliente in (1, 12, 13);
update cliente set idbairro = 2 where idcliente in (2, 3, 5, 8, 9);
update cliente set idbairro = 3 where idcliente in (4, 5);
update cliente set idbairro = 4 where idcliente = 7;

select * from cliente

create table uf (
	iduf integer not null,
	nome varchar(30) not null,
	sigla char(2) not null,

	constraint pk_ufd_idunidade_federacao primary key (iduf),
	constraint un_ufd_nome unique (nome),
	constraint un_ufd_siglha unique (sigla)
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
insert into municipio (idmunicipio, nome, iduf) values (9, 'União Vitória', 2);
select * from municipio;
select * from cliente;
alter table cliente drop municipio;
alter table cliente drop uf;
alter table cliente add idmunicipio integer;
alter table cliente add constraint fk_cliente_idmunicipio foreign key (idmunicipio) references municipio (idmunicipio);
update cliente set idmunicipio = 1 where idcliente in (1, 2, 10, 11);
update cliente set idmunicipio = 2 where idcliente in (3, 12);
update cliente set idmunicipio = 3 where idcliente = 4;
update cliente set idmunicipio = 4 where idcliente in (5);
update cliente set idmunicipio = 6 where idcliente in (6, 13);
update cliente set idmunicipio = 7 where idcliente in (7);
alter table cliente add iduf integer;
alter table cliente add constraint fk_cliente_iduf foreign key (iduf) references uf (iduf);
update cliente set iduf = 1 where idmunicipio in (1, 2);
update cliente set iduf = 2 where idmunicipio in (2, 4, 9);
update cliente set iduf = 3 where idmunicipio = 5;
update cliente set iduf = 4 where idmunicipio = 7;
update cliente set iduf = 5 where idmunicipio = 8;
update cliente set iduf = 6 where idmunicipio = 6;
select * from cliente
select * from municpio
-- exercício 

create table fornecedor (
	idfornecedor integer not null,
	nome varchar(30) not null,
	
	constraint pk_for_idfornecedor primary key (idfornecedor),
	constraint un_for_nome unique (nome)
)

create table vendedor (
	idvendedor integer not null, 
	nome varchar(50), 

	constraint pk_vnd_idvendedor primary key (idvendedor),
	constraint un_vnd_nome unique (nome)
)

create table transportadora (
	idtransportadora integer not null,
	nome varchar(50) not null, 
	logradouro varchar(50),
	numero varchar(10),

	constraint pk_tnp_idtransportadora primary key (idtransportadora),
	constraint un_ntp_nome unique (nome)
)

alter table transportadora add idmunicipio integer;
alter table transportadora add constraint fk_tnp_idmunicipio foreign key (idmunicipio) references municipio (idmunicipio);

create table produto (
	idproduto integer not null,
	nome varchar(50) not null,
	valor numeric(10,2) not null,

	constraint pk_pdt_idproduto primary key (idproduto)
);

alter table produto add idfornecedor integer;
alter table produto add constraint fk_pdt_idfornecedor foreign key (idfornecedor) references fornecedor (idfornecedor)
insert into fornecedor (idfornecedor, nome) values (1, 'Cap. Computadores');
insert into fornecedor (idfornecedor, nome) values (2, 'AA. Computadores');
insert into fornecedor (idfornecedor, nome) values (3, 'BB. Máquinas');
insert into vendedor (idvendedor, nome) values (1, 'André');
insert into vendedor (idvendedor, nome) values (2, 'ALisson');
insert into vendedor (idvendedor, nome) values (3, 'José');
insert into vendedor (idvendedor, nome) values (4, 'Ailton');
insert into vendedor (idvendedor, nome) values (5, 'Maria');
insert into vendedor (idvendedor, nome) values (6, 'Suelem');
insert into vendedor (idvendedor, nome) values (7, 'Aline');
insert into vendedor (idvendedor, nome) values (8, 'Silvana');
insert into transportadora (idtransportadora, idmunicipio, nome, logradouro, numero) values (1, 9, 'BS. Transportes', 'Rua das Limas', 01);
insert into transportadora (idtransportadora, idmunicipio, nome, logradouro, numero) values (2, 5, 'União Transportes', null, null);
insert into produto (idproduto, idfornecedor, nome, valor) values (1, 1, 'Microcomputador', 800);
insert into produto (idproduto, idfornecedor, nome, valor) values (2, 1, 'Monitor', 500);
insert into produto (idproduto, idfornecedor, nome, valor) values (3, 2, 'Placa mãe', 200);
insert into produto (idproduto, idfornecedor, nome, valor) values (4, 2, 'HD', 150);
insert into produto (idproduto, idfornecedor, nome, valor) values (5, 2, 'Placa de vídeo', 200);
insert into produto (idproduto, idfornecedor, nome, valor) values (6, 3, 'Memória RAM', 100);
insert into produto (idproduto, idfornecedor, nome, valor) values (7, 1, 'Gabinete', 35)
select * from transportadora;

create table pedido (
	idpedido integer not null,
	idcliente integer not null,
	idtransportadora integer,
	idvendedor integer not  null,
	data_pedido date not null,
	valor float not null,
	
	constraint pk_pdd_idpedido primary key (idpedido),
	constraint fk_pdd_idcliente foreign key (idcliente) references cliente (idcliente),
	constraint fk_pdd_idtransportadora foreign key (idtransportadora) references transportadora (idtransportadora),
	constraint fk_pdd_idvendedor foreign key (idvendedor) references vendedor (idvendedor)
);

select * from cliente
update cliente set nome = 'Manoel' where idcliente = 1;
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor )
values(1, '2008-04-01', 1300, 1, 1, 1);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor )
values(2, '2008-04-01', 500, 1, 1, 1);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor )
values(3, '2008-04-01', 30, 1, 1, 1);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor )
values(4, '2008-04-05', 1000, 8, 1, 7);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor )
values(5, '2008-04-06', 200, 9, 2, 6);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor )
values(6, '2008-04-06', 1985, 10, 1, 6);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor )
values(7, '2008-04-06', 800, 3, 1, 7);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor )
values(8, '2008-04-07', 175, 3, null, 7);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor )
values(9, '2008-04-07', 1300, 12, null, 7);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor )
values(10, '2008-04-10', 200, 6, 1, 8);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor )
values(11, '2008-04-15', 300, 10, 2, 1);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor )
values(12, '2008-04-20', 300, 10, 2, 5);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor )
values(13, '2008-04-20', 350, 9, 1, 7);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor )
values(14, '2008-04-23', 300, 2, 1, 5);
insert into pedido (idpedido, data_pedido, valor, idcliente, idtransportadora, idvendedor )
values(15, '2008-04-01', 200, 11, null, 5);
select * from cliente;
select * from pedido;

create table pedido_produto (
	idpedido integer not null,
	idproduto integer not null,
	quantidade integer not null,
	valor_unitario float not null,

	constraint pk_pdp_idpedidoproduto primary key (idpedido, idproduto),
	constraint fk_pdp_idpedido foreign key (idpedido) references pedido (idpedido),
	constraint fk_pdp_idproduto foreign key (idproduto) references produto (idproduto)
	
);

insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (1, 1, 1, 800);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (1, 2, 1, 500);
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (2, 2, 1, 500);
-- exercícios
-- 1. Somente o nome de todos os vendedores em ordem alfabética
select nome from vendedor order by nome asc;
-- 2. Os produtos que o preço seja maior que R$200,00, em ordem crescente pelo preço
select nome, valor from produto where valor > 500;
-- 3. O nome do produto, o preço e o preço reajustado em 10%, ordenado pelo nome do produto
select nome, valor, valor + (valor * 10)/100 as Reajuste from produto order by nome asc;
-- 4. Os municípios do Rio Grande do Sul
select * from municipio;
select nome from municipio where iduf = 5;
-- 5. Os pedidios feitos entre 10/04/2008 e 25/04/2008 ordenando pelo valor
select * from pedido;
select idpedido, valor, data_pedido from pedido where data_pedido between '2008-04-10' and '2008-04-25' order by valor asc;
-- 6. Os pedidos que o valor esteja entre R$1.000,00 e R$1.500,00
select idpedido, valor from pedido where valor between 1000 and 1500
-- 7. Os pedidos que o valor não esteja entre 1000 e 1500
select idpedido, valor from pedido where valor not between 1000 and 1500
-- 8. Os pedidos do Vendedor ANdré ordenado pelo valor em ordem decrescente
select * from vendedor
-- vendedor André é 1
select * from pedido;
select idpedido, idvendedor, valor from pedido where idvendedor = 1 order by valor desc;
-- 9. Os pedidos do cliente Darian ordenado pelo vlaor em ordem crescente
select * from cliente 
-- Darian é 9
select idpedido, idcliente, valor from pedido where idcliente = 9 order by valor desc;
-- 10. Os pedidos da cliente Maria Eduarda que foram feitos pelo vendedor André
select idpedido, idcliente, idvendedor, valor from pedido where idcliente = 11 and idvendedor = 5;
-- 11. Os pedidos que foram transportados pela transportadora UNião Transportes
select * from transportadora
select idpedido, idtransportadora from pedido where idtransportadora = 2
-- 12. Os pedidos feitos pela vendedora Maria ou pela vendedora Aline
select idpedido, idvendedor from pedido where idvendedor = 5 or idvendedor = 7
-- 13. Os clientes que moram em União da Vitória e nem em Porto União
select * from municipio;
-- Porto União = 1 and União Vitória = 9
select * from cliente where idmunicipio = 1 or idmunicipio = 9;
-- 14. Os que não moram
select * from cliente where not idmunicipio = 1 or idmunicipio = 9;
-- 15. Os clientes que não informaram o logradouro
select * from cliente where logradouro is null;
-- 16. Os clientes que moram em avenidas
select * from cliente where logradouro ilike '%avenida%';
-- 17. Os vendedores que o nome começa com a letra S
select * from vendedor where nome ilike 'S%';
-- 18. Os vendedores que o nome termian com a letra A
select * from vendedor where nome ilike '%A';
-- 19. Os vendedores que o nome não começa com a letra A
select * from vendedor where nome not like 'A%'
-- 20. Os municípios que começam com a letra P e são de SantaCatarina
select * from uf
select * from municipio where nome ilike 'P%' and iduf = 1
-- 21. As transportadoras que informaram o endereço 
select * from transportadora where logradouro is not null
-- 22. Os itens do pedido 01
select * from pedido_produto where idpedido = 1
-- 23. Os itens do pedido 06 ou do pedido 10
select * from pedido_produto where idpedido = 6 or idpedido = 10;
insert into pedido_produto (idpedido, idproduto, quantidade, valor_unitario) values (6, 2, 1, 3000), (10, 3, 1, 1000);

-- Funções agregradas
-- avg -> average (média)
select avg(valor) from pedido;
-- contagem de registros -> variáveis not null
select count(idmunicipio) from municipio
select count(*) from municipio
-- máximo --> max(valor) --> MAIOR VALOR REGISTRADO
select max(valor) from pedido
-- mínimo --> min(valor) --> MENOR VALOR REGISTRADO
select min(valor) from pedido
select min(Valor), max(valor) from pedido

-- soma --> sum(valor)

select sum(valor) from pedido

-- várias

select idcliente, sum(valor) from pedido group by idcliente
select idcliente, sum(valor) from pedido group by idcliente having sum(valor) > 500

-- Exercícios Funções agregradas
-- 1. A média dos valores de vendas dos vendedores que venderam maiS que R$ 200,00 
select avg(valor) from pedido group by idvendedor having sum(valor) > 200;
select * from pedido;
-- 2. Os vendedores que venderam mais que R$ 1500,00
select idvendedor from pedido group by idvendedor having sum(valor) > 1500;
-- 3. O somatório das vendas de cada vendedor
select idvendedor, sum(valor) from pedido group by idvendedor;
-- 4. A quantidade de municípios
select count(idmunicipio) from municipio
-- 5. A quantidade de municípios que são do Paraná ou de Santa Catarina
select iduf, count(idmunicipio) from municipio group by iduf having iduf = 1 or iduf = 2;
select * from municipio;
select * from uf;
-- 6. A quantidade de municípios por estado
select iduf, count(idmunicipio) from municipio group by iduf;
-- 7. A quantidade de cientes que informaram o logradouro
select count(idcliente) from cliente where logradouro is not null;
select * from cliente;
-- 8. A quantidade de clientes por município

select idmunicipio, count(idcliente) from cliente group by idmunicipio

-- 9. A quantidade de fornecedores 

select count(idfornecedor) from fornecedor 

-- 10. A quantidade de produtos por fornecedor
select * from produto
select idfornecedor, count(idproduto) from produto group by idfornecedor;

-- 11. A média e preços dos produtos do fornecedor Cap. Computadores
select * from produto
select * from fornecedor
select avg(valor) from produto where idfornecedor = 1

-- 12. O somatório dos preços de todos os produtos

select sum(valor) from produto

-- 13. O nome do produto e o preço somente do produto mais caro

--select nome, max(valor) from produto group by nome
select nome, valor from produto order by valor desc limit 1

-- 14. O nome do produto e o preço somente do produto mais barato
select nome, valor from produto order by valor asc limit 1

-- 15. A média de preço de todos os produtos

select nome, avg(valor) from produto group by nome
--select avg(valor) from produto

-- 16. A quantidade de transportadoras

select count(idtransportadora) from transportadora

-- 17. A média do valor de todos os pedidos

select avg(valor) from pedido

-- 18. O somatório do valor do pedido agrupado por cliente

select idcliente, sum(valor) from pedido group by idcliente

-- 19. O somatório do valor do pedido agrupado por vendedor

select * from pedido
select idvendedor, sum(valor) from pedido group by idvendedor

-- 20. O somatório do pedido agrupado por transportadora

select idtransportadora, sum(valor) from pedido group by idtransportadora

-- 21. O somatório do valor do pedido agrupado pela data

select data_pedido, sum(valor) from pedido group by data_pedido

-- 22 O somatório do valor do pedido agrupado por cliente, vendedor e transportadora

select idcliente, sum(valor) from pedido group by idcliente
select idvendedor, sum(valor) from pedido group by idvendedor
select idtransportadora, sum(valor) from pedido group by idtransportadora

-- 23. O somatório do vlaor do pedido que esteja entre 01/04/2008 e 10/12/2009 e que seja maior que R$ 200,00

select sum(valor) from pedido where data_pedido between '2008-01-04' and '2009-12-10' and valor > 200

-- 24. A média do valor do pedido do vendedor André

select * from vendedor
select avg(valor) from pedido where idvendedor = 1

-- 25. A média do valor do pedido da cliente Maria Eduarda
select * from cliente
select avg(valor) from pedido where idcliente = 11

-- 26. A quantidade de pedidos transportados pela transportadora BS. Transportes

select * from transportadora
select count(idpedido) from pedido where idtransportadora = 1

-- 27. A quantidade de pedidos agrupados por vendedor 

select idvendedor, count(idpedido) from pedido group by idvendedor

-- 28. A quantidade de pedidos agrupados por cliente

select idcliente, count(idpedido) from pedido group by idcliente

-- 29. A quantidade de pedidos entre 15/04/2008 e 25/04/2008

select count(idpedido) from pedido where data_pedido between '2008-04-15' and '2008-04-25'

-- 30. A quantidade de pedidos que o valor seja maior que R$1000,00

select count(idpedido) from pedido where valor > 1000

-- 31. A quantidade de micromputadores vendida

select * from pedido_produto
select * from produto
select sum(quantidade) from pedido_produto where idproduto = 1

-- 32. A quantidade de produtos vendida agrupado por produto

select sum(quantidade) from pedido_produto group by idproduto

-- 33. O somatório do valor dos produtos dos pedidos, agrupado por pedido

select idpedido, sum(valor_unitario) from pedido_produto group by idpedido

-- 34. A quantidade de produtos agrupados por pedido

select idpedido, sum(quantidade) from pedido_produto group by idpedido

-- 35. O somatório dos valores unitáios de todos os produtos 

select sum(valor_unitario) from pedido_produto group by idproduto

-- 36. A média dos produtos do pedido 6
select avg(valor_unitario) from pedido_produto where idpedido = 6

-- 37. O valor do maior produto do pedido

select max(valor_unitario) from pedido_produto where idpedido = 6

-- 38. O valor do menor produto do pedido

select min(valor_unitario) from pedido_produto where idpedido = 6

-- 39. O somatŕoio da quantidade de produtos por pedido

select idpedido, sum(quantidade) from pedido_produto group by idpedido

-- 40. O somatório da quantidade de todos os produtos do pedido

select sum(quantidade) from pedido_produto

-- Relacionamentos com joins

select 
	cln.nome as cliente, 
	prf.nome as profissao
from 
	cliente as cln
-- define qual tabela vai puxar
-- puxa todos os dados
left outer join
	profissao as prf on cln.idprofissao = prf.idprofissao

select 
	cln.nome as cliente, 
	prf.nome as profissao
from 
	cliente as cln
-- define qual tabela vai puxar
-- puxa os dados compatíveis com a condição determinada
inner join
	profissao as prf on cln.idprofissao = prf.idprofissao

select 
	cln.nome as cliente, 
	prf.nome as profissao
from 
	cliente as cln
-- define qual tabela vai puxar
-- compara os dados da tabela-base direita e puxa os resultados compatíveis
right outer join
	profissao as prf on cln.idprofissao = prf.idprofissao

-- EXERCÍCIOS

-- 1. O nome do cliente, a profissão, a nacionalidade, o logradouro, o número, o complemento, o bairro, o município e a unidade de federação
select * from cliente
select 
	cln.nome as ciente, 
	prf.nome as profissao,
	ncn.nome as nacionalidade,
	cln.logradouro, 
	cln.numero,
	cmp.nome as complemento,
	brr.nome as bairro,
	mcp.nome as municipio,
	uf.nome as uf,
	uf.sigla as sigla
	
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
	municipio mcp on cln.idmunicipio = mcp.idmunicipio
left outer join
	uf on cln.iduf = uf.iduf

-- 2. O nome do produto, o valore o nome do fornecedor

select
	prd.nome,
	prd.valor,
	frd.nome as fornecedor
from
	produto as prd
left outer join
	fornecedor frd on prd.idfornecedor = frd.idfornecedor

-- 3. O nome da transportadora e o município

select
	tnd.nome,
	mnc.nome as municipio
from 
	transportadora as tnd
left outer join
	municipio mnc on tnd.idmunicipio = mnc.idmunicipio

-- 4. A data do pedido, o valor, o nome do cliente, o nome da transportadora e o nome do vendedor

select * from pedido
select
	pdd.data_pedido,
	pdd.valor,
	cln.nome as cliente,
	tnd.nome as transportadora,
	vdd.nome as vendedor
from 
	pedido as pdd
left outer join
	cliente cln on pdd.idcliente = cln.idcliente
left outer join
	transportadora tnd on pdd.idtransportadora = tnd.idtransportadora
left outer join
	vendedor vdd on pdd.idvendedor = vdd.idvendedor

-- 5. O nome do produto, a quantidade e o valor unitário dos produtos do pedido

select * from pedido_produto
select
	prd.nome as produto,
	ppd.quantidade,
	ppd.valor_unitario
from 
	pedido_produto as ppd
left outer join
	produto prd on ppd.idproduto = prd.idproduto

-- 6. O nome dos clientes e a data do pedido dos clientes que fizeram algum pedido (ordenado pelo nome do cliente) 

select * from pedido
select
	cln.nome as cliente,
	pdd.data_pedido
from 
	pedido as pdd
inner join
	cliente cln on pdd.idcliente = cln.idcliente
order by cln.nome asc

-- 7. O nome dos clientes e a data do pedido de todos os clientes, independente se tenham feito pedido
select
	cln.nome as cliente,
	pdd.data_pedido
from 
	pedido as pdd
left outer join 
	cliente cln on pdd.idcliente = cln.idcliente
order by cln.nome asc

-- 8. O nome da cidade e a quantidade de clientes que moram naquela cidade

select 
	mun.nome as municipio,
	count(cln.nome)
from
	cliente as cln
left outer join
	municipio mun on cln.idmunicipio = mun.idmunicipio
group by(mun.nome)
	
-- 9. O nome do fornecedor e a quantidade de produtos de cada fornecedor

select * from produto
select
	frn.nome as fornecedor,
	count(prd.idproduto) as total
from
	produto as prd
left outer join
	fornecedor frn on prd.idfornecedor = frn.idfornecedor
group by(frn.nome)

-- 10. O nome do cliente e o somatório do valor do pedido (agrupado por cliente

select * from pedido
select
	cln.nome as cliente,
	sum(pdd.valor) as total
from
	pedido as pdd
left outer join
	cliente cln on pdd.idcliente = cln.idcliente
group by(cln.nome)

-- 11. O nome do vendedor e o somatório do valor do pedido (agrupado por vendedor)

select 
	vdd.nome as vendedor,
	sum(pdd.valor) as total
from
	pedido as pdd
left outer join
	vendedor vdd on pdd.idvendedor = vdd.idvendedor
group by(vdd.nome)

-- 12. O nome do vendedor e o somatório do valor do pedido (agrupado por vendedor)

select 
	tnd.nome as transportadora,
	sum(pdd.valor) as total
from
	pedido as pdd
left outer join
	transportadora tnd on pdd.idvendedor = tnd.idtransportadora
group by(tnd.nome)

-- 13. O nome do cliente e a quantidade de pedidos de cada um

select 
	cln.nome as cliente,
	sum(pdd.valor) as total
from
	pedido as pdd
left outer join
	cliente cln on pdd.idcliente = cln.idcliente
group by(cln.nome)

-- 14. O nome do produto e a quantidade vendida 

select * from pedido_produto

select
	prd.nome as produto,
	sum(ppd.quantidade) as quantidade
from 
	pedido_produto as ppd
left outer join
	produto prd on ppd.idproduto = prd.idproduto
group by(prd.nome)

-- 15. A data do pedido e o somatório do valor dos produtos do pedido

select * from pedido

select 
	pdd.data_pedido,
	sum(pdd.valor)
from 
	pedido as pdd
group by(pdd.data_pedido)

-- 16. A data do pedido e a quantidade de produtos do pedido (agrupado pela data do pedido)
-- não tenho nenhuma data nessa tabela e tô com preguiça de colocar já q é só pra 1 exercício
select 
	pdd.data_pedido,
	sum(pdd.valor) as total
from 
	pedido_produto as ppd
group by
	pdd.data_pedido

-- comandos adicionais 

-- extract (extrai qualquer dado específico de alguma variável)
-- utilizado principalmente para filtrar alguma pesquisa, por exemplo
-- Ex: puxar dados específicos dentro de uma data
select 
	data_pedido,
	extract(day from data_pedido),
	extract(month from data_pedido),
	extract(year from data_pedido)
from pedido

-- substring (extrai caractéres determinados pelo usuário dentro de uma variável)

select
	nome,
	substring(nome from 1 for 5), -- puxando os dados que preenchem os caractéres de 1 a 5 
	substring(nome, 2) -- extração feita a partir do TERCEIRO caractér
from cliente

-- upper (deixa todos os dados strings em maiúsculo)

select
	nome,
	upper(nome)
from cliente

-- coalesce (adiciona msgs para campos não informados)

select nome, cpf, coalesce(cpf, 'Não informado') from cliente

select * from cliente
insert into cliente(idcliente, nome, cpf, rg, data_nascimento) values(23, 'Arroba', null, null, null)

-- case, when, then, else, end (o if e else do postgres. Definem uma condição dentro das pesquisas)

select
	case sigla 
		when 'PR' then 'Paraná'
		when 'SC' then 'Santa Catarina'
	else 'Outros'
	end as uf
from uf

-- Exercícios - Comandos adicionais 

-- 1. O nome do cliente e somente o mÊs de nascimento. Caso a data de nascimento não esteja preenchida, mostrar a mensagem "Não informado"

select
	nome,
	coalesce(extract(month from data_nascimento), 0)
from cliente

-- 2. O nome do cliente e somente o ano de nascimento. Caso a data de nascimento não esteja preenchida mostrar a mensagem "Não informado"

select
	nome,
	case extract(month from data_nascimento)
		when 1 then 'Janeiro'
		when 2 then 'Fevereiro'
		when 3 then 'Março'
		when 4 then 'Abril'
		when 5 then 'Março'
		when 6 then 'Junho'
		when 7 then 'Julho'
		when 8 then 'Agosto'
		when 9 then 'Setembro'
		when 10 then 'Outubro'
		when 11 then 'Novembro'
		when 12 then 'Dezembro'
	else 'Incoerente'
	end as mes
from
	cliente

-- 3. O nome do cliente e somente o ano de nascimento. Caso a data de nascimento não esteja preenchida, mostrar a mensagem "Não informado"

select 
	nome,
	coalesce(extract(year from data_nascimento), 0)
from cliente

-- 4. O caractere 5 até o 10 de todos os municípios

select 
	nome,
	substring(nome from 5 for 10 )
from municipio

-- 5. O nome em maiúsculo de todos os municípios 

select
	nome,
	upper(nome)
from municipio

-- 6. O nome do cliente e o gênero. Caso seja M mostrar "Masculino", senão mostrar "Feminino"

select
	nome,
	case genero
		when 'M' then 'Masculino'
		when 'F' then 'Feminino'
	else 'Indefinido'
	end as genero
from cliente

-- 7. O nome do produto e o valor. Caso o vlaor seja maior do que R$ 500,00, mostrar a mensagem "Acima de 500", caso contrário, mostrar a mensagem "Abaixo de 500"

select 
	nome,
	case 
		when valor > 500 then 'Acima de 500'
	else 'Abaixo de 500'
	end as valor
from produto

-- Subconsultas

-- Selecionar a data do pedido e o valor onde o valor seja maior que a média dos valores de todos os pedidos

select
	data_pedido,
	valor
from pedido
where valor > (select avg(valor) from pedido)
-- Exemplo com count

select
	pdd.data_pedido,
	pdd.valor,
	(select sum(quantidade) from pedido_produto pdp where pdp.idpedido = pdp.idpedido)
from pedido pdd
-- Exemplo com update
select * from pedido

update pedido set valor = valor + (valor * (5/100))
where valor > (select avg(valor) from pedido)

-- Exercícios - Subconsulta
-- 1. O nome dos clientes que moram na mesma cidade do Manoel. Não deve ser mostrado o Manoel
select * from cliente where nome = 'Manoel'
select
	nome,
	idmunicipio
from cliente
where
	idmunicipio = (select idmunicipio from cliente where nome = 'Manoel')
and 
	idcliente <> 1

-- 2. A data e o valor dos pedidos que o valor do pedido seja menor que a média de todos os pedidos

select * from pedido

-- 3. A data, o valor, o cliente e o vendedor dos pedidos que possuem 2 ou mais produtos
select * from pedido_produto 
select
	pdd.data_pedido,
	pdd.valor,
	cln.nome as cliente,
	vnd.nome as vendedor,
	(select sum(quantidade) from pedido_produto pdp where pdp.idpedido = pdd.idpedido)
from pedido pdd
left outer join
	cliente cln on pdd.idcliente = cln.idcliente
left outer join
	vendedor vnd on pdd.idvendedor = vnd.idvendedor
where (select sum(quantidade) 

-- 4. O nome dos clientes que moram na mesma cidade da transportadora BSTransportes
select * from cliente
select * from municipio
select * from transportadora
select * from pedido
select
	cln.nome as cliente,
	(select nome as municipio from municipio mun where mun.idmunicipio = cln.idmunicipio),
	trn.nome as transportadora
from pedido pdd	
left outer join cliente cln on pdd.idcliente = cln.idcliente
left outer join transportadora trn on pdd.idtransportadora = trn.idtransportadora
where trn.idmunicipio = 1

-- 5. O nome do cliente e o município dos clientes que estão localizados no mesmo município de qualquer uma das transportadoras
select
	cln.nome as cliente,
	(select nome as municipio from municipio mun where mun.idmunicipio = cln.idmunicipio),
	trn.nome as transportadora
from pedido pdd	
left outer join cliente cln on pdd.idcliente = cln.idcliente
left outer join transportadora trn on pdd.idtransportadora = trn.idtransportadora
where trn.idmunicipio = 1 and trn.idmunicipio = 5

-- 6. Atualizar o valor do pedido em 5% para os pedidos que o somatório do valor total dos produtos daquele seja maior que a média do valor total

update pedido set valor = valor + (valor * (5/100)) where valor > (select sum(valor) from pedido group by idpedido having avg(valor) < sum(valor))

-- 7. O nome do cliente e a quantidade de pedidos feitos pelo cliente
select * from cliente
select * from pedido
select
	cln.nome as cliente,
	(select count(pdd.idpedido) from pedido pdd where pdd.idcliente = cln.idcliente)
from cliente cln

-- 8. Para revisar, refaça o exercício anterior utilizando group by e mostrando somente os clientes que fizeram pelo menos um pedido

select 
	cln.nome as cliente,
	count(pdd.idpedido) as total
from pedido pdd
left outer join cliente cln on pdd.idcliente = cln.idcliente
group by cln.nome

-- views
-- Utilizadas para criar visões das tabelas. Prioriza a agilidade na hora das consultas.
-- Método utilizado para contornar a utilização exagerada de comandos como os join's
create view cliente_profissao as
select
	cln.nome as cliente,
	prf.nome as profissao
from cliente cln
left outer join
	profissao prf on cln.idprofissao = prf.idprofissao

-- Após a criação da view, é possível encontrá-la na barra lateral do postgres no campo 'views'. Depois, podemos utilizar as views em consultas como qualquer outra tabela
select cliente from cliente_profissao where profissao = 'Professor'
-- drop viw 'nome da view' -> apaga a view

-- Exercícios - Views

-- 1. O nome, a profissão, a nacionalidade, o complemento, o município, a unidade de federação, o bairro, o CPF, o RG, a data de nascimento, o gÊnero (mostrar "Masculino" ou "Feminino"), o logradouro, o número e as observações dos clientes
select * from bairro
select * from cliente
create view view_cliente as
select
	cln.nome as cliente,
	prf.nome as profissao,
	ncl.nome as nacionalidade,
	cmp.nome as complemento,
	mnc.nome as municipio,
	uf.nome as uf,
	brr.nome as bairro,
	cln.cpf,
	cln.rg,
	cln.logradouro,
	cln.numero,
	cln.observacoes,
	case cln.genero
		when 'M' then 'Masculino'
		when 'F' then 'Feminino'
	else 'Indefinido'
	end as genero
from cliente cln
left outer join
	profissao prf on cln.idprofissao = prf.idprofissao
left outer join
	complemento cmp on cln.idcomplemento = cmp.idcomplemento
left outer join
	nacionalidade ncl on cln.idnacionalidade = ncl.idnacionalidade
left outer join
	municipio mnc on cln.idmunicipio = mnc.idmunicipio
left outer join
	uf on cln.iduf = uf.iduf
left outer join
	bairro brr on cln.idbairro = brr.idbairro

select * from view_cliente 
-- 2. O nome do município e o nome e a sigla da unidade da federação

create view municipio_uf as
select
	mun.nome as Município,
	uf.nome as Estado,
	uf.sigla as Sigla
from municipio mun
left outer join
	uf on mun.iduf = uf.iduf
select * from municipio_uf
-- 3. O nome do produto, o valor e o nome do fornecedor dos produtos

create view ver_produtos as
select
	prd.nome as "Produto",
	prd.valor as "Valor",
	frn.nome as "Fornecedor"
from produto prd
left outer join
	fornecedor frn on prd.idfornecedor = frn.idfornecedor

select * from ver_produtos
-- 4. O nome da transportadora, o logradouro, o número, o nome da unidade de federação e a sigla da unidade de federação das transportadoras
select * from transportadora
create view transpor_uf as
select
	trn.nome as "Transportadora",
	trn.logradouro as "Logradouro",
	trn.numero as "Número",
	uf.nome as "Estado",
	uf.sigla as "Sigla"
from municipio mnc
left outer join
	uf on mnc.iduf = uf.iduf
left outer join
	transportadora trn on mnc.idmunicipio = trn.idmunicipio

select * from transpor_uf

-- 5. A data do pedido, o valor , o nome da transportadora, o nome do cliente e o nome do vendedor dos pedidos

select * from pedido
create view pedido_tudo as
select
	pdd.data_pedido as "Data Do Pedido",
	pdd.valor as "Valor",
	trn.nome as "Transportadora",
	cln.nome as "Cliente",
	vdd.nome as "Vendedor"
from pedido pdd
left outer join
	transportadora trn on pdd.idtransportadora = trn.idtransportadora
left outer join
	cliente cln on pdd.idcliente = cln.idcliente
left outer join
	vendedor vdd on pdd.idvendedor = vdd.idvendedor

select * from pedido_tudo
-- 6. O nome do produto, a quantidade, o valor unitário e o valor total dos produtos do pedido
select * from pedido_produto
select * from pedido
select * from produto
create view ped_prod_tudo as
select
	pdp.idpedido as "IdPedido",
	prd.nome as "Produto",
	pdp.quantidade as "Quantidade",
	pdp.valor_unitario as "Valor Unitário",
	sum(pdd.valor) as "Total"
from pedido_produto pdp
left outer join
	produto prd on pdp.idproduto = prd.idproduto
left outer join
	pedido pdd on pdp.idpedido = pdd.idpedido 
group by pdp.idpedido
drop view ped_prod_tudo
select * from ped_prod_tudo

-- Campos autoincremento

create table exemplo (
	idexemplo serial not null, -- tipo serial (permite o autoincremento em uma variável. Cria uma sequence)
	nome varchar(50) not null,

	constraint pk_exemplo_idexemplo primary key (idexemplo)
);

insert into exemplo (nome) values ('exempro')
select * from exemplo

-- Para alterar o tipo de uma variável, siga os passos

select * from bairro

select max(idbairro) + 1 from bairro
create sequence bairro_id_seq minvalue 5
alter table bairro alter idbairro set default nextval('bairro_id_Seq')
alter sequence bairro_id_seq owned by bairro.idbairro
insert into bairro (nome) values ('Teste 1')

-- Exercícios - campos de autoincremento

-- 1. Criar sequências para todas as outras tabelas da base de dados

-- a) Cliente
select * from cliente
select max(idcliente) + 1 from cliente
create sequence cliente_id_seq minvalue 18
alter table cliente alter idcliente set default nextval('cliente_id_seq')
alter sequence cliente_id_seq owned by cliente.idcliente
insert into cliente (nome) values ('Teste 1')
select * from cliente 
-- b) Complemento

select max(idcomplemento) + 1 from complemento
create sequence complemento_id_seq minvalue 3
alter table complemento alter idcomplemento set default nextval('complemento_id_seq')
alter sequence complemento_id_seq owned by complemento.idcomplemento
insert into complemento (nome) values ('Teste 1')
select * from complemento

-- c) Fornecedor

select max(idfornecedor) + 1 from fornecedor
create sequence fornecedor_id_seq minvalue 4
alter table fornecedor alter idfornecedor set default nextval('fornecedor_id_seq')
alter sequence fornecedor_id_seq owned by fornecedor.idfornecedor
insert into fornecedor (nome) values ('Teste 1')
select * from fornecedor

-- d) Município 

select max(idmunicipio) + 1 from municipio
create sequence municipio_id_seq minvalue 10
alter table municipio alter idmunicipio set default nextval('municipio_id_seq')
alter sequence municipio_id_seq owned by municipio.idmunicipio
insert into municipio (nome) values ('Teste 1')
select * from municipio

-- e) Nacionalidade

select max(idnacionalidade) + 1 from nacionalidade
create sequence nacionalidade_id_seq minvalue 5
alter table nacionalidade alter idnacionalidade set default nextval('nacionalidade_id_seq')
alter sequence nacionalidade_id_seq owned by nacionalidade.idnacionalidade
insert into nacionalidade (nome) values ('Teste 1')
select * from nacionalidade

-- f) Pedido

select max(idpedido) + 1 from pedido
create sequence pedido_id_seq minvalue 16
alter table pedido alter idpedido set default nextval('pedido_id_seq')
alter sequence pedido_id_seq owned by pedido.idpedido
insert into pedido (data_pedido, valor, idcliente, idvendedor)
values (current_date, 1500, 17, 5)
select * from pedido

-- g) Pedido produto (verificar se é necessário)

-- h) Profissão

select max(idprofissao) + 1 from profissao
create sequence profissao_id_seq minvalue 6
alter table profissao alter idprofissao set default nextval('profissao_id_seq')
alter sequence profissao_id_seq owned by profissao.idprofissao
insert into profissao (nome) values ('Doutor')
select * from profissao

-- i) Transportadora

select max(idtransportadora) + 1 from transportadora
create sequence transportadora_id_seq minvalue 3
alter table transportadora alter idtransportadora set default nextval('transportadora_id_seq')
alter sequence transportadora_id_seq owned by transportadora.idtransportadora
insert into transportadora (nome) values ('Teste 1')
select * from transportadora

-- j) UF

select max(iduf) + 1 from uf 
create sequence uf_id_seq minvalue 7
alter table uf alter iduf set default nextval('uf_id_seq')
alter sequence uf_id_seq owned by uf.iduf
insert into uf (nome, sigla) values ('Roraima', 'RR')
select * from uf

-- k) Vendedor

select max(idvendedor) + 1 from vendedor
create sequence vendedor_id_seq minvalue 9
alter table vendedor alter idvendedor set default nextval('vendedor_id_seq')
alter sequence vendedor_id_seq owned by vendedor.idvendedor
insert into vendedor (nome) values ('Jorge')
select * from vendedor

-- Campos Default

alter table pedido alter column data_pedido set default current_date;
-- definiu que as tabelas serão preenchidas por datas - especificamente a data do dia - quando não informado
alter table pedido alter column valor set default 0;
-- definiu que as tabelas serão preenchidas pelo número 0 quando não for definidio nenhum valor
insert into pedido (idcliente, idvendedor) values (1,1)
select * from pedido

-- Exercícios -> valores default

-- 1. Adicione valores na tabela de produtos do pedido

-- a) Quantidade com o valor 1
alter table pedido_produto alter column quantidade set default 1;
-- b) Valor unitário com o valor 0
alter table pedido_produto alter column valor_unitario set default 0;

-- 2. Adicione valor default na tabela de produtos
-- a) Valor com o valor 0
alter table produto alter column valor set default 0;

-- Índices 

create index idx_cln_nome on cliente (nome);

-- Exercícios -> Índices

-- 1. Adicione índices nas seguintes tabelas e campos

-- a) Pedido - data do pedido

create index idx_pdd_dataPdd on pedido (data_pedido);

-- b) Produto - nome

create index idx_prd_nome on produto (nome);