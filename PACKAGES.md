
configure as variávels:  
```bash
export PYTHON_HOME=/f/python/python37 
export PROJECT_HOME=f:\\labs\\py#um bug na versao para windows (usando gitbash)
export PYTHON_SCRIPTS=/f/python/python37/Scripts 
export WORKON_HOME=~/.virtualenvs 
export PATH=$PATH:$PYTHON_HOME:$PYTHON_SCRIPTS:$PROJECT_HOME 
```

use os comandos:  
```bash
source $PYTHON_SCRIPTS/virtualenvwrapper.sh#para configurar o virtualenvwrapper (assim os comandos ficam disponíveis no bash)  
```

mkproject <nomedoprojeto>#para criar virtualenv e um diretorio para um projeto novo  


workon <nomedoprojeto>#para ativar um projeto existente  

instale o microframework flask:  
 
```bash
pip install flask 
``` 

### instalação para o activemq  

instale a biblioteca para stomp:  


```bash
pip install stompest
``` 

### instalação para o rabbitmq  
 
```bash
pip install pika --upgrade
``` 

instale as bibliotecas para transformar objetos python em json e vice-versa:  
 
```bash
pip install marshmallow-dataclass 
``` 

```bash
pip install marshmallow-enum 
``` 

### instalação dos plugins para mysql/sqlalchemy  
 

```bash
pip install sqlalchemy 
``` 

```bash
pip install Flask-SQLAlchemy 
``` 


```bash
pip install pymysql 
``` 

### tutorial python com mongodb

https://realpython.com/introduction-to-mongodb-and-python/

### configurando debug

 
```bash
pip install PDBSublimeTextSupport
```

no sublime instale o pacote: Python Breakpoint