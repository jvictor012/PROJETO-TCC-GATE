from db import db

class Usuario(db.Model):# herda da tabela de usuarios...
    __tablename__ = 'usuarios' # nome da tabela no banco de dados
    id = db.Column(db.Integer, primary_key=True) # id do usuario
    nome = db.Column(db.String(30), unique = True) # nome do usuario
    email = db.Column(db.String(50), unique = True) # email do usuario
    senha = db.Column(db.String()) # senha do usuario

#envia isso tudo para o main