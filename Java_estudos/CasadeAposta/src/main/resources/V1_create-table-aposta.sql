CREATE TABLE apostas (
    id UUID PRIMARY KEY,
    usuario_id UUID NOT NULL,
    valor_apostado NUMERIC(10,2) NOT NULL,
    valor_ganhos NUMERIC(10,2),
    status VARCHAR(20) NOT NULL,
    data_criacao TIMESTAMP,
    diamantes_encontrados INT,

    CONSTRAINT fk_usuario
    FOREIGN KEY(usuario_id)
    REFERENCES users(id)
);