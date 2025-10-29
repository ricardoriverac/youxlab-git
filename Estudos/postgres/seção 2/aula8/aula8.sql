
CREATE TABLE clientes (
    idcliente INTEGER NOT NULL,
    nome VARCHAR(2253),
    cpf CHAR(11),
    rg VARCHAR(20),
    data_nascimento DATE,
    genero CHAR(1),
    profissao VARCHAR(29),
    nacionalidade VARCHAR(32),
    logradouro VARCHAR(179),
    numero VARCHAR(15),
    complemento VARCHAR(200),
    bairro VARCHAR(150),
    municipio VARCHAR(300),
    uf VARCHAR(5),
    observacoes TEXT,

	--Primary key
    CONSTRAINT pk_cln_idcliente PRIMARY KEY (idcliente)
);

INSERT INTO clientes (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
VALUES (1, 'Manoel', '88828383821', '32323', '10/10/2001', 'M', 'Estudante', 'Brasileira', 'Rua Joaquim Nabuco', '23', 'Casa', 'Cidade Nova', 'Porto União', 'SC');

INSERT INTO clientes (idcliente, nome, cpf, rg, data_nascimento, genero, profissao, nacionalidade, logradouro, numero, complemento, bairro, municipio, uf)
VALUES (2, 'Geraldo', '12343299291', '56565', '04/01/1987', 'M', 'Engenheiro', 'Brasileira', 'Rua das Limas', '200', 'AP.', 'Cientro', 'P. União', 'SC')
