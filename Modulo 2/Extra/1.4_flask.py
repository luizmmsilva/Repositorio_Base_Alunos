# Rota com numero


from flask import Flask
app = Flask(__name__) # representa o nome de um arquivo

@app.route('/') # decorador de função 
def homr():
    return "olá Mundo!"

@app.route('/sobre')
def sobre():
    return 'Olá, meu nome é Luiz Miguel e sou aprendiz em Phyton.'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f'Olá  {nome}! Seja bem-vindo(a)!'

@app.route('/dobro/<int:numero>')
def dobro(numero):
    return f'O dobro do {numero} é {2*numero}.'

if __name__ == '__main__':
    app.run(debug=True)