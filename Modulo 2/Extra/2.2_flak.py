# Exercico 2.2 Links entres roatas 
# Adiconar # Exercicio 2.2: Links entre rotas
# Adicionar um menu de navegação simples com links para todas as suas rotas(/,/sobre,/saudacao, etc.)
# Passar a variavél através do 'url for'
# dentro do script html: ("{{url_for('saudacao'), nome='Joãozinho'}}")
#saudacao é o nome da função Python que define a rota espera (<nome>)




from flask import Flask, render_template
app = Flask(__name__) # representa o nome de um arquivo

@app.route('/') # decorador de função 
def home():
     return render_template('ex_2-2.html')

@app.route('/sobre')
def sobre():
    return 'Olá, eu sou o mais top dos alunos da fabrica de programadores.'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f'Olá  {nome}! Seja bem-vindo(a)!'

@app.route('/dobro/<int:numero>')
def dobro(numero):
    return f'O dobro do {numero} é {2*numero}.'

if __name__ == '__main__':
    app.run(debug=True)