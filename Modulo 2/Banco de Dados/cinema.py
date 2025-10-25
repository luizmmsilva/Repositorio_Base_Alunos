# Criar o banco de dados e conexão 
import sqlite3
con =  sqlite3.connect('cinema.db') # cria ou se conecta a um banco existente

# Criar um objeto cursor
cur = con.cursor()

# Criar tabelas
cur.execute('CREATE TABLE IF NOT EXISTS filme(titulo,ano,duracao)')
# retorna com o endereço de memória da tabela 

# Verificar se a tabela foi cirada
res = cur.execute('SELECT name FROM sqlite_master')
print(res.fetchall())

# Inserir dados
cur.execute('''INSERT INTO filme VALUES
            ('Carros',2006,150),
            ('GEnte Grande 2',2013,130)''')
con.commit() # tudo que altera tem que salvar

# verificar dados se foi inserido
res = cur.execute('SELECT titulo FROM filme')
print(res.fetchall())
dados_filme = [
    ('Velozes e Furiosos 7',2015,90),
    ('O espanta Tubarões',2004, 70),
]
cur.executemany('INSERT INTO filme (titulo,ano,duracao) VALUES(?,?,?)', dados_filme)
con.commit()

res = cur.execute('SELECT tituylo FROM filme')
print(res.fetchall())

# Outra forma de verificar dados inseridos
for linha in cur.execute('SELECT ano,titulo FROM filme ORDER by por ano'):
    print(linha)

con.close() # para fechar a conexão
