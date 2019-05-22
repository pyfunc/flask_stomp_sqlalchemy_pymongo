from flask import Flask, render_template

import stomp_connector

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

if __name__ == '__main__':
  app.run(debug=True)