from sqlalchemy import create_engine, Column, Integer, String, Date, Float, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship, sessionmaker
from database import Base

class Tutor(Base):
    __tablename__ = 'tutores'
    
    email = Column(String(64), primary_key=True)
    nome = Column(String(64), nullable=False)
    senha = Column(String(64), nullable=False)
    telefone = Column(String(16), nullable=False)
    
    # Relacionamento com pets (um tutor pode ter muitos pets)
    pets = relationship("Pet", back_populates="tutor", cascade="all, delete-orphan")


class Pet(Base):
    __tablename__ = 'pets'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(32), nullable=False)
    especie = Column(String(16), nullable=False)
    raca = Column(String(32), server_default='Desconhecido')
    nascimento = Column(Date)
    peso = Column(Float)
    imagem = Column(String(128))
    tutor_email = Column(String(64), ForeignKey('tutores.email'), primary_key=True)
    
    # Relacionamentos
    tutor = relationship("Tutor", back_populates="pets")
    consultas = relationship("Consulta", back_populates="pet", cascade="all, delete-orphan")
    diagnosticos = relationship("Diagnostico", back_populates="pet", cascade="all, delete-orphan")


class Consulta(Base):
    __tablename__ = 'consultas'
    
    id = Column(Integer, primary_key=True)
    data = Column(Date, nullable=False)
    resultado = Column(String(512), nullable=False)
    pets_id = Column(Integer, nullable=False)
    pets_tutor_email = Column(String(64), nullable=False)
    
    # Chave estrangeira composta
    __table_args__ = (
        ForeignKeyConstraint(
            ['pets_id', 'pets_tutor_email'],
            ['pets.id', 'pets.tutor_email']
        ),
    )
    
    # Relacionamentos
    pet = relationship("Pet", back_populates="consultas")
    profissionais = relationship("Profissional", back_populates="consulta", cascade="all, delete-orphan")


class Profissional(Base):
    __tablename__ = 'profissionais'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(32), nullable=False)
    email = Column(String(64), unique=True)
    telefone = Column(String(16), nullable=False)
    clinica = Column(String(64))
    especialidade = Column(String(64))
    consultas_id = Column(Integer, ForeignKey('consultas.id'), nullable=False)
    
    # Relacionamento
    consulta = relationship("Consulta", back_populates="profissionais")


class Diagnostico(Base):
    __tablename__ = 'diagnosticos'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(32), nullable=False)
    detalhamento = Column(String(256), nullable=False)
    data = Column(Date, nullable=False)
    pets_id = Column(Integer, nullable=False)
    pets_tutor_email = Column(String(64), nullable=False)
    
    # Chave estrangeira composta
    __table_args__ = (
        ForeignKeyConstraint(
            ['pets_id', 'pets_tutor_email'],
            ['pets.id', 'pets.tutor_email']
        ),
    )
    
    # Relacionamentos
    pet = relationship("Pet", back_populates="diagnosticos")