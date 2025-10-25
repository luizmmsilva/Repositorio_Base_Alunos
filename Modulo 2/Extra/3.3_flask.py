from flask import Flask, render_template
app = Flask(__name__) # representa o nome de um arquivo

@app.route('/') # decorador de função 
def index():
     return 'Hello Flask!'

@app.route('/sobre')
def sobre():
    return 'Olá, eu sou o mais top dos alunos da fabrica de programadores.'

@app.route('/idade/<int:idade>')
def idade(idade):
    return render_template('ex_3-3.html',idade=idade)


if __name__ == '__main__':
    app.run(debug=True)