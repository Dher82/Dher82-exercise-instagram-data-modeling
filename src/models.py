import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(250), nullable=False)
    nombre_completo = Column(String(250), nullable=False)
    correo_electronico = Column(String(250), unique=True, nullable=False)
    contraseña = Column(String(250), unique=True, nullable=False)
    seguidores = Column(String(250), unique=True, nullable=False)
    seguidos = Column(String(250), unique=True, nullable=False)
    publicaciones = Column(Integer, primary_key=True)
    etiquetas = Column(String(255))

class Etiqueta(Base):
    __tablename__ = 'etiquetas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    usuario_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)

class Publicacion(Base):
    __tablename__ = 'publicaciones'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('etiquetas.id'))
    etiquetas = relationship(Etiqueta)
    usuario_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)

class Seguidores(Base):
    __tablename__ = 'seguidores'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
