from db import db
from flask_login import UserMixin

class Usuario(UserMixin, db.Model):# herda da tabela de usuarios...
    __tablename__ = 'usuarios' # nome da tabela no banco de dados
    id = db.Column(db.Integer, primary_key=True) # id do usuario
    nome = db.Column(db.String(30), unique = True) # nome do usuario
    email = db.Column(db.String(50), unique = True) # email do usuario
    senha = db.Column(db.String()) # senha do usuario

#envia isso tudo para o main
#UserMixin é uma classe do Flask-Login que fornece métodos para autenticação de usuários, como is_authenticated, is_active e is_anonymous. Isso permite que o Flask-Login saiba se o usuário está autenticado ou não.
# A classe Usuario herda de db.Model, que é a classe base para todos os modelos do SQLAlchemy. Isso significa que a classe Usuario é um modelo de banco de dados e pode ser usada para criar, ler, atualizar e excluir registros na tabela usuarios.