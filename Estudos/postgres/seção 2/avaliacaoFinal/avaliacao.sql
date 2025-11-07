create table EDITORA(
	idEditora serial not null,
	nome varchar(50) not null,

	constraint pk_edit_id primary key (idEditora),
	constraint un_edit_nome unique (nome)
);
insert into EDITORA (nome) values ('Bookman'), ('Edgard Blusher'), ('Nova Terra'), ('Brasport');

create table CATEGORIA(
	idCategoria serial not null,
	nome varchar(50) not null,

	constraint pk_cat_id primary key(idCategoria),
	constraint un_cat_nome unique (nome)
);

insert into CATEGORIA (nome) values ('Banco de Dados'), ('HTML'), ('Java'), ('PHP');

create table AUTOR(
	idAutor serial not null,
	nome varchar(50) not null,

	constraint pk_aut_id primary key(idAutor),
	constraint un_aut_nome unique(nome)
);

insert into AUTOR (nome) values ('Waldemar Setzer'), ('Flávio Soares'), ('John Watson'), ('Rui Rossi dos Santos'), ('Antonio Pereira Resende'), ('Claudiney Calixto de Lima'), ('Evando Carlos Teruel'), ('Ian Graham'), ('Fabricio Xavier'), ('Pablo Dalloglio');

create table LIVRO(
	idLivro serial not null,
	idEditora integer not null,
	idCategoria integer not null,
	nome varchar(50) not null,
	constraint pk_livro_id primary key(idLivro),
	constraint un_livro_nome unique (nome),
	foreign key (idEditora) references EDITORA (idEditora),
	foreign key (idEditora) references CATEGORIA(idCategoria)
);

select * from LIVRO;


select * from EDITORA;
select * from CATEGORIA;
	
insert into LIVRO (idEditora, idCategoria, nome) 
	values (2, 1, 'Banco de dados - 1 edição'),
		   (1, 1, 'Oracle DataBase 11G admnistração'),
		   (3, 3, 'Programação de computadores em java'),
		   (4, 3, 'Programação Orientada e Aspectos em Java'),
		   (4, 2, 'HTML5 - Guia Prático'),
		   (3, 2, 'XHTML: Guia de referência para desenvolvimento web'),
		   (1, 4, 'PHP para Desenvolvimento Profissional'),
		   (1, 4, 'PHP com Programação Orientada a Objetos');


create table LIVRO_AUTOR(
	idLivro integer not null,
	idAutor integer not null,
	constraint pk_livrat_idLivro_idAutor primary key (idLivro, idAutor),
	foreign key (idLivro) references LIVRO (idLivro),
	foreign key (idAutor) references AUTOR (idAutor)

);
select * from autor;
select * from LIVRO;
insert into LIVRO_AUTOR (idLivro, idAutor) values (1, 1), (1, 2), (2,3), (3, 4), (4, 5), (4, 6 ), (5, 7), (6, 8), (7, 9), (8, 10);

create table ALUNO(
	idALuno serial not null,
	nome varchar(30) not null,
	constraint pk_alun_idAluno primary key(idAluno)
);

insert into ALUNO (nome) values ('Mario'), ('João'), ('Paulo'), ('Pedro'), ('Maria');

create table EMPRESTIMO(
	idEmprestimo serial not null,
	idAluno integer not null,
	data_Emprestimo date default current_date,
	data_Devolucao date not null,
	valor numeric (10,2) not null,
	devolvido char(1) not null,
	constraint pk_empr_idEmprestimo primary key (idEmprestimo),
	foreign key (idAluno) references ALUNO (idAluno)
	
);

insert into EMPRESTIMO(idAluno, Data_Emprestimo, data_Devolucao, valor, devolvido) values (1, '02-05-2012', '12-05-2012', 10, 'S'), (1, '23-04-2012', '03-05-2012', 5, 'N'), (2, '10-05-2012', '20-05-2012', 12, 'N'), (3, '10-05-2012', '20-05-2012', 8, 'S'), (4, '05-05-2012', '15-05-2012', 15, 'N'), (4, '07-05-2012', '17-05-2012', 20, 'S'), (4, '08-05-2012', '18-05-2012', 5, 'S');

create table EMPRESTIMO_LIVRO(
	idEmprestimo integer not null,
	idLivro integer not null,
	constraint pk_el_idEmprestimo_idLivro primary key (idEmprestimo, idLivro),
	foreign key (idEmprestimo) references EMPRESTIMO (idEmprestimo),
	foreign key (idLivro) references LIVRO(idLivro)
);


insert into EMPRESTIMO_LIVRO (idEmprestimo, idLivro) values (1, 1), (2,4), (2, 3), (3, 2), (3, 7), (4, 5), (5, 4), (6, 6), (6, 1), (7,8);

create index idx_emprestimo_emprestimo on EMPRESTIMO(data_Emprestimo);
create index idx_emprestimo_devolucao on EMPRESTIMO(data_Devolucao);


select nome from autor order by nome asc;
select nome from autor where nome like 'P%';
select * from livro;
select * from emprestimo;
select * from livro where idcategoria = 1 or idcategoria = 3;
select * from livro where ideditora = 1;
select * from emprestimo where data_emprestimo between '05-05-2012' and '10-05-2012';
select * from emprestimo where data_emprestimo not between '05-05-2012' and '10-05-2012';
select * from emprestimo where devolvido = 'S';

select count(idlivro) as quantidade_livros from livro;
select * from emprestimo;
select sum(valor) as valor_emprestimos from emprestimo;
select round(avg(valor)) as media_valores_emprestimos from emprestimo;
select max(valor) as maior_valor_emprestimos from emprestimo;
select min(valor) as menor_valor_emprestimos from emprestimo;
select sum(valor) as somatorio_valores from emprestimo where data_emprestimo  between '05-05-2012' and '10-05-2012';
select count(idemprestimo) as quantidade_emprestimo from emprestimo where data_emprestimo between '01-05-2012' and '05-05-2012';

create view LIVROS as
	select
		l.nome as livro,
		ctg.nome as categoria,
		edtr.nome as editora
	from livro as l
	left join categoria	as ctg		on l.idcategoria= ctg.idcategoria
	left join editora as edtr		on l.ideditora = edtr.ideditora;

select * from livros;

create view LIVROS_AUTORES as
	select
		l.nome as livro,
		a.nome as autor
	from livro_autor as autl
	left join livro as l		on autl.idlivro = l.idlivro
	left join autor as a		on autl.idautor = a.idautor;

select * from livros_autores;

create view LIVROS_IAN as
	select
		a.nome as autor,
		l.nome as livro 
	from livro_autor as autl
	left join autor as a		on autl.idautor = a.idautor
	left join livro as l 		on autl.idlivro = l.idlivro
	where a.nome = 'Ian Graham';

