import sqlite3

conn = sqlite3.connect('adocao.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS animais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade TEXT,
    especie TEXT,
    descricao TEXT,
    imagem TEXT
)
''')

conn.commit()
conn.close()

print("Banco de dados e tabela 'animais' criados com sucesso.")
