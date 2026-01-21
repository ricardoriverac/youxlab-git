-- 1. criar tabela Editora
create table Editora (
    IdEditora serial primary key,
    Nome varchar(100) not null unique
);

-- 2. inserir dados em Editora
insert into Editora (Nome) values
('bookman'),
('edgard blusher'),
('nova terra'),
('brasport');

-- 1. criar tabela editora
create table Editora (
    Ideditora serial primary key,
    Nome varchar(100) not null unique
);

-- 2. inserir dados em editora
insert into Editora (Nome) values
('bookman'),
('edgard blusher'),
('nova terra'),
('brasport');

create table categoria (
    idcategoria serial primary key,
    nome varchar(100) not null unique
);
insert into categoria (nome) values
('banco de dados'),
('html'),
('java'),
('php');



create table autor (
    idautor serial primary key,
    nome varchar(100) not null
);

insert into autor (nome) values
('waldemar setzer'),
('flávio soares'),
('john watson'),
('rui rossi dos santos'),
('antonio pereira de resende'),
('claudiney calixto lima'),
('evandro carlos teruel'),
('ian graham'),
('fabrício xavier'),
('pablo dalloglio');


create table livro (
    idlivro serial primary key,
    ideditora int not null,
    idcategoria int not null,
    nome varchar(150) not null unique,

    foreign key (ideditora) references editora(ideditora),
    foreign key (idcategoria) references categoria(idcategoria)
);
insert into livro (ideditora, idcategoria, nome) values
(2, 1, 'Banco de Dados – 1 Edição'),
(1, 1, 'Oracle DataBase 11G Administração'),
(3, 3, 'Programação de Computadores em Java'),
(4, 3, 'Programação Orientada a Aspectos em Java'),
(4, 2, 'HTML5 – Guia Prático'),
(3, 2, 'XHTML: Guia de Referência para Desenvolvimento na Web'),
(1, 4, 'PHP para Desenvolvimento Profissional'),
(2, 4, 'PHP com Programação Orientada a Objetos');

create table livro_autor (
    idlivro int not null,
    idautor int not null,
    primary key (idlivro, idautor),

    foreign key (idlivro) references livro(idlivro),
    foreign key (idautor) references autor(idautor)
);

insert into livro_autor (idlivro, idautor) values
(1, 1),  -- banco de dados – 1 edição / waldemar setzer
(1, 2),  -- banco de dados – 1 edição / flávio soares
(2, 3),  -- oracle database 11g administração / john watson
(3, 4),  -- programação de computadores em java / rui rossi dos santos
(4, 5),  -- programação orientada a aspectos / antonio pereira de resende
(4, 6),  -- programação orientada a aspectos / claudiney calixto lima
(5, 7),  -- html5 – guia prático / evandro carlos teruel
(6, 8),  -- xhtml guia / ian graham
(7, 9),  -- php prof / fabricio xavier
(8, 10); -- php poo / pablo dalloglio



create table aluno (
    idaluno serial primary key,
    nome varchar(100) not null
);

insert into aluno (nome) values
('mario'),
('joão'),
('paulo'),
('pedro'),
('maria');

-- criar tabela emprestimo
create table emprestimo (
    idemprestimo serial primary key,
    idaluno int not null,
    data_emprestimo date not null default current_date,
    data_devolucao date not null,
    valor decimal(10,2) not null,
    devolvido char(1) not null,
    foreign key (idaluno) references aluno(idaluno)
);

-- inserir dados em emprestimo
-- mario  → id 1
-- joão   → id 2
-- paulo  → id 3
-- pedro  → id 4

insert into emprestimo (idaluno, data_emprestimo, data_devolucao, valor, devolvido) values
(1, '2012-05-02', '2012-05-12', 10.00, 'S'),
(1, '2012-04-23', '2012-05-03', 5.00,  'N'),
(2, '2012-05-10', '2012-05-20', 12.00, 'N'),
(3, '2012-05-10', '2012-05-20', 8.00,  'S'),
(4, '2012-05-05', '2012-05-15', 15.00, 'N'),
(4, '2012-05-07', '2012-05-17', 20.00, 'S'),
(4, '2012-05-08', '2012-05-18', 5.00,  'S');


create table Emprestimo_Livro (
    IdEmprestimo int not null,
    IdLivro int not null,
    primary key (IdEmprestimo, IdLivro),

    foreign key (IdEmprestimo) references Emprestimo(IdEmprestimo),
    foreign key (IdLivro) references Livro(IdLivro)
);


insert into Emprestimo_Livro values
(1, 1),  -- primeiro empréstimo do mário → banco de dados – 1 edição
(2, 4),  -- segundo empréstimo do mário → programação orientada a aspectos em java
(2, 3),  -- segundo empréstimo do mário → programação de computadores em java
(3, 2),  -- empréstimo do joão → oracle database 11g administração
(3, 7),  -- empréstimo do joão → php para desenvolvimento profissional
(4, 5),  -- empréstimo do paulo → html5 – guia prático
(5, 4),  -- primeiro empréstimo do pedro → programação orientada a aspectos em java
(6, 6),  -- segundo empréstimo do pedro → xhtml: guia de referência
(6, 1),  -- segundo empréstimo do pedro → banco de dados – 1 edição
(7, 8);  -- terceiro empréstimo do pedro → php com programação orientada a objetos

-- índice na data do empréstimo
create index idx_emprestimo_data_emprestimo
on emprestimo (data_emprestimo);

-- índice na data de devolução
create index idx_emprestimo_data_devolucao
on emprestimo (data_devolucao);



-- CONSULTA SIMPLES
--Nome dos autores em ordem alfabética:

SELECT nome
FROM autor
ORDER BY nome;


--Nome dos alunos que começam com a letra P:

SELECT nome
FROM aluno
WHERE nome LIKE 'p%';


--Nome dos livros da categoria Banco de Dados ou Java:

SELECT l.nome
FROM livro l
JOIN categoria c ON l.idcategoria = c.idcategoria
WHERE c.nome IN ('banco de dados', 'java');


--Nome dos livros da editora Bookman:

SELECT l.nome
FROM livro l
JOIN editora e ON l.ideditora = e.ideditora
WHERE e.nome = 'bookman';


--Empréstimos realizados entre 05/05/2012 e 10/05/2012:

SELECT *
FROM emprestimo
WHERE data_emprestimo BETWEEN '2012-05-05' AND '2012-05-10';


--Empréstimos que não foram feitos entre 05/05/2012 e 10/05/2012:

SELECT *
FROM emprestimo
WHERE data_emprestimo NOT BETWEEN '2012-05-05' AND '2012-05-10';


--Empréstimos que os livros já foram devolvidos:

SELECT *
FROM emprestimo
WHERE devolvido = 'S';


--CONSULTAS COM AGRUPAMENTO SIMPLES



--Quantidade de livros:

SELECT COUNT(*) AS quantidade_livros
FROM livro;


--Somatório do valor dos empréstimos:

SELECT SUM(valor) AS total_valor
FROM emprestimo;


--Média do valor dos empréstimos:

SELECT AVG(valor) AS media_valor
FROM emprestimo;


--Maior valor dos empréstimos:

SELECT MAX(valor) AS maior_valor
FROM emprestimo;


--Menor valor dos empréstimos:

SELECT MIN(valor) AS menor_valor
FROM emprestimo;


--Somatório do valor do empréstimo entre 05/05/2012 e 10/05/2012:

SELECT SUM(valor) AS total_valor_periodo
FROM emprestimo
WHERE data_emprestimo BETWEEN '2012-05-05' AND '2012-05-10';


--Quantidade de empréstimos entre 01/05/2012 e 05/05/2012:

SELECT COUNT(*) AS quantidade_emprestimos
FROM emprestimo
WHERE data_emprestimo BETWEEN '2012-05-01' AND '2012-05-05';

-- CONSULTA COM JOIN
--Nome do livro, a categoria e a editora (LIVRO) – criar uma view:

CREATE VIEW vw_livro AS
SELECT l.nome AS nome_livro,
       c.nome AS categoria,
       e.nome AS editora
FROM livro l
JOIN categoria c ON l.idcategoria = c.idcategoria
JOIN editora e ON l.ideditora = e.ideditora;


--Nome do livro e o nome do autor (LIVRO_AUTOR) – criar uma view:

CREATE VIEW vw_livro_autor AS
SELECT l.nome AS livro,
       a.nome AS autor
FROM livro l
JOIN livro_autor la ON l.idlivro = la.idlivro
JOIN autor a ON la.idautor = a.idautor;


--Nome dos livros do autor Ian Graham (LIVRO_AUTOR):

SELECT l.nome
FROM livro l
JOIN livro_autor la ON l.idlivro = la.idlivro
JOIN autor a ON la.idautor = a.idautor
WHERE a.nome = 'ian graham';


--Nome do aluno, a data do empréstimo e a data de devolução (EMPRESTIMO):

SELECT al.nome AS aluno,
       e.data_emprestimo,
       e.data_devolucao
FROM emprestimo e
JOIN aluno al ON e.idaluno = al.idaluno;


--CONSULTAS COM AGRUPAMENTO + JOIN


--Nome de todos os livros que foram emprestados (EMPRESTIMO_LIVRO):

SELECT DISTINCT l.nome
FROM livro l
JOIN emprestimo_livro el ON l.idlivro = el.IdLivro;

--Nome da editora e a quantidade de livros de cada editora (LIVRO):

SELECT e.nome AS editora,
       COUNT(*) AS quantidade_livros
FROM livro l
JOIN editora e ON l.ideditora = e.ideditora
GROUP BY e.nome;


--Nome da categoria e a quantidade de livros de cada categoria (LIVRO):

SELECT c.nome AS categoria,
       COUNT(*) AS quantidade_livros
FROM livro l
JOIN categoria c ON l.idcategoria = c.idcategoria
GROUP BY c.nome;


--Nome do autor e a quantidade de livros de cada autor (LIVRO_AUTOR):

SELECT a.nome AS autor,
       COUNT(*) AS quantidade_livros
FROM livro_autor la
JOIN autor a ON la.idautor = a.idautor
GROUP BY a.nome;


--Nome do aluno e a quantidade de empréstimos de cada aluno (EMPRESTIMO_LIVRO):

SELECT al.nome AS aluno,
       COUNT(el.IdLivro) AS quantidade_emprestimos
FROM emprestimo e
JOIN aluno al ON e.idaluno = al.idaluno
JOIN emprestimo_livro el ON e.idemprestimo = el.IdEmprestimo
GROUP BY al.nome;


--Nome do aluno e o somatório do valor total dos empréstimos de cada aluno (EMPRESTIMO):

SELECT al.nome AS aluno,
       SUM(e.valor) AS total_valor
FROM emprestimo e
JOIN aluno al ON e.idaluno = al.idaluno
GROUP BY al.nome;


--Nome do aluno e o somatório do valor total dos empréstimos > 7,00 (EMPRESTIMO):

SELECT al.nome AS aluno,
       SUM(e.valor) AS total_valor
FROM emprestimo e
JOIN aluno al ON e.idaluno = al.idaluno
GROUP BY al.nome
HAVING SUM(e.valor) > 7.00;


--CONSULTAS COMANDOS DIVERSOS

--Nome de todos os alunos em ordem decrescente e em letra maiúscula:

SELECT UPPER(nome) AS nome_maiusculo
FROM aluno
ORDER BY nome DESC;


--Empréstimos que foram feitos no mês 04 de 2012:

SELECT *
FROM emprestimo
WHERE EXTRACT(MONTH FROM data_emprestimo) = 4
  AND EXTRACT(YEAR FROM data_emprestimo) = 2012;


--Todos os campos do empréstimo. Caso já tenha sido devolvido, mostrar “Devolução completa”, senão “Em atraso”:

SELECT *,
       CASE
           WHEN devolvido = 'S' THEN 'Devolução completa'
           ELSE 'Em atraso'
       END AS status
FROM emprestimo;


--Somente o caractere 5 até o caractere 10 do nome dos autores:

SELECT SUBSTRING(nome FROM 5 FOR 6) AS parte_nome
FROM autor;


--Valor do empréstimo e somente o mês da data de empréstimo (escrevendo o nome do mês):

SELECT valor,
       CASE EXTRACT(MONTH FROM data_emprestimo)
           WHEN 1 THEN 'Janeiro'
           WHEN 2 THEN 'Fevereiro'
           WHEN 3 THEN 'Março'
           WHEN 4 THEN 'Abril'
           WHEN 5 THEN 'Maio'
           WHEN 6 THEN 'Junho'
           WHEN 7 THEN 'Julho'
           WHEN 8 THEN 'Agosto'
           WHEN 9 THEN 'Setembro'
           WHEN 10 THEN 'Outubro'
           WHEN 11 THEN 'Novembro'
           WHEN 12 THEN 'Dezembro'
       END AS mes
FROM emprestimo;

--SUBCONSULTAS

--Data do empréstimo e valor dos empréstimos que o valor seja maior que a média de todos os empréstimos:

SELECT data_emprestimo, valor
FROM emprestimo
WHERE valor > (SELECT AVG(valor) FROM emprestimo);


--Data do empréstimo e valor dos empréstimos que possuem mais de um livro:

SELECT e.data_emprestimo, e.valor
FROM emprestimo e
WHERE e.idemprestimo IN (
    SELECT IdEmprestimo
    FROM emprestimo_livro
    GROUP BY IdEmprestimo
    HAVING COUNT(IdLivro) > 1
);


--Data do empréstimo e valor dos empréstimos que o valor seja menor que a soma de todos os empréstimos:

SELECT data_emprestimo, valor
FROM emprestimox
WHERE valor < (SELECT SUM(valor) FROM emprestimo);
a

