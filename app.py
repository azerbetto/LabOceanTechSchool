from flask import Flask

app = Flask("meu app")

@app.route('/')
def hello():
    return "Hello World"

@app.route('/teste')
def teste():
    return "<h1> Teste de Rota</h1>"
