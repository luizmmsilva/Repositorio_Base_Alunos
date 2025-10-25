# Exercicio 2.1: HTML básivo na resposta
# Modificar sua rota principal para retornar um pequeno html um pequeno html com título,
# parágrafo e um link para outra rota.
# Usar 'rende template para renderizar um arquivo .html


from flask import Flask, render_template
app = Flask(__name__) # representa o nome de um arquivo

@app.route('/') # decorador de função 
def home():
    return render_template('ex_2-1.html')

@app.route('/sobre')
def sobre():
    return 'Fábrica de Programadores'

@app.route('/chiquinho')
def chiquinho():
    return 'Achou a rota'

if __name__ == '__main__':
    app.run(debug=True)