# Importação da bibliot3eca sqlite3
import sqlite3

# Criar o banco de dados
produto = 'produtos.db'

# Criar Tabela 
script_produtos = '''CREATE TABLE IF NOT EXISTS Produtos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    preco REAL NOT NULL,
                    categoria TEXT NOT NULL,
                    estoque INTEGER NOT NULL
                    );'''
try:
    with sqlite3.connect(produto) as con:
    # Criar um cursor
        cur = con.cursor()

        # EXecutar o script
        cur.execute(script_produtos)

        #SAlvar as alterações no banco de dados
        con.commit()
        print('Tabela Criada com sucesso')
except sqlite3.OperationalError as e:
    print('Erro:', e)

# Verificar se a tabela foi criada
res = cur.execute('SELECT name FROM sqlite_master')
res.fetchall() # Retorna uma linha do resultado obtido, tabela
# resultado vem no formato tupla

# Consulta tabelas

sql = 'SELECT * FROM Produtos'

try:
    with sqlite3.connect(produto) as con:
        cur = con.cursor()
        cur.execute(sql)
        res = cur.fetchall() # retorna uma lista de lista
        print(res)
except sqlite3.OperationalError as e:
    print('Erro' ,)

# iNSERIR DADOS

sql = 'INSERT INTO produtos(nome, preco, categoria, estoque) VALUES(?, ?, ?, ?)'

try:
    with sqlite3.connect(produto) as con:
        cur = con.cursor()
        cur.execute(sql,('Notebook Dell' ,2500.00,'Eletrônicos', 20))
        con.commit()
except sqlite3.OperationalError as e:
    print('Erro', e)

# inserir vários dados

produtos = [
    ('Notebook', 3500.00,'Eletrônicos', 10),
    ('Smartphone', 2100.00, 'Eletrônicos', 15),
    ('Geladeira', 4500.00, 'Eletrodomésticos', 15),
    ('Camiseta', 45.99, 'Vestuário',50),
    ('Capacete', 240, 'Acessórios',20)
]

try:
    with sqlite3.connect(produto) as con:
        cur =con.cursor()
        cur.executemany('INSERT INTO Produtos(nome,preco,categoria,estoque) VALUES(?,?,?,?)',
                        produtos) # comando para inserir cvários dados de uma vez
        con.commit()
        print('Produtos inseridos com sucesso')
except sqlite3.OperationalError as e:
    print ('Erro:', e)

# Verificar se os dados foram adicionados corretamente
res = cur.execute('SELECT nome FROM Produtos')
print(res.fetchall()) # esse comando busca todos os registros 

# Ataulizar registro

sql = 'UPDATE Produtos SET preco = ? WHERE id = ?'

try:
    with sqlite3.connect(produto) as con:
        cur = con.cursor()
        cur.execute(sql,(5000.00,1))
        con.commit()
except sqlite3.OperationalError as e:
    print('Erro:', e)


# Deletear rEGISTROS

sql = 'DELETE FROM Produtos Where  id = ?'

try:
    with sqlite3.connect(produto) as con:
        cur = con.cursor()
        cur.execute(sql,(1,))
        con.commit()
except sqlite3.OperationalError as e:
    print('Erro:', e)

# Fechar conexão. Após concluir precisamos fechar a conexão com o banco