from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'chave_secreta_segura'

def init_db():
    with sqlite3.connect('db.sqlite3') as conn:
        cursor = conn.cursor()
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nome TEXT UNIQUE,
                          email TEXT UNIQUE,
                          senha TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS animais (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nome TEXT,
                          idade TEXT,
                          especie TEXT,
                          descricao TEXT,
                          imagem TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS adotantes (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nome TEXT,
                          email TEXT UNIQUE,
                          telefone TEXT,
                          endereco TEXT)''')

        # 📌 Criar usuário padrão SEBEM se não existir
        cursor.execute("SELECT * FROM usuarios WHERE nome = 'SEBEM'")
        if not cursor.fetchone():
            cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", 
                           ('SEBEM', None, 'SEBEMprefeitaoegabi'))  # Correção do NULL para None
        
        conn.commit()

# 📌 Página inicial exibe os animais disponíveis para adoção
@app.route('/')
def index():
    with sqlite3.connect('db.sqlite3') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM animais")
        animais = cursor.fetchall()
    return render_template('adocao.html', animais=animais)

# 📌 Página de Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']

        with sqlite3.connect('db.sqlite3') as conn:
            cursor = conn.cursor()
            
            # 📌 Permitir login de SEBEM com nome e senha, sem precisar de email
            if usuario == "SEBEM":
                cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND senha = ?", (usuario, senha))
            else:
                cursor.execute("SELECT * FROM usuarios WHERE (email = ? OR nome = ?) AND senha = ?", (usuario, usuario, senha))
            
            user = cursor.fetchone()

            if user:
                session['usuario_logado'] = user[0]  # Guarda o ID do usuário
                
                # 📌 Redirecionar usuário logado para a página de adoção
                return redirect(url_for('adocao'))
            else:
                return render_template('login.html', erro="Usuário ou senha inválidos!")

    return render_template('login.html')

# 📌 Logout
@app.route('/logout')
def logout():
    session.pop('usuario_logado', None)
    return redirect(url_for('index'))  # Redireciona para a listagem de adoção

# 📌 Página de Adoção (acessível a todos)
@app.route('/adocao')
def adocao():
    with sqlite3.connect('db.sqlite3') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM animais")
        animais = cursor.fetchall()
    return render_template('adocao.html', animais=animais)

# 📌 Página de Cadastro de Adotante (acessível a todos)
@app.route('/cadastro_adotante', methods=['GET', 'POST'])
def cadastro_adotante():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        endereco = request.form['endereco']

        with sqlite3.connect('db.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO adotantes (nome, email, telefone, endereco) VALUES (?, ?, ?, ?)",
                           (nome, email, telefone, endereco))
            conn.commit()
        return redirect(url_for('index'))  # Redireciona para a página inicial (adoção)

    return render_template('cadastro_adotante.html')

# 📌 Página de Cadastro de Animais (SOMENTE para usuários logados)
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if 'usuario_logado' not in session:  # Proteção para evitar acesso sem login
        return redirect(url_for('login'))

    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        especie = request.form['especie']
        descricao = request.form['descricao']
        imagem = request.files['imagem']

        # 📌 Salvar imagem na pasta correta
        if imagem:
            caminho_imagem = os.path.join("static/images", imagem.filename)
            imagem.save(caminho_imagem)
            caminho_imagem_relativo = f"images/{imagem.filename}"
        else:
            caminho_imagem_relativo = "images/default.jpg"  # Definir uma imagem padrão caso não seja enviada
        
        with sqlite3.connect('db.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO animais (nome, idade, especie, descricao, imagem) VALUES (?, ?, ?, ?, ?)",
                           (nome, idade, especie, descricao, caminho_imagem_relativo))
            conn.commit()
            
        return redirect(url_for('adocao'))

    return render_template('cadastro.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
