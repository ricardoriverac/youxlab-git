-- AVALIAÇÃO PRÁTICA - BANCO DE DADOS

-- 1- Criação do banco de dados BIBLIOTECA

-- 2
create table editora (
	ideditora integer not null,
	nome varchar(50) not null,

	constraint pk_ed_id primary key (ideditora),
	constraint un_ed_nome unique (nome)
)

create sequence editora_id_seq minvalue 1
alter table editora alter ideditora set default nextval('editora_id_seq')
alter sequence editora_id_seq owned by editora.ideditora

-- 3
insert into editora (nome) values ('Bookman'), ('Edgard Blusher'), ('Nova Terra'), ('Brasport')

-- 4
create table categoria (
	idcategoria integer not null,
	nome varchar(50) not null,

	constraint pk_ctg_id primary key (idcategoria),
	constraint un_ctg_nome unique (nome)
)

create sequence categoria_id_seq minvalue 1
alter table categoria alter idcategoria set default nextval('categoria_id_seq')
alter sequence categoria_id_seq owned by categoria.idcategoria

-- 5
insert into categoria (nome) values ('Banco de Dados'), ('HTML'), ('Java'), ('PHP')

select * from categoria

-- 6
create table autor (
	idautor integer not null,
	nome varchar(50) not null,

	constraint pk_aut_id primary key (idautor),
	constraint un_aut_nome unique (nome)
)

create sequence autor_id_seq minvalue 1
alter table autor alter idautor set default nextval('autor_id_seq')
alter sequence autor_id_seq owned by autor.idautor

-- 7
insert into autor (nome)
values ('Waldemar Setzer'),
	('Flávio Soares'),
	('John Watson'),
	('Rui Rossi dos Santos'),
	('Antonio Pereira de Resende'),
	('Claudiney Calixto Lima'),
	('Evandro Carlos Teruel'),
	('Ian Graham'),
	('Fabrício Xavier'),
	('Pablo Dalloglio')

select * from autor

-- 8
create table livro (
	idlivro integer not null,
	ideditora integer not null,
	idcategoria integer not null,
	nome varchar(100) not null,

	constraint pk_liv_id primary key (idlivro),
	constraint fk_ed_ideditora foreign key (ideditora) references editora (ideditora),
	constraint fk_ctg_idcategoria foreign key (idcategoria) references categoria (idcategoria),
	constraint un_liv_nome unique (nome)
)

create sequence livro_id_seq minvalue 1
alter table livro alter idlivro set default nextval('livro_id_seq')
alter sequence livro_id_seq owned by livro.idlivro

-- 9
insert into livro (ideditora, idcategoria, nome)
values
	(2, 1, 'Banco de Dados - 1 Edição'),
	(1, 1, 'Oracle DataBase 11G Administração'),
	(3, 3, 'Programação de Computadores em Java'),
	(4, 3, 'Programação Orientada a Aspectos em Java'),
	(4, 2, 'HTML5 - Guia Prático'),
	(3, 2, 'XHTML: Guia de Referência para Desenvolvimento na Web'),
	(1, 4, 'PHP para Desenvolvimento Profissional'),
	(2, 4, 'PHP com Programação Orientada a Objetos')

select * from livro

-- 10
create table livro_autor (
	idlivro integer not null,
	idautor integer not null,

	constraint pk_liv_aut_idlivro_idautor primary key (idlivro, idautor),
	constraint fk_liv_idlivro foreign key (idlivro) references livro (idlivro),
	constraint fk_aut_idautor foreign key (idautor) references autor (idautor)
)

-- 11
insert into livro_autor
values
	(1,1),
	(1,2),
	(2,3),
	(3,4),
	(4,5),
	(4,6),
	(5,7),
	(6,8),
	(7,9),
	(8,10)

select * from autor

-- 12
create table aluno (
	idaluno integer not null,
	nome varchar(50) not null,

	constraint pk_aln_idaluno primary key (idaluno)
)

create sequence aluno_id_seq minvalue 1
alter table aluno alter idaluno set default nextval('aluno_id_seq')
alter sequence aluno_id_seq owned by aluno.idaluno

-- 13
insert into aluno (nome) values ('Mario'), ('João'), ('Paulo'), ('Pedro'), ('Maria')

-- 14
create table emprestimo (
	idemprestimo integer not null,
	idaluno integer not null,
	data_emprestimo date not null,
	data_devolucao date not null,
	valor numeric(10,2) not null,
	devolvido char(1) not null,

	constraint pk_emp_idemprestimo primary key (idemprestimo),
	constraint fk_aln_idaluno foreign key (idaluno) references aluno (idaluno)
)

create sequence emprestimo_id_seq minvalue 1
alter table emprestimo alter idemprestimo set default nextval('emprestimo_id_seq')
alter sequence emprestimo_id_seq owned by emprestimo.idemprestimo

alter table emprestimo alter column data_emprestimo set default current_date;

-- 15
insert into emprestimo
	(idaluno, data_emprestimo, data_devolucao, valor, devolvido)
values
	(1,'2012-05-02','2012-05-12',10,'S'),
	(1,'2012-04-23','2012-05-03',5,'N'),
	(2,'2012-05-10','2012-05-20',12,'N'),
	(3,'2012-05-10','2012-05-20',8,'S'),
	(4,'2012-05-05','2012-05-15',15,'N'),
	(5,'2012-05-07','2012-05-17',20,'S'),
	(4,'2012-05-08','2012-05-18',5,'S')

-- 16
create table emprestimo_livro (
	idemprestimo integer not null,
	idlivro integer not null,

	constraint pk_idemp_idliv primary key (idemprestimo, idlivro),
	constraint fk_emp_idemprestimo foreign key (idemprestimo) references emprestimo (idemprestimo),
	constraint fk_liv_idlivro foreign key (idlivro) references livro (idlivro)
)

-- 17
insert into emprestimo_livro (idemprestimo, idlivro)
values
	(1,1),
	(2,4),
	(2,3),
	(3,2),
	(3,7),
	(4,5),
	(5,4),
	(6,6),
	(6,1),
	(7,8)

-- 18
create index idx_emp_data_emprestimo on emprestimo (data_emprestimo)
create index idx_emp_data_devolucao on emprestimo (data_devolucao)

-- Consultas simples
-- 19
select * from autor order by nome asc

-- 20
select * from aluno where nome like 'P%'

-- 21
select * from livro where idcategoria = 1 or idcategoria = 3

-- 22
select * from livro where ideditora = 1

-- 23
select * from emprestimo where data_emprestimo between '2012-05-05' and '2012-05-10'

-- 24
select * from emprestimo where data_emprestimo not between '2012-05-05' and '2012-05-10'

-- 25
select * from emprestimo where devolvido = 'S'

-- Consultas com agrupamentos simples
-- 26
select count(idlivro) as quantidade_livro from emprestimo_livro group by idlivro

-- 27
select sum(valor) from emprestimo group by idemprestimo

-- 28
select avg(valor) from emprestimo group by idemprestimo

-- 29
select max(valor) from emprestimo group by idemprestimo

-- 30
select min(valor) from emprestimo group by idaluno

-- 31
select sum(valor) from emprestimo where data_emprestimo between '2012-05-05' and '2012-05-10' 

-- 32
select count(idemprestimo) from emprestimo where data_emprestimo between '2012-05-01' and '2012-05-05' 

-- 33
create view info_livro as
select
	liv.nome as Livro,
	ctg.nome as Categoria,
	edt.nome as Editora
from
	livro liv
left outer join
	categoria ctg on ctg.idcategoria = liv.idcategoria
left outer join
	editora edt on edt.ideditora = liv.ideditora

-- 34
create view ds as
select
	liv.nome as livro,
	aut.nome as autor
from
	livro_autor liv_aut
left outer join
	livro liv on liv.idlivro = liv_aut.idlivro
left outer join
	autor aut on aut.idautor = liv_aut.idautor

-- 35
select
	liv.nome as livro,
	aut.nome as autor
from
	livro_autor liv_aut
left outer join
	livro liv on liv.idlivro = liv_aut.idlivro
left outer join
	autor aut on aut.idautor = liv_aut.idautor
where
	aut.nome = 'Ian Graham'

-- 36
select
	aln.nome,
	emp.data_emprestimo,
	emp.data_devolucao
from
	emprestimo emp
left outer join
	aluno aln on aln.idaluno = emp.idaluno

-- 37
select
	liv.nome
from
	emprestimo_livro emp_liv
left outer join
	livro liv on liv.idlivro = emp_liv.idlivro

-- Consultas com agrupamento + join
-- 38
select
	edt.nome,
	count(idlivro)
from
	livro liv
left outer join
	editora edt on edt.ideditora = liv.ideditora
group by edt.nome

-- 39
select
	ctg.nome,
	count(idlivro)
from
	livro liv
left outer join
	categoria ctg on ctg.idcategoria = liv.idcategoria
group by
	ctg.nome

-- 40
select
	aut.nome,
	count(idlivro)
from
	livro_autor liv_aut
left outer join
	autor aut on aut.idautor = liv_aut.idautor
group by
	aut.nome

-- 41
select
	aln.nome,
	count(idemprestimo)
from
	emprestimo emp
left outer join
	aluno aln on aln.idaluno = emp.idaluno
group by
	aln.nome

-- 42
select
	aln.nome,
	sum(valor)
from
	emprestimo emp
left outer join
	aluno aln on aln.idaluno = emp.idaluno
group by
	aln.nome

-- 43
select
	aln.nome,
	sum(valor)
from
	emprestimo emp
left outer join
	aluno aln on aln.idaluno = emp.idaluno
group by
	aln.nome
having
	sum(valor) > 7.00

-- 44
select upper(nome) from aluno order by nome desc

-- 45
select
	*
from
	emprestimo
where
	extract(month from data_emprestimo) = 4

-- 46
select
	idemprestimo,
	idaluno,
	data_emprestimo,
	data_devolucao,
	valor,
	case devolvido
		when 'S' then 'Devolução completa'
		when 'N' then 'Em atraso'
	end as situacao
from
	emprestimo

-- 47
select
	substring(nome from 5 for 10)
from
	autor

-- 48
select
	valor,
	case extract(month from data_emprestimo)
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
	else
		'Não informado'
	end as mes
from
	emprestimo

-- 49
select
	data_emprestimo,
	valor
from
	emprestimo
where
	valor > (select avg(valor) from emprestimo)

-- 50
select
	eml.idemprestimo,
	data_emprestimo,
	valor
from
	emprestimo_livro eml
left outer join
	emprestimo emp on emp.idemprestimo = eml.idemprestimo
group by
	eml.idemprestimo,
	data_emprestimo,
	valor
having
	count(idlivro) > 1

-- 51
select
	data_emprestimo,
	valor
from
	emprestimo emp
where
	valor < (select sum(valor) from emprestimo)