create table EDITORA(
	id serial not null,
	nome varchar(50) not null,

	constraint pk_edit_id primary key (id),
	constraint un_edit_nome unique (nome)
);
insert into EDITORA (nome) values ('Bookman'), ('Edgard Blusher'), ('Nova Terra'), ('Brasport');

create table CATEGORIA(
	id serial not null,
	nome varchar(50) not null,

	constraint pk_cat_id primary key(id),
	constraint un_cat_nome unique (nome)
);

insert into CATEGORIA (nome) values ('Banco de Dados'), ('HTML'), ('Java'), ('PHP');

create table AUTOR(
	id serial not null,
	nome varchar(50) not null,

	constraint pk_aut_id primary key(id),
	constraint un_aut_nome unique(nome)
);

insert into AUTOR (nome) values ('Waldemar Setzer'), ('Flávio Soares'), ('John Watson'), ('Rui Rossi dos Santos'), ('Antonio Pereira Resende'), ('Claudiney Calixto de Lima'), ('Evando Carlos Teruel'), ('Ian Graham'), ('Fabricio Xavier'), ('Pablo Dalloglio');

create table LIVRO(
	id serial not null,
	idEditora integer not null,
	idCategoria integer not null,
	nome varchar(50) not null,
	constraint pk_livro_id primary key(id),
	constraint un_livro_nome unique (nome),
	foreign key (id) references EDITORA (id),
	foreign key (id) references CATEGORIA(id)
);

select * from LIVRO;
drop table LIVRO;

insert into