# Impotação do peewee e criação do database / tables

from peewee import *

db = SqliteDatabase('freelancers.db')

class Usuario(Model):
    nome = CharField()
    email = CharField(unique=True)
    senha = CharField()

    class Meta:
        database = db

class Anuncio(Model):
    usuario = ForeignKeyField(Usuario, backref='usuarios')
    titulo = CharField()
    descricao = CharField()
    valor = DecimalField()

    class Meta:
        database = db
