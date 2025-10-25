# No terminal instalar o flask com comando: pip install flask
# Criar um app flask báisco que exibe "Olá Mundo!" na rota principal('/)

from flask import Flask
app = Flask(__name__) # representa o nome de um arquivo


@app.route('/') # decorador de função 
def homr():
    return "olá Mundo!"

if __name__ == '__main__':
    app.run(debug=True)

