from flask import Flask, render_template
from flask import request

#import activemq_connector
import rabbitmq_connector

import dao

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html')


@app.route('/rabbit_enviar', methods=['POST'])
def rabbit_enviar():
    nome = request.form['nome']
    quantidade = request.form['quantidade']
    cli = rabbitmq_connector.RabbitCli()
    cli.send(nome, quantidade)
    produtoDao = dao.ProdutoDao()
    produtoDao.gravar(nome, quantidade, status)
    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
