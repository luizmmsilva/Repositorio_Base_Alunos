# Exercicio 3.1: templates com estrutura de controle
# Passe uma lista de nomes para o teplate e use um for em Jinja para
# listar todos os nomes em <ul>



from flask import Flask, render_template
app = Flask(__name__) # representa o nome de um arquivo

@app.route('/') # decorador de função 
def index():
     return 'Hello Flask!'

@app.route('/sobre')
def sobre():
    return 'Olá, eu sou o mais top dos alunos da fabrica de programadores.'

@app.route('/lista')
def lista():
    alunos = ['Kauan','Luana','Miguel','Thiago']
    return render_template('ex_3-2.html',lista=alunos)






if __name__ == '__main__':
    app.run(debug=True)