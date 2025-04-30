from flask import Flask, render_template, url_for, request, redirect, flash, session
from db import db
from models import Usuario, Evento
from flask_login import LoginManager, login_user, login_required
import hashlib


gate = Flask(__name__)
gate.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gate.db'# cria o banco de dados
gate.secret_key = 'ma.vi.dri.hay.'
db.init_app(gate)# conecta o banco de dados no gate
lm = LoginManager(gate)# inicializa o gerenciador de login

@lm.user_loader
def load_user(id):
    usuario = db.session.query(Usuario).filter_by(id=id).first()# busca o usuário no banco de dados
    return usuario# retorna o usuário encontrado
    


@gate.route('/')
def home():
    return render_template('home.html')

@gate.route('/escolha')
def escolha():
    return render_template('escolha.html')

@gate.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['emailForm']
        senha = request.form['senhaForm']

        user = db.session.query(Usuario).filter_by(email=email, senha=senha ).first()# busca o usuário no banco de dados
        if not user:
            return 'usuario nao encontrado'
        
        login_user(user)# faz o login do usuário
        return redirect(url_for('criar_evento'))# redireciona para a página de criar evento

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

        login_user(novo_user)

        return redirect(url_for('escolha'))# redireciona para a página de criar evento

@gate.route('/gerar_qrcode1', methods=['GET', 'POST'])
@login_required# verifica se o usuário está logado
def gerar_qrcode1():
    return render_template('qrcode_1.html')

@gate.route('/criar_evento', methods=['GET', 'POST'])
@login_required# verifica se o usuário está logado
def criar_evento():
    if request.method == 'GET':
        return render_template('criar_evento.html')
    elif request.method == 'POST':
        nome_evento = request.form['id_evento']
        data_evento = request.form['data_evento']
        local_evento = request.form['local_evento']
        horario_inicio_evento = request.form['inicio_evento']
        horario_fim_evento = request.form['fim_evento']

        novo_evento = Evento(nome_evento=nome_evento, data_evento=data_evento,
                              local_evento=local_evento, horario_inicio_evento=horario_inicio_evento,
                              horario_fim_evento=horario_fim_evento )
        db.session.add(novo_evento)
        db.session.commit()

        return redirect(url_for('gerar_qrcode1'))

if __name__ == "__main__":
    with gate.app_context():
        db.create_all()# cria todas as tabelas no banco de dados
    gate.run(debug=True)