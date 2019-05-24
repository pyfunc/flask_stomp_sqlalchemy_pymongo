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

class Produto(Base):
    __tablename__ = 'produtos'
 
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False, unique=True)
    quantidade = Column(Integer, nullable=False, unique=False) 
    status = Column(Integer, ForeignKey('status_pedido.id'))
 
    #nao vejo um status via tabela a principio como a melhor abordagem
    #depende de como serao integrados os sistemas, mas ainda sim, por mim provavelmente sera uma abordagem problematica,
    #utilizei pela simplicidade e para exemplo apenas
    status_pedido = relation("StatusPedido", backref='produtos', lazy=False)

    def __init__(self, nome=None,quantidade=None):
        self.nome = nome
        self.quantidade = quantidade
 
    def __repr__(self):
        return "Produto(%r, %r, %r)" % (self.nome, self.quantidade, self.status)

class StatusPedido(Base):
    __tablename__ = 'status_pedido'

    id = Column(Integer, primary_key=True)
    nome = Column(String(30), nullable=False, unique=True)

    def __init__(self, nome=None):
        self.nome = nome

    def __repr__(self):
        return "StatusPedido(%r)" % (self.nome)

engine = create_engine('mysql+pymysql://maria:123@localhost/brlabs?host=localhost?port=3306')
Base.metadata.create_all(engine)

'''db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
'''
class ProdutoDao():
    def gravar(self, nome, quantidade, status):
        Session = sessionmaker(bind=engine)
        session = Session()

        produto = Produto(nome, quantidade)
        produto.status_pedido = StatusPedido(status)

        try:
            session.add(produto)
            session.commit()
        except:
            session.rollback()

class FilmeDao():
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