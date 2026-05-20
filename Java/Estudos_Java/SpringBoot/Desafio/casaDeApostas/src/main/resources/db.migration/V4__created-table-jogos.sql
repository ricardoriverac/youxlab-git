CREATE TABLE jogo (
    id_jogo UUID PRIMARY KEY,
    id_usuario UUID NOT NULL,

    CONSTRAINT fk_usuario_id FOREIGN KEY (id_usuario) REFERENCES users(id),
);