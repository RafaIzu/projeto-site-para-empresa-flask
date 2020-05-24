from flask import Flask, render_template, request, jsonify 
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mensagem.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(25), nullable=True)
    sobrenome = db.Column(db.String(25), nullable=True)
    email = db.Column(db.String(25), nullable=True)
    assunto =  db.Column(db.String(50), nullable=True )
    mensagem = db.Column(db.String(100), nullable=True)
    hora = db.Column(db.DateTime, default=datetime.now)


@app.route('/comunicado', methods = ['POST'])
def visitante():
    if request.method == 'POST':
        print(request.form['nome'])
        print(request.form['sobrenome'])
        print(request.form['email'])
        print(request.form['assunto'])
        print(request.form['mensagem'])
        visita = Mensagem(nome = request.form['nome'], sobrenome=request.form['sobrenome'],email=request.form['email'],assunto = request.form['assunto'],mensagem=request.form['mensagem'])
        db.session.add(visita)
        db.session.commit()
        return render_template('/obrigado.html')


@app.route('/cursos')
@app.route('/')
def cursos():
    return render_template('/cursos.html')


@app.route('/contato')
def contato():
    return render_template('/contato.html')


@app.route('/obrigado')
def obrigado():
    return render_template('/obrigado.html')


@app.route('/login')
def login():
    return render_template('/login.html')

@app.route('/sobre')
def sobre():
    return render_template('/sobre.html')


if __name__ == '__main__':
    app.run(debug= True, host='0.0.0.0')