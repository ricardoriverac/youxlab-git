CREATE TYPE user_role AS ENUM ('ADMIN', 'USER');

CREATE TABLE users (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    data_nascimento DATE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    role user_role NOT NULL,
    cpf BIGINT UNIQUE NOT NULL
);