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