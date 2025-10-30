insert into clientes (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, municipio, uf) values ('16', 'Maicon', '12349596421', '1234', '10-10-1995', 'F', 'Empresário', 'Florianópolis', 'PR');
insert into clientes (idcliente, nome, rg, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro,  municipio, uf) values ('17', 'Getúlio', '4631', 'F', 'Estudante', 'Brasileira', 'Rua central', '343', 'Apartamento', 'Centro', 'Curitiba', 'SC');
insert into clientes (idcliente, nome, genero, profissao, nacionalidade, numero, complemento) values ('18', 'Sandra', 'M', 'Professor', 'Italiana', '12', 'Bloco A');
update clientes set cpf = '45390569432' where idcliente = 16;
update clientes set genero = 'M', nacionalidade = 'Brasileira', uf = 'SC' where  idcliente = 16;
update clientes set genero = 'M', data_nascimento = '01-04-1978' where idcliente = 17;
update clientes set genero = 'F', profissao= 'Professora', numero= '123' where idcliente = 18;
select * from clientes;
delete from clientes where idcliente = '16';
select * from clientes;
delete from clientes where idcliente= '18';
select * from clientes;

create table profissao(
	idprofissao integer not null,
	nome varchar(30) not null,

	constraint pk_prf_idprofissao primary key (idprofissao),
	constraint un_prf_nome unique (nome)
);
select profissao from clientes;
insert into profissao (idprofissao, nome) values (1, 'Engenheiro');
insert into profissao (idprofissao, nome) values (2, 'Pedreiro');
insert into profissao (idprofissao, nome) values (3, 'Jornalista');
insert into profissao (idprofissao, nome) values (4, 'Professor');
insert into profissao (idprofissao, nome) values (6, 'Professora');
insert into profissao (idprofissao, nome) values (7, 'Estudante');

create table nacionalidade(
	idnacionalidade integer not null,
	nome varchar(30) not null,

	constraint pk_nac_idnacionalidade primary key (idnacionalidade),
	constraint un_nac_nome unique (nome)
);
select nacionalidade from clientes;
insert into nacionalidade (idnacionalidade, nome) values (1, 'Brasileira');
insert into nacionalidade (idnacionalidade, nome) values (2, 'Italiana');
insert into nacionalidade (idnacionalidade, nome) values (3, 'Brasileiro');
insert into nacionalidade (idnacionalidade, nome) values (4, 'Italiano');
insert into nacionalidade (idnacionalidade, nome) values (5, 'Norte americana');
insert into nacionalidade (idnacionalidade, nome) values (6, 'Alemã');
insert into nacionalidade (idnacionalidade, nome) values (7, 'Alemão');

create table complemento(
	idcomplemento integer not null,
	nome varchar(30) not null,

	constraint pk_compl_idcomplemento primary key (idcomplemento),
	constraint un_compl_nome unique (nome)
);
select complemento from clientes;
insert into complemento (idcomplemento, nome) values (1, 'Apartamento');
insert into complemento (idcomplemento, nome) values (2, 'Casa');

create table bairro(
	idbairro integer not null,
	nome varchar(30) not null,

	constraint pk_brr_idbairro primary key (idbairro),
	constraint un_brr_nome unique (nome)
);
select bairro from clientes;
insert into bairro (idbairro, nome) values (1, 'Centro');
insert into bairro(idbairro, nome) values (2, 'São Pedro');
insert into bairro(idbairro, nome) values (3, 'Santa Rosa');
insert into bairro (idbairro, nome) values (4, 'Cidade Nova');

alter table clientes rename column "idprofissao;" to "idprofissao";
select * from clientes;
alter table clientes drop idprofissao;
alter table clientes add idprofissao integer;
alter table clientes add constraint fk_cln_idprofissao foreign key (idprofissao) references profissao(idprofissao);
update clientes set idprofissao = 1 where idcliente in (1,9, 10, 12,15,17);
update clientes set idprofissao = 2 where idcliente= 2;
update clientes set idprofissao = 3 where idcliente = 3;
update clientes set idprofissao = 4 where idcliente in (4, 5);
update clientes set idprofissao = 6 where idcliente in (6, 7, 8, 13);
select * from profissao;

select * from clientes;
--Brasileira - 2, 3, 6, 10, 11, 14,, 17, 4, 1 
--Italiana - 3, 7
--Alemã - 9, 13
--Norte Americana -  8
alter table clientes drop nacionalidade;
alter table clientes add idnacionalidade integer;
alter table clientes add constraint fk_cln_idnacionalidade foreign key (idnacionalidade) references nacionalidade(idnacionalidade);
update clientes set idnacionalidade = 1 where idcliente in (2, 3, 6, 10, 11, 14, 17, 4, 1);
update clientes set idnacionalidade = 2 where idcliente in (3, 7);
update clientes set idnacionalidade = 5 where idcliente in (8);
update clientes set idnacionalidade = 6 where idcliente in (9, 13);

select * from nacionalidade

select * from complemento;
select * from clientes;
--Apartamento - 2, 3, 7, 17
--Casa - 4, 13, 15, 16
alter table clientes drop complemento;
alter table clientes add idcomplemento integer;
alter table clientes add constraint fk_cln_idcomplemento foreign key (idcomplemento) references complemento(idcomplemento);
update clientes set idcomplemento = 1 where idcliente in (2, 3, 7, 17);
update clientes set idcomplemento = 2 where idcliente in (4, 13, 15, 16);
select * from clientes;

select * from bairro;
select * from clientes;
--São Pedro - 5, 4
--Centro - 6, 8, 9, 2, 17, 3
--Cidade Nova - 1, 12, 13
--Santa Rosa - 7
alter table clientes drop bairro;
alter table clientes add idbairro integer;
alter table clientes add constraint fk_cln_idbairro foreign key (idbairro) references bairro(idbairro);
update clientes set idbairro = 1 where idcliente in (6, 8, 9, 2, 17, 3);
update clientes set idbairro = 2 where idcliente in (5, 4);
update clientes set idbairro = 3 where idcliente = 7;
update clientes set idbairro = 4 where idcliente in (1, 12, 13);