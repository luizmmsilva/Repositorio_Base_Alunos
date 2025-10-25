
#Exercico 3.1: Templates com variaveis 
# Modifique o template para recebr o nome como variavel e exibir bem vindo




from flask import Flask, render_template
app = Flask(__name__) # representa o nome de um arquivo

@app.route('/') # decorador de função 
def index():
     return 'Hello flask!'

@app.route('/sobre')
def sobre():
    return 'Olá, eu sou o mais top dos alunos da fabrica de programadores.'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return render_template('ex_3-1.html', nome=nome)


if __name__ == '__main__':
    app.run(debug=True)