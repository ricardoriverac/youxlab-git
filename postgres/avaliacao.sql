-- AVALIAÇÃO

-- 2. Crie uma tabela chamada EDITORA, de acordo com os dados disponibilizados

create table editora(

	ideditora serial not null,
	nome varchar(50) not null,
	
	constraint pk_edt_ideditora primary key (ideditora),
	constraint un_edt_nome unique (nome)
)

-- 3. Insira os dados abaixo na tabela editora
-- a) Bookman
-- b) Edgard Blusher 
-- c) Nova Terra
-- d) Brasport

insert into editora (nome) values ('Bookman')
insert into editora (nome) values ('Edgard Blusher');
insert into editora (nome) values ('Nova Terra');
insert into editora (nome) values ('Brasport');
select * from editora

-- 4. Crie uma tabela chamada Categoria, de acordo com os dados entregues

create table categoria (
	idcategoria serial not null,
	nome varchar(50) not null,

	constraint pk_cat_idcategoria primary key (idcategoria),
	constraint un_cat_nome unique (nome)
);



-- 5. Insira os dados na tabela categoria
insert into categoria (nome) values ('Banco de Dados');
insert into categoria (nome) values ('HTML');
insert into categoria (nome) values ('Java'), ('PHP')
select * from categoria

-- 6. Crie uma tabela chamada AUTOR

create table autor (
	idautor serial not null,
	nome varchar(50) not null,

	constraint pk_aut_idautor primary key (idautor),
	constraint un_aut_nome unique (nome)
);

-- 7. Insira os dados abaixo na tabela AUTOR

insert into autor (nome) values ('Waldemar Setzer'), ('Fláveio Soares'), ('John Watson'), ('Rui Rossi dos Santos'), ('Antonio Pereira de Resende'), ('Claudiney Calixto Lima'), ('Evandro Carlos Teruel'), ('Ian Graham'), ('Fabricio Xavier'), ('Pablo Dailoglio')

-- 8. Crie uma tabela chamada LIVRO

create table livro (
	idlivro serial not null, 
	ideditora integer not null,
	idcategoria integer not null,
	nome varchar(50) not null,

	constraint pk_lvr_idlivro primary key(idlivro),
	constraint fk_lvr_ideditora foreign key(ideditora) references editora (ideditora),
	constraint fk_lvr_idcategoria foreign key(idcategoria) references categoria (idcategoria),
	constraint un_lvr_nome unique (nome)
);
drop table livro
-- 9. Insira os dados na tabela
select * from editora
select * from categoria
insert into livro (ideditora, idcategoria, nome) 
values
(1, 1, 'Oracle DataBase 11G Administração'),
(4, 3, 'Programação de Computadores em Java'),
(4, 3, 'Programação Orientada a Aspectos em Java'),
(3, 2, 'HTML5 - Guia Prático'),
(1, 2, 'XHTML: Guia de Referência para Desenvolvimento'),
(2, 4, 'PHP para Desenvolvimento Profissional'),
(2, 4, 'PHP com Programação Orientada a Objetos')

-- 10. Crie uma tabela chamada Livro_Autor

create table livro_autor (
	idlivro integer not null,
	idautor integer not null,

	constraint pk_lvat_idlivroautor primary key (idlivro, idautor),
	constraint fk_lvat_idlivro foreign key (idlivro)  references livro (idlivro),
	constraint fk_lvat_idautor foreign key (idautor) references autor (idautor)
);

-- 11. Insira os dados
select * from livro
select * from autor
insert into livro_autor (
	idlivro,
	idautor
)
values 
(1, 1),
(1, 2),
(2, 3),
(3, 4),
(4, 5),
(5, 6),
(6, 7)
insert into livro_autor (
	idlivro,
	idautor
)
values 
(7, 8),
(8, 9)
-- 12. Crie uma tabela chamada ALUNO, de acordo com os dados abaixo

create table aluno (
	idaluno serial not null,
	nome varchar(50) not null,

	constraint pk_aln_idaluno primary key (idaluno),
	constraint un_aln_nome unique (nome)
)

--- 13. Insira os dados

insert into aluno (nome) values ('Mario'), ('João'), ('Paulo'), ('Pedro'), ('Maria')

-- 14. Crie uma tabela chamada Empréstimo

create table emprestimo (
	idemprestimo serial not null,
	idaluno integer not null,
	data_emprestimo date not null default current_date,
	data_devolucao date not null default current_date,
	valor float not null default 0,
	devolvido char(1) not null,

	constraint pk_emp_idemprestimo primary key (idemprestimo),
	constraint fk_emp_idaluno foreign key (idaluno) references aluno (idaluno)
)
drop table emprestimo
-- 15. Insira os dados
select * from aluno
insert into emprestimo (idaluno, data_emprestimo, data_devolucao, valor, devolvido)
values
(1, '2012-05-12', '2012-05-12', 10, 'S'),
(1, '2012-04-23', '2012-05-03', 5, 'N'),
(2, '2012-05-10', '2012-05-20', 12, 'N'),
(3, '2012-05-10', '2012-05-20', 8, 'S'),
(4, '2012-05-05', '2012-05-15', 15, 'N'),
(4, '2012-05-07', '2012-05-17', 20, 'S'),
(4, '2012-05-08', '2012-05-18', 5, 'S')
select * from emprestimo
-- 16. Crie uma tabela chamada EMPRETIMO_LIVRO

create table emprestimo_livro (
	idemprestimo integer not null,
	idlivro integer not null,

	constraint pk_emli_idemplivro primary key (idemprestimo, idlivro),
	constraint fk_emli_idemprestimo foreign key (idemprestimo) references emprestimo(idemprestimo),
	constraint fk_emli_idlivro foreign key (idlivro) references livro (idlivro)
)
select * from livro
-- 17. Insira os dados abaixo na tabela

insert into emprestimo_livro (idemprestimo, idlivro) values
(1, 1),
(2, 3),
(2, 2),
(3, 2),
(3, 7),
(4, 5),
(5, 4),
(6, 6),
(6, 1),
(7, 8)

-- 18. Crie os seguintes índices

create index indx_emp_emp on emprestimo (idemprestimo)
create index indx_emp_devo on emprestimo (data_devolucao)

-- CONSULTAS SIMPLES

-- 19. O nome dos autores em ordem alfabética

select nome from autor order by nome asc

-- 20. O nome dos alunos que começam com a letra P

select nome from autor where nome ilike 'P%'

-- 21. O nome dos livros da categoria Banco de dados OU Java
select * from livro
select nome, categoria from livro where idcategoria = 1 or idcategoria = 3

-- 22. O nome dos livros da editora Bookman
select * from editora
select nome from livro where ideditora = 1

-- 23. Os empréstimos que não foram feitos entre 05/05/2012 e 10/05/2012

select * from emprestimo where data_emprestimo between '2012-05-05' and '2012-05-10'

-- 24. Os empréstimos que não foram feitos entre 05/05/2012 e 10/05/2012]

select * from emprestimo where data_emprestimo not between '2012-05-05' and '2012-05-10'

-- 25. Os empréstimos que os livros já foram devolvidos


select * from emprestimo where devolvido ilike 'S'

-- CONSULTAS COM AGRUPAMENTO SIMPLES

-- 26. A quantidade de livros

select sum(idlivro) from livro

-- 27. O somatório do valor dos empréstimos

select * from emprestimo
select sum(valor) from emprestimo

-- 28. A média do valor dos empréstimos

select avg(valor) from emprestimo

-- 29. O maior valor dos empréstimos

select max(valor) from emprestimo

-- 30. O menor valor dos empréstios

select min(valor) from emprestimo

-- 31. O somatório do valor do empréstimo que estão entre 05/05/2012

select sum(Valor) from emprestimo where data_emprestimo between '2012-05-05' and '2012-05-10'

-- 32. A quantidade de empréstimos que estão entre 01/05/2012 e 05/05/2012

select count(idemprestimo) from emprestimo where data_emprestimo between '2012-05-01' and '2012-05-05'

-- CONSULTAS COM JOIN

-- 33. O nome do livro, a categoria e a editora (LIVRO) - fazer uma view

select 
	lvr.nome,
	edt.nome
from livro lvr
left outer join
	editora edt on lvr.ideditora = edt.ideditora

-- 34. O nome do livro e o nome do autor (LIVRO_AUTOR) - fazer uma view

select
	lvr.nome as livro,
	aut.nome as autor
from livro_autor lvat
left outer join
	livro lvr on lvat.idlivro = lvr.idlivro
left outer join
	autor aut on lvat.idautor = aut.idautor

-- 35. O nome dos livros do autor Ian Graham (LIVRO_AUTOR)
select * from autor
select 
	lvr.nome as livro
from livro_autor lvat
left outer join
	livro lvr on lvat.idlivro = lvr.idlivro
left outer join
	autor aut on lvat.idautor = aut.idautor
where aut.idautor = 8


-- 36. O nome do aluno, a data do emŕéstimo e a data de devolução (EMPRESTIMO)

select
	aln.nome as Aluno,
	emp.data_emprestimo as "Data do Empréstimo",
	emp.data_devolucao as "Data de Devolução"
from emprestimo emp
left outer join
	aluno aln on emp.idaluno = aln.idaluno

-- 37. O nome de todos os livro sque foram emprestados (emprestimo_livro)
select * from emprestimo_livro
select
	lvr.nome as livro
from emprestimo_livro eplv
left outer join
	livro lvr on eplv.idlivro = lvr.idlivro
left outer join
	emprestimo epm on eplv.idemprestimo = epm.idemprestimo
where 
	epm.devolvido ilike 'S'

-- CONSULTAS COM AGRUPAMENTO + JOIN

-- 38. O nome da editora e a quantidade de livros de cada editora (LIVRO)

select * from livro
select
	edt.nome as editora,
	count(lvr.idlivro)
from livro lvr
left outer join
	editora edt on lvr.ideditora = edt.ideditora
group by edt.nome
-- 39. O nome da categoria e a quantidade de livros de cada categoria (LIVRO)

select
	cat.nome as categora,
	count(lvr.idlivro) as total
from livro lvr
left outer join
	categoria cat on lvr.idcategoria = cat.idcategoria
group by cat.nome

-- 40. O nome do autor e a quantidade de livros de cada autor (LIVRO_AUTOR)
select * from livro
select
	aut.nome as autor,
	count(lvr.idlivro)
from livro_autor lvat
left outer join
	autor aut on lvat.idautor = aut.idautor
left outer join
	livro lvr on lvat.idlivro = lvr.idlivro
group by aut.nome
-- 41. O nome do aluno e a quantidade de empréstimo de cada aluno (EMPRESTIMO_LIVRO)

select
	aln.nome as aluno,
	count(emp.idemprestimo)
from emprestimo emp
left outer join
	aluno aln on aln.idaluno = emp.idaluno
group by aln.nome
-- 42. O nome do aluno e o do valor total dos empréstimos de cada aluno (EMPRESTIMO)


select
	aln.nome as aluno,
	sum(emp.valor) as total
from emprestimo emp
left outer join
	aluno aln on emp.idaluno = aln.idaluno
group by aln.nome

-- 43. O nome do aluno e o somatório do valor total dos empréstimo de cada aluno somente daqueles que o somatório for mairo do e 7 (EMPRESTIMO)

select
	aln.nome as aluno,
	sum(epm.valor)
from emprestimo epm
left outer join
	aluno aln on epm.idaluno = aln.idaluno
group by aln.nome
having sum(epm.valor) > 7
-- CONSULTAS COMANDOS DIVERSOS

-- 44. O nome de todos os alunos em ordem decrescente e em letra maiúscula

select lower(nome) from aluno order by nome desc 

-- 45. Os empréstimos que foram feitos no mês 04 de 2012

select * from emprestimo where data_emprestimo between '2012-04-01' and '2012-04-30'

-- 46. Todos os campos do empréstimo. Caso já tenha sido devolvido, mostrar a mensagem "Devolução Completa", senão "Em atraso"
select * from emprestimo
select
	*, 
	case devolvido
		when 'N' then 'Não devolvido'
	else 'Devolvido'
	end as awnser
from emprestimo

-- 47. SOmente o caractere 5 até o caractere 10 do nome dos autores

select
	substring(nome from 5 for 10)
from autor

-- 48. O valor do empréstimo e somente o mÊs de data de empréstimo. EScreva "Janeiro", "Fevereiro", etc

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
	end as meses
from emprestimo
-- SUBCONSULTAS

-- 49. A data do empréstimo e o valor dos empréstimos que o valor seja maior que a média de todos os empréstimos

select
	data_emprestimo,
	valor
from emprestimo
where valor > (select avg(valor) from emprestimo)
-- 50. A data do empréstimo e o valor dos empréstimos que possuem mais de um livro

select * from emprestimo_livro
select
	emp.data_emprestimo,
	emp.valor,
	(select count(emlv.idemprestimo) from emprestimo_livro emlv where emlv.idemprestimo = emp.idemprestimo)
from emprestimo emp
where (select count(emlv.idemprestimo) from emprestimo_livro emlv where emlv.idemprestimo = emp.idemprestimo) > 1
-- 51. A data do empréstimo e o valor dos empréstimos que o valor seja menor que a soma de todos os empréstimos

select
	data_emprestimo,
	valor
from emprestimo
where valor < (select sum(valor) from emprestimo)