# Importa funções do SQLAlchemy (biblioteca pra mexer com banco de dados)
from sqlalchemy import create_engine, Column, String, Integer,Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

# Cria a "conexão" com o banco de dados
# sqlite:///meubanco.db = cria um arquivo chamado meubanco.db no seu PC
db = create_engine("sqlite:///meubanco.db")

# Cria uma "fábrica" de sessões (tipo um molde pra conversar com o banco)
Session = sessionmaker(bind=db)

# Aqui você cria uma sessão de fato (é com isso que você vai salvar, ler, apagar dados)
session = Session()


# Cria uma base que vai servir de modelo pras tabelas
# Toda classe que virar tabela vai herdar disso
Base = declarative_base()
#cria a tabela
class Usuario(Base):
    __tablename__ = "usuario"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    Nome = Column("nome", String)
    its_adm = Column("its_adm", Boolean)

    def __init__(self, nome, its_adm=False):
        self.Nome = nome
        self.its_adm = its_adm

Base.metadata.create_all(bind=db)

usuario = Usuario(nome="roger")
pedro = Usuario(nome="pedro")
cavalo = Usuario(nome="cavalo")
boi = Usuario(nome="boi")

session.add(usuario)
session.add(pedro)
session.add(cavalo)
session.add(boi)
session.commit()

#fazendo uma consulta no db, na coluna usuarios, e trazendo todos
lista_usuarios = session.query(Usuario).all()
print(lista_usuarios)
# Cria todas as tabelas no banco de dados
# MAS só funciona se você já tiver classes definidas herdando de Base
