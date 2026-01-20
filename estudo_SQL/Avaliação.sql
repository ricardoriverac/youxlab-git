-- AVALIAÇÃO --

-- 1. Crie um banco de dador chamado BIBLIOTECA.

-- 2. Crie uma tabela chamada EDITORA.
create table editora(
	ideditora serial not null, -- primery key
	nome varchar (50) not null, -- unique

	constraint pk_edt_ideditora primary key (ideditora),
	constraint un_edt_nome unique (nome)
)
-- 3. Insira os dados abaixo na tabela EDITORA.
insert into editora (nome) values ('Bookman');
insert into editora (nome) values ('Edgard Blusher');
insert into editora (nome) values ('Nova Terra');
insert into editora (nome) values ('Brasport');

select * from editora

-- 4. Crie uma tabela chamada CATEGORIA, de acordo com os dados abaixo
create table categoria (
	idcategoria serial not null, -- primary key
	nome varchar (50) not null, -- unique

	constraint pk_ctg_idcategoria primary key (idcategoria),
	constraint un_nome_nm unique (nome)
);

-- 5. Insira os dados abaixo na tabela CATEGORIA
insert into categoria (nome) values ('Banco de Dados');
insert into categoria (nome) values ('HTML');
insert into categoria (nome) values ('Java');
insert into categoria (nome) values ('PHP');

select * from categoria

-- 6. Crie uma tabela chamada AUTOR.
create table autor(
	idautor serial not null, --primary key
	nome varchar (50) not null, 

	constraint pk_at_idautor primary key (idautor)
)

-- 7. Insira os dados abaixo na tabela AUTOR
insert into autor (nome) values ('Waldemar Setzer');
insert into autor (nome) values ('Flávio Soares');
insert into autor (nome) values ('John Watson');
insert into autor (nome) values ('Rui Rossi dos Santos');
insert into autor (nome) values ('Antonio Pereira de Resende');
insert into autor (nome) values ('Claudiney Calixto Lima');
insert into autor (nome) values ('Evandro Carlos Teruel');
insert into autor (nome) values ('Lan Graham');
insert into autor (nome) values ('Fabrício Xavier');
insert into autor (nome) values ('Pablo Dalloglio');

select * from autor

-- 8. Crie uma tabela chamada LIVRO
create table livro(
	idlivro serial not null, -- primary key
	ideditora integer not null, -- foreign key / EDITORA
	idcategoria integer not null, -- foreign key / CATEGORIA
	nome varchar (50) not null, -- unique

	constraint pk_lvr_idlivro primary key (idlivro),
	constraint fk_lvr_ideditora foreign key (ideditora) references editora(ideditora),
	constraint fk_lvr_idcategoria foreign key (idcategoria) references categoria(idcategoria)
	
)

-- 9. Insira os dados na tabela LIVRO
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

-- 10. Crie uma tabela chamada LIVRO_AUTOR
create table livro_autor(
	idlivro integer not null, -- foreign key / LIVRO
	idautor integer not null, -- foreign key / AUTOR

	constraint fk_lvr_at_idlivro foreign key (idlivro) references livro(idlivro),
	constraint fk_lvr_at_idautor foreign key (idautor) references autor(idautor),
	constraint pk_lvr_at_idlivro_idautor primary key (idlivro, idautor)
)

-- 11. Insira os dados na tabela LIVRO_AUTOR
insert into livro_autor (idlivro, idautor)
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

select * from livro_autor

-- 12. Crie uma tabela chamada ALUNO

create table aluno (
	idaluno serial not null, -- primary key
	nome varchar (50) not null,

	constraint pk_aln_idaluno primary key (idaluno) 
)

-- 13. Insira os dados na tabela ALUNO
insert into aluno (nome)
values 
	('Mario'),
	('João'),
	('Paulo'),
	('Pedro'),
	('Maria')

select * from aluno

-- 14. Crie uma tabela chamada EMPRESTIMO
create table emprestimo(
	idemprestimo serial not null, -- primary key
	idaluno integer not null, -- foreing key / ALUNO
	data_emprestimo date not null, -- alter table pedido alter column data_pedido set default current_date;
	data_devolucao date not null, 
	valor numeric not null,
	devolucao char not null,

	constraint pk_ept_idemprestimo primary key (idemprestimo),
	constraint fk_aln_idaluno foreign key (idaluno) references aluno(idaluno)
)

-- 15. Insira os dados abaixo na tabela EMPRESTIMO.
insert into emprestimo (idaluno, data_emprestimo, data_devolucao, valor, devolucao)
values 
	(1,'2012-05-02','2012-05-12',10,'S'),
	(1,'2012-04-23','2012-05-03',5,'N'),
	(2,'2012-05-10','2012-05-20',12,'N'),
	(3,'2012-05-10','2012-05-20',8,'S'),
	(4,'2012-05-05','2012-05-15',15,'N'),
	(5,'2012-05-07','2012-05-17',20,'S'),
	(4,'2012-05-08','2012-05-18',5,'S')

alter table emprestimo alter column data_emprestimo set default current_date;

select * from emprestimo

-- 16. Crie uma tabela chamada EMPRESTIMO_LIVRO 
create table emprestimo_livro (
	idemprestimo integer not null, -- foreign key / EMPRESTIMO
	idlivro integer not null, -- foreign key / LIVRO

	constraint fk_ept_lvr_idemprestimo foreign key (idemprestimo) references emprestimo(idemprestimo),
	constraint fk_ept_lvr_idlivro foreign key (idlivro) references livro(idlivro),
	constraint pk_ept_lvr_idlivro_idemprestimo primary key (idlivro, idemprestimo)
)

-- 17. Insira os dados abaixo na tabela EMPRESTIMO_LIVRO
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

-- 18. Crie índeces
create index idx_emp_data_emprestimo on emprestimo (data_emprestimo)
create index idx_emp_data_devolucao on emprestimo (data_devolucao)

-- Consulta simples

-- 19.
select nome from autor order by nome

-- 20.
select nome from aluno where nome like 'P%'

-- 21.
select nome from livro where idcategoria = 1 or idcategoria = 3

-- 22.
select nome from livro where ideditora = 1

-- 23. 
select * from emprestimo where data_emprestimo between '05/05/2012' and '10/05/2012'

-- 24.
select * from emprestimo where data_emprestimo between '05/05/2012' and '10/05/2012'

-- 25.
select * from emprestimo where devolucao = 'S'

-- Consultas com agrupamentos simples 

-- 26
select count(idlivro) from livro 

-- 27.
select sum(valor) from emprestimo

-- 28.
select avg(valor) from emprestimo

-- 29.
select max(valor) from emprestimo

-- 30. 
select  min(valor) from emprestimo

-- 31.
select sum(valor) from emprestimo where data_emprestimo between '05/05/2012' and '10/05/2012'

-- 32.
select count(idemprestimo) from emprestimo where data_emprestimo between '01/05/2012' and '05/05/2012'

-- Consultas com join

-- 33.
create view info_livros as
select
	lvr.nome as livro,
	ctg.nome as categoria
from
	livro lvr
left outer join
	categoria ctg on ctg.idcategoria = lvr.idcategoria
left outer join 
	editora edt on edt.ideditora = lvr.ideditora

select * from info_livros

-- 34.
create view autor_livro as
select
	lvr.nome as livro,
	tr.nome as autor
from
	 livro_autor lvr_tr
left outer join 
	livro lvr on lvr.idlivro = lvr_tr.idlivro
left outer join
	autor tr on tr.idautor = lvr_tr.idautor

-- 35. 
select 
	lvr.nome as livro,
	tr.nome as autor
from
	livro_autor lvr_tr
left outer join
	autor tr on tr.idautor = lvr_tr.idautor
left outer join
	livro lvr on lvr.idlivro = tr.idautor
where
	lvr_tr.idautor = 8

-- 36.
select
	aln.nome as aluno,
	data_emprestimo,
	data_devolucao
from
	emprestimo epr
left outer join
	aluno aln on aln.idaluno = epr.idaluno

-- 37.
select
	lvr.nome
from
	emprestimo_livro epr_lvr
left outer join
	emprestimo epr on epr.idemprestimo = epr_lvr.idemprestimo
left outer join
	livro lvr on lvr.idlivro = epr_lvr.idlivro
where 
	devolucao = 'N'
	

-- Consultas com agrupamento + join

-- 38.
select * from livro

select
	edt.nome,
	count(lvr.nome)
from
	livro lvr
left outer join
	editora edt on edt.ideditora = lvr.ideditora
group by
	edt.nome

-- 39.
select * from categoria

select 
	ctg.nome,
	count(ctg.idcategoria)
from
	livro lvr
left outer join
	categoria ctg on ctg.idcategoria = lvr.idcategoria
group by
	ctg.nome
	
-- 40.
select * from livro

select
	tr.nome,
	count(idlivro)
from
	livro_autor lvr_tr
left outer join
	autor tr on tr.idautor = lvr_tr.idautor
group by
	tr.nome

-- 41.
select * from emprestimo_livro

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
select * from emprestimo

select
	aln.nome,
	sum(valor)
from
	emprestimo epr
left outer join
	aluno aln on aln.idaluno = epr.idaluno
group by
	aln.nome

-- 43.
select * from emprestimo

select
	aln.nome,
	sum(valor)
from
	emprestimo epr
left outer join
	aluno aln on aln.idaluno = epr.idaluno
where
	valor > 7
group by
	aln.nome

--  Consultas comandos diversos

-- 44.
select * from aluno order by idaluno desc;

-- 45. 
select
	*
from
	emprestimo
where
	extract(month from data_emprestimo) = 4

-- 46.
select
	idemprestimo,
	idaluno,
	data_emprestimo,
	data_devolucao,
	valor,
	case devolucao
		when 'S' then 'Devolução completa'
		when 'N' then 'Em atraso'
	else 'Não informado'
	end as devolucao
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


-- Subconsultas

-- 49.
select * from emprestimo

select
	data_emprestimo,
	valor
from
	emprestimo	
where
	valor > (select avg(valor) from emprestimo) 

-- 50.
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

-- 51.
select
	data_emprestimo,
	valor
from
	emprestimo emp
where
	valor < (select sum(valor) from emprestimo)	



























	

