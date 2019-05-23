from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

Base = declarative_base()
 
class Filme(Base):
    __tablename__ = 'filmes'
 
    id = Column(Integer, primary_key=True)
    titulo = Column(String(255), nullable=False)
    ano = Column(Integer)
    dirigido_por = Column(Integer, ForeignKey('diretores.id'))
 
    diretor = relation("Diretor", backref='filmes', lazy=False)
 
    def __init__(self, titulo=None, ano=None):
        self.titulo = titulo
        self.ano = ano
    def __repr__(self):
        return "Filme(%r, %r, %r)" % (self.titulo, self.ano, self.diretor)
 
class Diretor(Base):
    __tablename__ = 'diretores'
 
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False, unique=True)
 
    def __init__(self, nome=None):
        self.nome = nome
 
    def __repr__(self):
        return "Diretor(%r)" % (self.nome)
 
engine = create_engine('mysql+pymysql://maria:123@localhost/brlabs?host=localhost?port=3306')
Base.metadata.create_all(engine)

'''db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
'''
class Dao():
    def gravar(self):
        Session = sessionmaker(bind=engine)
        session = Session()

        f1 = Filme("Star Trek", 2009)
        f1.diretor = Diretor("JJ Abrams")

        d2 = Diretor("George Lucas")
        d2.filmes = [Filme("Guerra nas Estrelas", 1977), Filme("THX 1138", 1971)]

        try:
            session.add(f1)
            session.add(d2)
            session.commit()
        except:
            session.rollback()