# Rota personalizada



from flask import Flask
app = Flask(__name__) # representa o nome de um arquivo

@app.route('/') # decorador de função 
def homr():
    return "olá Mundo!"

@app.route('/sobre')
def sobre():
    return 'Olá, meu nome é Luiz Miguel e sou aprendiz em Phyton.'

if __name__ == '__main__':
    app.run(debug=True)
