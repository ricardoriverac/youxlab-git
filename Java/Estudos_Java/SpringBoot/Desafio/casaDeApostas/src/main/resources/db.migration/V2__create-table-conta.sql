
CREATE TABLE conta (
    id UUID PRIMARY KEY,
    cpf CHAR(11) NOT NULL,
    saldo DOUBLE PRECISION NOT NULL,

    CONSTRAINT fk_user_conta FOREIGN KEY (id_usuario) REFERENCES users(id)
);