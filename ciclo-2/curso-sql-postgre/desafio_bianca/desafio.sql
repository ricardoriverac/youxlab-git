-- Cria schema lógico para o desafio
CREATE SCHEMA IF NOT EXISTS escola_online;
SET search_path TO escola_online;

-- Tabela de usuários (alunos e instrutores)
CREATE TABLE usuario (
    id_usuario       BIGSERIAL PRIMARY KEY,
    nome_completo    VARCHAR(200) NOT NULL,
    email            VARCHAR(255) NOT NULL UNIQUE,
    senha_hash       VARCHAR(255) NOT NULL,
    tipo_usuario     VARCHAR(20) NOT NULL CHECK (tipo_usuario IN ('ALUNO', 'INSTRUTOR', 'ADMIN')),
    data_cadastro    TIMESTAMP NOT NULL DEFAULT NOW(),
    ativo            BOOLEAN NOT NULL DEFAULT TRUE
);

-- Tabela de cursos
CREATE TABLE curso (
    id_curso         BIGSERIAL PRIMARY KEY,
    titulo           VARCHAR(200) NOT NULL,
    descricao        TEXT,
    nivel            VARCHAR(20) NOT NULL CHECK (nivel IN ('INICIANTE', 'INTERMEDIARIO', 'AVANCADO')),
    id_instrutor     BIGINT NOT NULL,
    data_criacao     TIMESTAMP NOT NULL DEFAULT NOW(),
    publicado        BOOLEAN NOT NULL DEFAULT FALSE,
    CONSTRAINT fk_curso_instrutor
        FOREIGN KEY (id_instrutor)
        REFERENCES usuario (id_usuario)a
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- Tabela de módulos de curso
CREATE TABLE modulo (
    id_modulo        BIGSERIAL PRIMARY KEY,
    id_curso         BIGINT NOT NULL,
    titulo           VARCHAR(200) NOT NULL,
    ordem            INTEGER NOT NULL,
    descricao        TEXT,
    CONSTRAINT fk_modulo_curso
        FOREIGN KEY (id_curso)
        REFERENCES curso (id_curso)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT uk_modulo_ordem_curso
        UNIQUE (id_curso, ordem)
);

-- Tabela de aulas dentro de cada módulo
CREATE TABLE aula (
    id_aula          BIGSERIAL PRIMARY KEY,
    id_modulo        BIGINT NOT NULL,
    titulo           VARCHAR(200) NOT NULL,
    conteudo_url     VARCHAR(500),
    duracao_minutos  INTEGER CHECK (duracao_minutos IS NULL OR duracao_minutos > 0),
    ordem            INTEGER NOT NULL,
    CONSTRAINT fk_aula_modulo
        FOREIGN KEY (id_modulo)
        REFERENCES modulo (id_modulo)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT uk_aula_ordem_modulo
        UNIQUE (id_modulo, ordem)
);

-- Tabela de matrículas dos alunos nos cursos
CREATE TABLE matricula (
    id_matricula     BIGSERIAL PRIMARY KEY,
    id_aluno         BIGINT NOT NULL,
    id_curso         BIGINT NOT NULL,
    data_matricula   TIMESTAMP NOT NULL DEFAULT NOW(),
    status           VARCHAR(20) NOT NULL CHECK (status IN ('ATIVA', 'CONCLUIDA', 'CANCELADA')),
    nota_final       NUMERIC(5,2) CHECK (nota_final IS NULL OR (nota_final >= 0 AND nota_final <= 10)),
    CONSTRAINT fk_matricula_aluno
        FOREIGN KEY (id_aluno)
        REFERENCES usuario (id_usuario)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT fk_matricula_curso
        FOREIGN KEY (id_curso)
        REFERENCES curso (id_curso)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT uk_matricula_aluno_curso
        UNIQUE (id_aluno, id_curso)
);

-- Tabela de avaliações (feedback) dos alunos sobre os cursos
CREATE TABLE avaliacao_curso (
    id_avaliacao     BIGSERIAL PRIMARY KEY,
    id_matricula     BIGINT NOT NULL,
    nota             INTEGER NOT NULL CHECK (nota BETWEEN 1 AND 5),
    comentario       TEXT,
    data_avaliacao   TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT fk_avaliacao_matricula
        FOREIGN KEY (id_matricula)
        REFERENCES matricula (id_matricula)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT uk_avaliacao_unica_por_matricula
        UNIQUE (id_matricula)
);

-- Tabela de progresso por aula (aluno X aula)
CREATE TABLE progresso_aula (
    id_progresso     BIGSERIAL PRIMARY KEY,
    id_matricula     BIGINT NOT NULL,
    id_aula          BIGINT NOT NULL,
    concluida        BOOLEAN NOT NULL DEFAULT FALSE,
    data_ultima_acao TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT fk_progresso_matricula
        FOREIGN KEY (id_matricula)
        REFERENCES matricula (id_matricula)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_progresso_aula
        FOREIGN KEY (id_aula)
        REFERENCES aula (id_aula)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT uk_progresso_matricula_aula
        UNIQUE (id_matricula, id_aula)
);

-- Índices para melhorar consultas comuns
CREATE INDEX idx_usuario_tipo ON usuario (tipo_usuario);
CREATE INDEX idx_curso_instrutor ON curso (id_instrutor);
CREATE INDEX idx_matricula_aluno ON matricula (id_aluno);
CREATE INDEX idx_matricula_curso ON matricula (id_curso);
CREATE INDEX idx_avaliacao_matricula ON avaliacao_curso (id_matricula);
CREATE INDEX idx_progresso_matricula ON progresso_aula (id_matricula);
CREATE INDEX idx_progresso_aula ON progresso_aula (id_aula);


-- 1) Usuários (3 alunos, 2 instrutores, 1 admin)
INSERT INTO usuario (id_usuario, nome_completo, email, senha_hash, tipo_usuario, data_cadastro, ativo) VALUES
(1, 'Ana Souza',        'ana.souza@example.com',        'hash1', 'ALUNO',     NOW() - INTERVAL '60 days', TRUE),
(2, 'Bruno Lima',       'bruno.lima@example.com',       'hash2', 'ALUNO',     NOW() - INTERVAL '40 days', TRUE),
(3, 'Carla Pereira',    'carla.pereira@example.com',    'hash3', 'ALUNO',     NOW() - INTERVAL '20 days', TRUE),
(4, 'Daniel Instrutor', 'daniel.instrutor@example.com', 'hash4', 'INSTRUTOR', NOW() - INTERVAL '90 days', TRUE),
(5, 'Erika Instrutora', 'erika.instrutora@example.com', 'hash5', 'INSTRUTOR', NOW() - INTERVAL '80 days', TRUE),
(6, 'Admin Sistema',    'admin@example.com',            'hash6', 'ADMIN',     NOW() - INTERVAL '100 days', TRUE);

-- 2) Cursos
INSERT INTO curso (id_curso, titulo, descricao, nivel, id_instrutor, data_criacao, publicado) VALUES
(1, 'Introdução a SQL', 'Curso básico de SQL para iniciantes',          'INICIANTE',     4, NOW() - INTERVAL '70 days', TRUE),
(2, 'Modelagem de Dados', 'Modelagem relacional e normalização',        'INTERMEDIARIO', 4, NOW() - INTERVAL '50 days', TRUE),
(3, 'PostgreSQL Avançado', 'Tópicos avançados em PostgreSQL',           'AVANCADO',      5, NOW() - INTERVAL '30 days', FALSE);

-- 3) Módulos
INSERT INTO modulo (id_modulo, id_curso, titulo, ordem, descricao) VALUES
-- Curso 1: Introdução a SQL
(1, 1, 'Fundamentos de Bancos de Dados', 1, 'Conceitos básicos'),
(2, 1, 'Comandos SQL Básicos',           2, 'SELECT, INSERT, UPDATE, DELETE'),
-- Curso 2: Modelagem de Dados
(3, 2, 'Conceitos de Modelagem',         1, 'Entidades, relacionamentos'),
(4, 2, 'Normalização',                   2, 'Formas normais'),
-- Curso 3: PostgreSQL Avançado
(5, 3, 'Tuning e Índices',               1, 'Uso de índices e EXPLAIN');

-- 4) Aulas
INSERT INTO aula (id_aula, id_modulo, titulo, conteudo_url, duracao_minutos, ordem) VALUES
-- Módulo 1
(1, 1, 'O que é um SGBD?',          'https://example.com/aula1', 20, 1),
(2, 1, 'Arquitetura básica',        'https://example.com/aula2', 25, 2),
-- Módulo 2
(3, 2, 'Primeiro SELECT',           'https://example.com/aula3', 30, 1),
(4, 2, 'Filtrando dados com WHERE', 'https://example.com/aula4', 35, 2),
-- Módulo 3
(5, 3, 'Entidades e atributos',     'https://example.com/aula5', 25, 1),
-- Módulo 4
(6, 4, '1FN, 2FN e 3FN',            'https://example.com/aula6', 40, 1),
-- Módulo 5
(7, 5, 'Índices B-tree',            'https://example.com/aula7', 30, 1),
(8, 5, 'Analisando planos',         'https://example.com/aula8', 45, 2);

-- 5) Matrículas
INSERT INTO matricula (id_matricula, id_aluno, id_curso, data_matricula, status, nota_final) VALUES
(1, 1, 1, NOW() - INTERVAL '55 days', 'CONCLUIDA', 9.0),
(2, 1, 2, NOW() - INTERVAL '25 days', 'ATIVA',     NULL),
(3, 2, 1, NOW() - INTERVAL '30 days', 'ATIVA',     NULL),
(4, 2, 2, NOW() - INTERVAL '10 days', 'ATIVA',     NULL),
(5, 3, 1, NOW() - INTERVAL '15 days', 'CANCELADA', 6.5),
(6, 3, 3, NOW() - INTERVAL '5 days',  'ATIVA',     NULL);

-- 6) Avaliações de curso (apenas matrículas concluídas)
INSERT INTO avaliacao_curso (id_avaliacao, id_matricula, nota, comentario, data_avaliacao) VALUES
(1, 1, 5, 'Curso excelente, bem didático.',    NOW() - INTERVAL '50 days'),
(2, 5, 3, 'Conteúdo bom, mas cancelei.',       NOW() - INTERVAL '10 days');

-- 7) Progresso por aula
INSERT INTO progresso_aula (id_progresso, id_matricula, id_aula, concluida, data_ultima_acao) VALUES
-- Ana no curso 1 (matrícula 1 - concluída)
(1, 1, 1, TRUE,  NOW() - INTERVAL '54 days'),
(2, 1, 2, TRUE,  NOW() - INTERVAL '53 days'),
(3, 1, 3, TRUE,  NOW() - INTERVAL '52 days'),
(4, 1, 4, TRUE,  NOW() - INTERVAL '51 days'),
-- Ana no curso 2 (matrícula 2 - ativa)
(5, 2, 5, TRUE,  NOW() - INTERVAL '20 days'),
(6, 2, 6, FALSE, NOW() - INTERVAL '5 days'),
-- Bruno no curso 1 (matrícula 3 - ativa)
(7, 3, 1, TRUE,  NOW() - INTERVAL '25 days'),
(8, 3, 2, FALSE, NOW() - INTERVAL '20 days'),
-- Bruno no curso 2 (matrícula 4 - ativa, sem progresso ainda)
-- Carla no curso 1 (matrícula 5 - cancelada, chegou a assistir algo)
(9, 5, 1, TRUE,  NOW() - INTERVAL '14 days'),
(10,5, 2, TRUE,  NOW() - INTERVAL '13 days'),
-- Carla no curso 3 (matrícula 6 - ativa, PostgreSQL Avançado)
(11,6, 7, FALSE, NOW() - INTERVAL '3 days');


-- Lista de Exercícios SQL - Escola Online
-- Nível 2: Intermediário (JOINs Simples)

-- Exercício 2.1
	-- Liste o nome de cada aluno e os cursos em que estão matriculados, incluindo o título do curso e data da matrícula. 
select
	usr.nome_completo as aluno,
	crs.id_curso as curso,
	crs.titulo,
	mtc.data_matricula
from
	escola_online.matricula mtc
left outer join
	escola_online.usuario usr on mtc.id_aluno = usr.id_usuario
left outer join
	escola_online.curso crs on mtc.id_curso = crs.id_curso
where
	tipo_usuario = 'ALUNO'

select * from escola_online.matricula

-- Exercício 2.2
	-- Mostre o título de cada curso e o nome do instrutor, apenas cursos publicados.
select
	crs.titulo as titulo,
	usr.nome_completo as nome
from
	escola_online.curso crs
left outer join
	escola_online.usuario usr on crs.id_instrutor = usr.id_usuario
where
	tipo_usuario = 'INSTRUTOR' and
	publicado = true

--Exercício 2.3
	-- Para cada matrícula CONCLUIDA, mostre nome do aluno, título do curso e nota final.
select
	usr.nome_completo as nome,
	crs.titulo as titulo,
	mtc.nota_final
from
	escola_online.matricula mtc
left outer join
	escola_online.usuario usr on mtc.id_aluno = usr.id_usuario
left outer join
	escola_online.curso crs on mtc.id_curso = crs.id_curso
where
	status = 'CONCLUIDA'

-- Exercício 2.4
	-- Liste cada aula e seu módulo correspondente, mostrando título da aula, 
	-- título do módulo e ordem da aula. Ordene por id_modulo, depois por ordem.
select
	aul.id_aula as aula,
	aul.id_modulo as modulo,
	aul.titulo as titulo,
	mdl.titulo as titulo_modulo,
	aul.ordem
from
	escola_online.aula aul
left outer join
	escola_online.modulo mdl on mdl.id_modulo = aul.id_modulo
order by
	mdl.id_modulo, aul.ordem asc
	
-- Exercício 2.5
	-- Mostre todas as avaliações com a informação do aluno (nome) que fez a avaliação.
select
	avc.id_avaliacao,
	usr.nome_completo as nome
from
	escola_online.avaliacao_curso avc
left outer join
	escola_online.matricula mtc on avc.id_matricula = mtc.id_matricula
left outer join
	escola_online.usuario usr on mtc.id_aluno = usr.id_usuario

-- Exercício 2.6
	-- Liste cada aula e quantas vezes foi registrada em progresso_aula 
	-- (quantos alunos iniciaram), mostrando título da aula, id_modulo e contagem.
select
	aul.titulo as aula,
	count(data_ultima_acao)
from
	escola_online.progresso_aula pga
left outer join
	escola_online.aula aul on pga.id_aula = aul.id_aula
group by
	aul.titulo

-- Exercício 2.7
	-- Encontre o nome do instrutor de cada curso que tem pelo menos uma matrícula cancelada.
select
	crs.titulo,
	usr.nome_completo as nome
from
	escola_online.curso crs
left outer join
	escola_online.usuario usr on crs.id_instrutor = usr.id_usuario
left outer join
	escola_online.matricula mtc on mtc.id_curso = crs.id_curso
where
	tipo_usuario = 'INSTRUTOR' and
	status = 'CANCELADA'

-- Exercício 2.8
	--	Mostre quais alunos completaram todas as aulas do módulo com id_modulo = 1. Use progresso_aula com concluida = TRUE.
select
	mdl.id_modulo as modulo,
	usr.nome_completo as nome,
	pga.concluida
from
	escola_online.progresso_aula pga
left outer join
	escola_online.matricula mtc on pga.id_matricula = mtc.id_matricula
left outer join
	escola_online.usuario usr on mtc.id_aluno = usr.id_usuario
left outer join
	escola_online.aula aul on pga.id_aula = aul.id_aula
left outer join
	escola_online.modulo mdl on aul.id_modulo = mdl.id_modulo
where
	mdl.id_modulo = 1 and
	aul.id_aula = 1 and
	pga.concluida = true and
	usr.tipo_usuario = 'ALUNO'

-- Nível 3: Intermediário-Avançado (GROUP BY com Agregação)

-- Exercício 3.1
	-- Para cada curso, mostre o título do curso e a quantidade de matrículas. Ordene pela quantidade (descrescente).
select
	crs.titulo as nome,
	count(mtc.id_curso)
from
	escola_online.matricula mtc
left outer join
	escola_online.curso crs on mtc.id_curso = crs.id_curso
group by
	crs.titulo,
	mtc.id_curso

-- Exercício 3.2
	-- Calcule a média de nota final (nota_final) por curso, mostrando o título do curso e a média.
	-- Considere apenas matrículas com nota não nula.
select
	crs.titulo as nome,
	round(avg(mtc.nota_final), 1)
from
	escola_online.matricula mtc
inner join
	escola_online.curso crs on mtc.id_curso = crs.id_curso
where
	mtc.nota_final is not null
group by
	crs.titulo

-- Exercício 3.3
	-- Liste cada instrutor e a quantidade de cursos que criou, mostrando nome e contagem. Ordene por contagem (descrescente).
select
	usr.nome_completo as nome,
	count(crs.id_curso) as curso_criado
from
	escola_online.curso crs
left outer join
	escola_online.usuario usr on crs.id_instrutor = usr.id_usuario
group by
	usr.nome_completo
order by
	curso_criado desc

-- Exercício 3.4
	-- Para cada aluno, mostre quantos cursos ele se matriculou e quantos concluiu. 
	-- Mostre nome_completo, qtd_matriculas e qtd_concluidas.
select
	usr.nome_completo as nome,
	count(mtc.id_matricula) as quantidade_matricula,
	count(*) filter(where status = 'CONCLUIDA')
from
	escola_online.matricula mtc
left outer join
	escola_online.usuario usr on mtc.id_aluno = usr.id_usuario
group by
	nome

select * from escola_online.matricula

-- Exercício 3.5
	-- Encontre quais módulos têm aulas, e para cada um mostre: título do módulo, 
	-- título do curso, quantidade total de aulas e duração total em minutos.
select
	mdl.titulo as modulo,
	crs.titulo as curso,
	count(aul.id_aula),
	sum(aul.duracao_minutos)
from
	escola_online.aula aul
left outer join
	escola_online.modulo mdl on aul.id_modulo = mdl.id_modulo
left outer join
	escola_online.curso crs on mdl.id_curso = crs.id_curso
group by
	modulo,
	curso

-- Exercício 3.6
	-- Calcule, para cada status de matrícula (ATIVA, CONCLUIDA, CANCELADA), quantas matrículas existem. Ordene por quantidade.
select
	count(*) filter(where status = 'ATIVA') as ativa,
	count(*) filter(where status = 'CANCELADA') as cancelada,
	count(*) filter(where status = 'CONCLUIDA') as concluida,
	count(status) total_matricula
from
	escola_online.matricula mtc

-- Exercício 3.7
	-- Para cada curso, calcule a média das avaliações recebidas. Mostre título do curso, 
	-- média de avaliações e quantidade de avaliações. Ordene pela média (descrescente).
select
	crs.titulo as curso,
	round(avg(avc.nota), 1) as media,
	count(avc.id_avaliacao) as quantidade_avaliacao
from
	escola_online.matricula mtc
left outer join
	escola_online.curso crs on mtc.id_curso = crs.id_curso
left outer join
	escola_online.avaliacao_curso avc on mtc.id_matricula = avc.id_matricula
where
	avc.nota is not null
group by
	titulo
	
-- Exercício 3.8
	-- Liste os instrutores que tiveram pelo menos 2 cursos criados, mostrando nome e quantidade de cursos.
select
	usr.nome_completo as instrutor,
	count(crs.id_curso)
from
	escola_online.curso crs
left outer join
	escola_online.usuario usr on crs.id_instrutor = usr.id_usuario
group by
	instrutor

-- Exercício 3.9
	-- Para cada aluno, calcule quantas aulas completou e quantas iniciou (registros em progresso_aula).
	-- Mostre nome, total iniciadas e total concluídas.
select 
	usr.nome_completo as aluno,
	count(pga.data_ultima_acao) as aula_iniciada,
	count(*) filter(where concluida = true) as aula_completa
from
	escola_online.progresso_aula pga
left outer join
	escola_online.matricula mtc on pga.id_matricula = mtc.id_matricula
left outer join
	escola_online.usuario usr on mtc.id_aluno = usr.id_usuario
group by
	aluno

-- Nível 4: Avançado (Múltiplos JOINs + GROUP BY + Agregação)

-- Exercício 4.1
	-- Crie um relatório de desempenho por instrutor:
		-- Nome do instrutor
		-- Quantidade de cursos criados
		-- Total de alunos matriculados em seus cursos (contar apenas alunos distintos)
		-- Média de avaliações recebidas
		-- Quantidade de matrículas concluídas
	-- Ordene pelo maior número de alunos.
select



select * from escola_online.aula
select * from escola_online.avaliacao_curso
select * from escola_online.curso
select * from escola_online.matricula
select * from escola_online.modulo
select * from escola_online.progresso_aula
select * from escola_online.usuario

-- Exercício 4.2
	-- Crie um ranking de alunos mostrando
		-- Nome do aluno
		-- Quantidade de cursos matriculados
		-- Quantidade de cursos concluídos
		-- Média de nota final nos cursos concluídos
	-- Ordene pela média de notas (descrescente).
select
	usr.nome_completo as nome,
	count(mtc.id_curso) as quantidade_curso,
	count(*) filter(where status = 'CONCLUIDA') as concluido,
	round(avg(mtc.nota_final) filter(where status = 'CONCLUIDA'), 1) as media_concluido			-- INCOMPLETO
from
	escola_online.matricula mtc
left outer join
	escola_online.usuario usr on mtc.id_aluno = usr.id_usuario
group by
	nome
order by
	media_concluido desc

-- Exercício 4.3
	-- Para cada módulo, calcule:
		-- Título do módulo
		-- Título do curso
		-- Quantidade de aulas no módulo
		-- Duração total das aulas
		-- Quantidade de alunos que iniciaram pelo menos uma aula do módulo
		-- Quantidade de alunos que concluíram todas as aulas do módulo
	-- Ordene por quantidade de alunos que concluíram (descrescente).
select
	mdl.titulo as titulo_modulo,
	crs.titulo as titulo_curso,
	count(distinct aul.id_aula) quantidade_aula,
	sum(aul.duracao_minutos) as tempo_aula,
	count(distinct mtc.id_aluno) as iniciaram_aula,
	count(aul.id_aula) filter(where concluida = true) as aulas_concluidas
from 
	escola_online.modulo mdl
left outer join
	escola_online.curso crs on mdl.id_curso = crs.id_curso
left outer join
	escola_online.aula aul on mdl.id_modulo = aul.id_modulo
left outer join
	escola_online.progresso_aula pga on aul.id_aula = pga.id_aula
left outer join
	escola_online.matricula mtc on pga.id_matricula = mtc.id_matricula
group by
	titulo_modulo,
	titulo_curso
order by
	count(mtc.id_aluno) filter(where mtc.status = 'CONCLUIDA')

-- Exercício 4.4
		-- Crie um relatório de matrículas ativas mostrando:
			-- Nome do aluno
			-- Título do curso
			-- Data da matrícula
			-- Quantidade de aulas do curso
			-- Quantidade de aulas já concluídas
			-- Percentual de conclusão (concluídas / total * 100)
		-- Ordene pelo percentual (ascendente - primeiramente os que precisam estudar mais).
select
	usr.nome_completo as nome,
	crs.titulo as titulo_curso,
	mtc.data_matricula,
	count(distinct aul.id_aula) as quantidade_aula,
	count(mtc.id_aluno) filter(where mtc.status = 'CONCLUIDA') as aula_concluida,
	((count(pga.concluida) / count(aul.id_aula)) * 100.0) as percentual_conclusao
from 
	escola_online.matricula mtc
left outer join
	escola_online.usuario usr on mtc.id_aluno = usr.id_usuario
left outer join
	escola_online.curso crs on mtc.id_curso = crs.id_curso
left outer join
	escola_online.modulo mdl on crs.id_curso = mdl.id_curso
left outer join
	escola_online.aula aul on mdl.id_modulo = aul.id_modulo
left outer join
	escola_online.progresso_aula pga on mtc.id_matricula = pga.id_matricula
group by
	usr.nome_completo,
	crs.titulo,
	mtc.data_matricula
	
-- Exercício 4.5
		-- Liste cursos com baixo engajamento:
			-- Título do curso
			-- Nome do instrutor
			-- Total de matrículas
			-- Quantidade de matrículas com status CANCELADA
			-- Média de avaliações (entre 1 e 5)
			-- Percentual de cancelamento
		-- Mostre apenas cursos com mais de 1 matrícula. Ordene pelo percentual de cancelamento (descrescente).

select
	crs.titulo as curso,
	usr.nome_completo as nome,
	count(mtc.id_matricula) as total_matricula,
	count(*) filter(where status = 'CANCELADA') as quantidade_cancelada
from
	escola_online.matricula mtc
left outer join
	escola_online.curso crs on mtc.id_curso = crs.id_curso
left outer join
	escola_online.usuario usr on crs.id_instrutor = usr.id_usuario
group by
	curso,
	nome

-- Exercício 4.6
	-- Crie um relatório de progresso geral por curso:
		-- Título do curso
		-- Total de aulas
		-- Total de registros de progresso (alunos × aulas)
		-- Quantidade de registros concluídos
		-- Percentual geral de conclusão
select
	crs.titulo as titulo_curso,
	count(aul.id_aula) as total_aula,
	sum
from
	escola_online.curso crs
left outer join
	escola_online.modulo mdl on crs.id_curso = mdl.id_curso
left outer join
	escola_online.aula aul on mdl.id_modulo = aul.id_modulo
left outer join
	escola_online.progresso_aula on aul.id_aula 
group by
	titulo_curso

-- Exercício 4.7
	-- Análise de avaliações:
		-- Título do curso
		-- Nome do instrutor
		-- Quantidade de avaliações recebidas
		-- Nota mínima, máxima e média
		-- Quantidade de avaliações com nota ≥ 4
		-- Quantidade de avaliações com nota < 4
	-- Ordene pela média de avaliações (descendente).

-- Exercício 4.8
	-- Relatório de alunos inativos:
		-- Nome do aluno
		-- Quantidade de matrículas ativas
		-- Última data de atividade em progresso_aula
		-- Dias desde a última atividade
	-- Mostre apenas alunos com matrículas ativas há mais de 7 dias sem atividade.

-- Exercício 4.9
	-- Comparação entre cursos do mesmo instrutor:
		-- Nome do instrutor
		-- Título do curso
		-- Quantidade de alunos matriculados
		-- Média de avaliações
		-- Status do curso (PUBLICADO ou RASCUNHO)
	-- Mostre instrutores com mais de um curso e ordene por instrutor, depois por quantidade de alunos.


-- Exercício Chat
-- Liste o nome dos alunos que estão matriculados no curso "Introdução a SQL".
	-- Dica
		-- Descubra o id_curso do curso Introdução a SQL
		-- Depois veja quais alunos têm matrícula nesse curso
(select id_aluno from escola_online.matricula where id_curso in (select id_curso from escola_online.curso where id_curso = 1))

-- Liste os títulos dos cursos que possuem pelo menos uma matrícula ATIVA.
select id_curso from escola_online.matricula where status = 'ATIVA'

-- Liste os alunos que NÃO estão matriculados em nenhum curso.
select id_usuario from escola_online.usuario where tipo_usuario = 'ALUNO' and id_usuario not in (select id_aluno from escola_online.matricula)

-- Liste os cursos que possuem mais matrículas do que o curso "Modelagem de Dados".
select id_curso from escola_online.matricula group by id_curso having count(id_matricula) > (select count(id_matricula) from escola_online.matricula where id_curso = 2)

-- Liste os alunos que possuem mais de uma matrícula.
select count(id_matricula) from escola_online.matricula group by id_aluno having count(id_matricula) > 1

-- Listar os cursos que NÃO possuem nenhuma matrícula.
select id_curso from escola_online.curso where id_curso not in (select id_curso from escola_online.matricula)

-- Listar os alunos e, ao lado, mostrar quantas matrículas cada um possui, usando subconsulta.
select id_usuario, nome_completo, (select count(id_matricula) as quantidade_matricula from escola_online.matricula where id_aluno = id_usuario) from escola_online.usuario where tipo_usuario = 'ALUNO'

-- Listar os cursos e, ao lado, mostrar a média das avaliações de cada curso.
select id_curso, titulo, (select avg(nota) from escola_online.avaliacao_curso where id_matricula in (select id_matricula from escola_online.matricula where matricula.id_curso = curso.id_curso)) from escola_online.curso

-- Listar os alunos que concluíram TODOS os cursos em que se matricularam.
select id_usuario from escola_online.usuario where tipo_usuario = 'ALUNO' and id_usuario not in (select id_aluno from escola_online.matricula where status != 'CONCLUIDA')

-- Listar os alunos que possuem pelo menos UMA matrícula ativa.
select id_usuario from escola_online.usuario where tipo_usuario = 'ALUNO' and exists (select id_aluno from escola_online.matricula where status = 'ATIVA' and matricula.id_aluno = usuario.id_usuario)






select * from escola_online.aula
select * from escola_online.avaliacao_curso
select * from escola_online.curso
select * from escola_online.matricula
select * from escola_online.modulo
select * from escola_online.progresso_aula
select * from escola_online.usuario