CREATE TABLE usuario (
                         id UUID PRIMARY KEY DEFAULT ,
                         nome VARCHAR(100) NOT NULL,
                         email VARCHAR(150) UNIQUE NOT NULL,
                         senha VARCHAR(255) NOT NULL,
                         role VARCHAR(20) NOT NULL, -- ALUNO / PROFESSOR
                         criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE turma(
                       id UUID PRIMARY KEY DEFAULT,
                       nome VARCHAR(150) NOT NULL,
                       professor_id UUID NOT NULL,

                       CONSTRAINT fk_turma_professor
                           FOREIGN KEY (professor_id)
                               REFERENCES usuario(id)
);


CREATE TABLE aula (
                      id UUID PRIMARY KEY DEFAULT,
                      titulo VARCHAR(150) NOT NULL,
                      conteudo TEXT,
                      curso_id UUID NOT NULL,

                      CONSTRAINT fk_aula_curso
                          FOREIGN KEY (curso_id)
                              REFERENCES curso(id)
);
CREATE TABLE progresso (
                           id UUID PRIMARY KEY DEFAULT,
                           usuario_id UUID NOT NULL,
                           aula_id UUID NOT NULL,
                           concluida BOOLEAN DEFAULT FALSE,
                           data_conclusao TIMESTAMP,

                           CONSTRAINT fk_progresso_usuario
                               FOREIGN KEY (usuario_id)
                                   REFERENCES usuario(id),

                           CONSTRAINT fk_progresso_aula
                               FOREIGN KEY (aula_id)
                                   REFERENCES aula(id),

                           CONSTRAINT unique_progresso UNIQUE (usuario_id, aula_id)
);


CREATE TABLE pontuacao (
                           id UUID PRIMARY KEY DEFAULT,
                           usuario_id UUID NOT NULL UNIQUE,
                           pontos INTEGER DEFAULT 0,

                           CONSTRAINT fk_pontuacao_usuario
                               FOREIGN KEY (usuario_id)
                                   REFERENCES usuario(id)
);
CREATE TABLE missao (
                        id UUID PRIMARY KEY DEFAULT,
                        titulo VARCHAR(150) NOT NULL,
                        descricao TEXT,
                        pontos_recompensa INTEGER NOT NULL
);

CREATE TABLE usuario_missao (
                                id UUID PRIMARY KEY DEFAULT,
                                usuario_id UUID NOT NULL,
                                missao_id UUID NOT NULL,
                                concluida BOOLEAN DEFAULT FALSE,
                                data_conclusao TIMESTAMP,

                                CONSTRAINT fk_usuario_missao_usuario
                                    FOREIGN KEY (usuario_id)
                                        REFERENCES usuario(id),

                                CONSTRAINT fk_usuario_missao_missao
                                    FOREIGN KEY (missao_id)
                                        REFERENCES missao(id),

                                CONSTRAINT unique_usuario_missao UNIQUE (usuario_id, missao_id)
);