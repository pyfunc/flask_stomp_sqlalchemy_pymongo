from flask import Flask, render_template
from flask import request

import stomp_connector
import rabbitmq_connector

import dao

app = Flask(__name__)  
 
@app.route('/hello_world')
def hello_world():
	return 'Hello, World!'

@app.route('/')
def home():
  return render_template('home.html')
 
@app.route('/about')
def about():
  stomp_connector.Connector.connect()
  return render_template('about.html')

@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html')

@app.route('/rabbit_enviar', methods=['POST'])
def rabbit_enviar():
    print('metodo rabbit enviar', flush=True)
    productname=request.form['name']
    quantity=request.form['quantity']
    print('product:'+productname,flush=True)
    print('quantity:'+quantity,flush=True)
    cli = rabbitmq_connector.RabbitCli()
    cli.send(productname, quantity)
    filmes = dao.Dao()
    filmes.gravar()
    return "ok"

if __name__ == '__main__':
  app.run(debug=True)