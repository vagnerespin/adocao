
from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastro_adotante')
def cadastro_adotante():
    return render_template('cadastro_adotante.html')

@app.route('/adocao')
def adocao():
    conn = sqlite3.connect('adocao.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animais")
    animais = cursor.fetchall()
    conn.close()
    return render_template('adocao.html', animais=animais)

@app.route('/animal/<int:id>')
def animal_detail(id):
    conn = sqlite3.connect('adocao.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animais WHERE id = ?", (id,))
    animal = cursor.fetchone()
    conn.close()
    if animal:
        return render_template('animal_detail.html', animal=animal)
    else:
        return "Animal não encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)
