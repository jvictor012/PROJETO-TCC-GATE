from flask import Flask, render_template, url_for, request, redirect, flash, session
from db import db
from models import Usuario


gate = Flask(__name__)
gate.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gate.db'# cria o banco de dados
db.init_app(gate)# conecta o banco de dados no gate

@gate.route('/')
def home():
    return render_template('home.html')

@gate.route('/escolha')
def escolha():
    return render_template('escolha.html')

@gate.route('/login')
def login():
    return render_template('login.html')

@gate.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'GET':# verifica se o método é GET
        return render_template('registrar.html')
    elif request.method == 'POST':
        nome = request.form['nomeForm']
        email = request.form['emailForm']
        senha = request.form['senhaForm']

        novo_user = Usuario(nome=nome, email=email, senha=senha)
        db.session.add(novo_user)# adiciona o novo usuário no banco de dados
        db.session.commit()# salva as alterações no banco de dados

        return redirect(url_for('escolha'))# redireciona para a página de criar evento

if __name__ == "__main__":
    with gate.app_context():
        db.create_all()# cria todas as tabelas no banco de dados
    gate.run(debug=True)