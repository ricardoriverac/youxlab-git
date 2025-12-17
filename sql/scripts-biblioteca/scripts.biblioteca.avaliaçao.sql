create table editora (
	ideditora serial not null,
	nome varchar(50) not null,

	constraint pk_edt_ideditora primary key (ideditora), 
	constraint un_edt_nome unique (nome)
);	



insert into editora (nome) values ('bookman');
insert into editora (nome) values ('edgard bushler');
insert into editora (nome) values ('nova terra');
insert into editora (nome) values ('brasport');
select * from editora



create table categoria (
	idcategoria serial not null,
	nome varchar(50) not null,

	constraint pk_ctg_idcategoria primary key (idcategoria), 
	constraint un_ctg_nome unique (nome)
);	

insert into categoria (nome) values ('banco de dados');
insert into categoria (nome) values ('HTML');
insert into categoria (nome) values ('java');
insert into categoria (nome) values ('PHP');
select * from categoria


create table autor (
	idautor serial not null,
	nome varchar(50) not null,

	constraint pk_atr_idautor primary key (idautor), 
	constraint un_atr_nome unique (nome)
);

insert into autor (nome) values ('waldemar setzer');
insert into autor (nome) values ('flávio soares');
insert into autor (nome) values ('john watson');
insert into autor (nome) values ('rui rossi dos santos');
insert into autor (nome) values ('antonio perreira de resende');
insert into autor (nome) values ('cladiney calixo lima');
insert into autor (nome) values ('evandro carlos teruel');
insert into autor (nome) values ('ian graham');
insert into autor (nome) values ('fabrício xavier');
insert into autor (nome) values ('pablo dalloglio');
select * from autor 	



create table livro (
	idlivro serial not null,
	ideditora integer not null,
	idcategoria integer not null,
	nome varchar(50) not null,
	

	constraint pk_lrv_idautor primary key (idlivro), 
	constraint fk_lvr_ideditora foreign key (ideditora) references editora (ideditora),
	constraint fk_lvr_idcategoria foreign key (idcategoria) references categoria (idcategoria),
	constraint un_lvr_nome unique (nome)
);

alter table livro alter column nome type varchar(70);

insert into livro (ideditora, idcategoria, nome) values (2, 1, 'banco de dados - 1 edição');
insert into livro (ideditora, idcategoria, nome) values (1, 1, 'oracle database 11G administração');
insert into livro (ideditora, idcategoria, nome) values (3, 3, 'programação de computadores em java');
insert into livro (ideditora, idcategoria, nome) values (4, 3, 'programação orientada a aspectos em java');
insert into livro (ideditora, idcategoria, nome) values (4, 2, 'HTML5 guia prático');
insert into livro (ideditora, idcategoria, nome) values (3, 2, 'XHTML: guia de referêcia para desenvolvimento na web');
insert into livro (ideditora, idcategoria, nome) values (1, 4, 'PHP para desenvolvimento proficional');
insert into livro (ideditora, idcategoria, nome) values (2, 4, 'PHP com programação orientada a objetos');
select * from livro



create table livro_autor (
	idlivro integer  not null, 
	idautor integer  not null,

	constraint pk_ltr_idlivroautor primary key (idlivro, idautor),
	constraint fk_ltr_idlivro foreign key (idlivro) references livro (idlivro),
	constraint fk_ltr_idautor foreign key (idautor) references autor (idautor)  
);

insert into livro_autor (idlivro, idautor) values (6, 1);
insert into livro_autor (idlivro, idautor) values (6, 2);
insert into livro_autor (idlivro, idautor) values (7, 3);
insert into livro_autor (idlivro, idautor) values (8, 4);
insert into livro_autor (idlivro, idautor) values (9, 5);
insert into livro_autor (idlivro, idautor) values (9, 6);
insert into livro_autor (idlivro, idautor) values (10, 7);
insert into livro_autor (idlivro, idautor) values (11, 8);
insert into livro_autor (idlivro, idautor) values (12, 9);
insert into livro_autor (idlivro, idautor) values (13, 10);





















































































































