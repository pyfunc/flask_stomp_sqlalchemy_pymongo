Install from 
```bash
pip install -r requirements.txt
pip install --user -r requirements.txt
```

```bash
python3 main.py
```

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


### tutorial python com mongodb

https://realpython.com/introduction-to-mongodb-and-python/
