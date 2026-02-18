from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()


Base = declarative_base()

# As Tabelas
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo


#Livros
class Livro(Base):
    __tablename__ = "livros"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    qtde_paginas = Column("qtde_paginas", Integer)
    dono = Column("dono", ForeignKey("usuarios.id"))

    def __init__(self, titulo, qtde_paginas, dono):
        self.titulo = titulo
        self.qtd_paginas = qtde_paginas
        self.dono = dono


Base.metadata.create_all(bind=db)

# CRUD

# usuario = Usuario(nome="João", email="joaoothavio@gmail.com", senha="12344321")
# session.add(usuario)
# session.commit()

# R - Read
# lista_usuarios = session.query(Usuario).all()
usuario_joao = session.query(Usuario).filter_by(email="joaoothavio@gmail.com").first()

# livro = Livro(titulo="Nome do Vento", qtde_paginas=1000, dono=usuario_joao.id)
# session.add(livro)
# session.commit()

# U - Update
# usuario_joao.nome = "João Othávio"
# session.add(usuario_joao)
# session.commit()

# D - Delete
# session.delete(usuario_joao)
# session.commit()

# livro_duplicado = session.query(Livro).filter_by(id=2).first()
# session.delete(livro_duplicado)
# session.commit()