-- Criando Tabela --

create table cliente(
	idcliente integer not null,
	nome varchar(50) not null,
	cpf char(11) not null,
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

	-- primary key
	constraint pk_cln_idcliente primary key (idcliente)
	
)

-- Inserção de Valores --

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (1, 'Manoel', '88828383821', '32323', '2001-10-10', 'M', 'Estudante', 'Brasileira', 'Rua Joaquim Nabuco', '23', 'Casa', 'Cidade Nova', 'Porto União', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (2, 'Geraldo', '12343299291', '56565', '1987-01-04', 'M', 'Engenheiro', 'Brasileira', 'Rua Das Limas', '200', 'Ap.', 'Centro', 'P.União', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (3, 'Carlos', '87732323227', '55463', '1967-10-01', 'M', 'Pedreiro', 'Brasileiro', 'Rua das Laranjas', '300', 'Apart.', 'Cto.', 'Canoinhas', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (4, 'Adriana', '12321222122', '98777', '1989-09-10', 'F', 'Jornalista', 'Brasileiro', 'Rua das Limas', '240', 'Casa', 'São Pedro', 'Porto Vitória', 'PR');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (5, 'Amanda', '99982838828', '28382', '1991-03-04', 'F', 'Jorn.', 'Italia', 'Av. Cetral', '100', null, 'São Pedro', 'General Carneiro', 'PR');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (6, 'Ângelo', '99982828181', '12323', '2000-01-01', 'M', 'Professor', 'Brasileiro', 'Av. Beira Mar', '300', null, 'Ctr.', 'São Paulo', 'SP');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (7, 'Anderson', null, null, null, 'M', 'Prof.', 'Italiano', 'AV. Brasil', '100', 'Apartamento', 'Santa Rosa', 'Rio de Janeiro', 'SP');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (8, 'Camila', '9998282828', null, '2001-10-10', 'F', 'Professora', 'Norte americana', 'Rua Central', '4333', null, 'Centro', 'Uberlância', 'MG');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (9, 'Cristiano', '9998282828', null, '2001-10-10', 'F', 'Professora', 'Norte americana', 'Rua Central', '4333', null, 'Centro', 'Uberlância', 'MG');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (10, 'Fabrício', '8828282828', '32323', null, 'M', 'Estudante', 'Brasileiro', null, null, null, null, 'PU', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (11, 'Fernanda', null, null, null, 'F', null, 'Brasileira', null, null, null, null, 'Posto União', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (12, 'Gilmar', '88881818181', '888', '2000-02-10', 'M', 'Estud.', null, 'Rua das Laranjas', '200', null, 'C. Nova', 'Canoinhas', 'SC');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (13, 'Diego', '1010191919', '111939', null, 'M', 'Professor', 'Alemão', 'Rua Central', '455', 'Casa', 'Cidade N.', 'São Paulo', 'SP');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (14, 'Jeferson', null, null, '1983-07-01', 'M', null, 'Brasileiro', null, null, null, null, 'União Vitória', 'PR');

insert into cliente (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
values (15, 'Jessica', null, null, null, 'F', 'Estudante', null, null, null, null, null, 'União Vitória', 'PR');

-- Mostrar Tabela --
select * from cliente

-- Mudar o nome da tabela
select cpf as "CPF dos clientes" from cliente

-- Tabela Concatenada
select 'CPF: ' || cpf || ' RG: ' || rg as "CPF e RG  do cliente" from cliente

-- Limite de dados
select nome, cpf, data_nascimento from cliente limit 5;

-- Filtrar informações
select nome, numero from cliente where numero < '200';

--  like
select nome from cliente where nome like 'A';
-
-- %like
select nome from cliente where nome like '%b';

-- %like%
select nome from cliente where nome like '%a%'

-- like%
select nome from cliente where nome like 'a%'

-- between
select nome from cliente where data_nascimento between '2000-01-01' and  '1980-01-01;'

-- is null
select nome, rg from cliente where rg is null

-- order by 
select nome from cliente order by nome asc;

-- order by txt  desc 
select nome from cliente order by nome desc 

-- Exercícios -- 

-- Exercício 1° - O nome, o gênero e a profissão de todos os clientes, ordenado pelo nome em ordem decrescente 

select nome, genero, profissao from cliente order by nome desc;


-- Exercício 2° - Os clientes que tenham a letra “R” no nome 
select nome from cliente where nome like '%r%';


-- Exercícios 3° - Os clientes que o nome inicia com a letra “C”
select nome from cliente where nome like 'C%'

-- Exercício 4° -  Os clientes que o nome termina com a letra “A”
select nome from cliente where nome like '%a';

-- Exercícios 5° -  Os clientes que moram no bairro “Centro”
select nome, bairro from cliente where bairro like 'Centro' or bairro like 'Ctr.' or bairro like 'Cto.';

-- Exercício 6° -  Os clientes que moram em complementos que iniciam com a letra “A”
select nome, complemento from cliente where complemento is not null and nome like 'A%';

-- Exercício 7° -  Somente os clientes do sexo feminino
select nome from cliente where genero = 'F';

-- Exercícios 8° - Os clientes que não informaram o CPF
select nome, cpf from cliente where cpf is null

-- Exercícios 9° - O nome e a profissão dos clientes, ordenado em ordem crescente pelo nome da profissão
select nome, profissao from cliente order by profissao asc;

-- Exercícios 10° - Os clientes de nacionalidade “Brasileira”
select nome, nacionalidade from cliente where nacionalidade like 'Brasileiro' or nacionalidade like 'Brasileira';

-- Exercício 11° - Os clientes que informaram o número da residência
select nome, numero from cliente where numero is not null;

-- Exercício 12° -  Os clientes que moram em Santa Catarina
select nome, uf from cliente where uf like 'SC';

-- Exercício 13° - Os clientes que nasceram entre 01/01/2000 e 01/01/2002
select nome, data_nascimento from cliente where data_nascimento between '2000-01-01' and '2002-01-01';

-- Exercício 14° -  O nome do cliente e o logradouro, número, complemento, bairro, município e UF concatenado de todos os clientes
select 
'Nome: ' || nome || ' Endereço: ' || logradouro || ' N° da casa: ' || numero || ' Complemento: ' || complemento || ' Bairro: ' || bairro || ' Município: ' || municipio || ' UF: ' || uf from cliente

-- Update e  Delete -- 

-- update 
update cliente set nome = 'Teste' where idcliente = 1;

update cliente set nome = 'Adriano', genero = 'M', numero = '241' where idcliente = 4;

-- delete 
delete from cliente where idclien
