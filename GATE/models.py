from .db import db
from flask_login import UserMixin
from datetime import date, time 

class Usuario(UserMixin, db.Model):# herda da tabela de usuarios...
    __tablename__ = 'usuarios' # nome da tabela no banco de dados
    id = db.Column(db.Integer, primary_key=True) # id do usuario
    nome = db.Column(db.String(30), unique = True) # nome do usuario
    email = db.Column(db.String(50), unique = True) # email do usuario
    senha = db.Column(db.String()) # senha do usuario


class Evento(UserMixin, db.Model):
    __tablename__ = 'eventos'
    id = db.Column(db.Integer, primary_key=True)
    nome_evento = db.Column(db.String(100), nullable=False)
    data_evento = db.Column(db.String(8), unique=False)
    local_evento = db.Column(db.String(100), nullable=False)
    horario_inicio_evento = db.Column(db.String(4), nullable=False)
    horario_fim_evento =db.Column(db.String(4), nullable=False)

class Aluno(UserMixin, db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key=True)
    nome_aluno = db.Column(db.String(100), nullable=False)
    matricula_aluno = db.Column(db.String(14), nullable=True)
    email_aluno = db.Column(db.String(40), nullable=False)

#envia isso tudo para o main
#UserMixin é uma classe do Flask-Login que fornece métodos para autenticação de usuários, como is_authenticated, is_active e is_anonymous. Isso permite que o Flask-Login saiba se o usuário está autenticado ou não.
# A classe Usuario herda de db.Model, que é a classe base para todos os modelos do SQLAlchemy. Isso significa que a classe Usuario é um modelo de banco de dados e pode ser usada para criar, ler, atualizar e excluir registros na tabela usuarios.