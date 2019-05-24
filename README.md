configure as variávels:  
`export PYTHON_HOME=/f/python/python37`  
`export PROJECT_HOME=f:\\labs\\py` #um bug na versao para windows (usando gitbash)  
`export PYTHON_SCRIPTS=/f/python/python37/Scripts`  
`export WORKON_HOME=~/.virtualenvs`  
`export PATH=$PATH:$PYTHON_HOME:$PYTHON_SCRIPTS:$PROJECT_HOME`  

use os comandos:  
`source $PYTHON_SCRIPTS/virtualenvwrapper.sh` #para configurar o virtualenvwrapper (assim os comandos ficam disponíveis no bash)  

`mkproject <nomedoprojeto>` #para criar virtualenv e um diretorio para um projeto novo  

`workon <nomedoprojeto>` #para ativar um projeto existente  

instale o microframework flask:  
`pip install flask`  

### instalação para o activemq  
instale a biblioteca para stomp:  
`pip install stompest`  

### instalação para o rabbitmq  
`pip install pika --upgrade` 

instale as bibliotecas para transformar objetos python em json e vice-versa:  
`pip install marshmallow-dataclass`  
`pip install marshmallow-enum`  

### instalação dos plugins para mysql/sqlalchemy  

`pip install sqlalchemy`  
`pip install Flask-SQLAlchemy`
`pip install pymysql`  

### tutorial python com mongodb

https://realpython.com/introduction-to-mongodb-and-python/

### configurando debug

`pip install PDBSublimeTextSupport`

no sublime instale o pacote: Python Breakpoint