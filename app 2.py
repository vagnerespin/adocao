from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'chave_secreta_segura'

def init_db():
    with sqlite3.connect('db.sqlite3') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nome TEXT,
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
        conn.commit()

@app.route('/')
def index():
    with sqlite3.connect('db.sqlite3') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM animais")
        animais = cursor.fetchall()
    return render_template('index.html', animais=animais)

@app.route('/adocao')
def adocao():
    with sqlite3.connect('db.sqlite3') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM animais")
        animais = cursor.fetchall()
    return render_template('adocao.html', animais=animais)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        especie = request.form['especie']
        descricao = request.form['descricao']
        imagem = request.form['imagem']
        with sqlite3.connect('db.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO animais (nome, idade, especie, descricao, imagem) VALUES (?, ?, ?, ?, ?)",
                           (nome, idade, especie, descricao, imagem))
            conn.commit()
        return redirect(url_for('adocao'))
    return render_template('cadastro.html')

@app.route('/animal/<int:id>')
def get_animal(id):
    with sqlite3.connect('db.sqlite3') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM animais WHERE id = ?", (id,))
        animal = cursor.fetchone()
    return render_template('animal_detail.html', animal=animal)

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
        return redirect(url_for('index'))

    return render_template('cadastro_adotante.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
