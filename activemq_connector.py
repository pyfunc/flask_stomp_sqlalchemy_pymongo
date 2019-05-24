import time
import sys

import stomp

from marshmallow_dataclass import dataclass
from enum import Enum

def encode_complex(obj):
    if isinstance(obj, complex):
        return [obj.real, obj.imag]
    raise TypeError(repr(obj) + " is not JSON serializable")

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        produto, err = Produto.Schema().loads(message)
        print(produto,flush=True)
        print(message,flush=True)


class Connector():
    def connect():
        conn = stomp.Connection()
        conn.set_listener('', MyListener())
        conn.start()
        conn.connect('admin', 'admin', wait=True)
        conn.subscribe(destination='/queue/order-queue', id=1, ack='auto')

    def send(nome, quantidade):
        product = Produto("50",nome,quantidade,PedidoStatus.CREATED)
        produto_json = Produto.Schema().dumps(produto)
        produto_str = produto_json.data
        conn.send(body=produto_str, destination='/queue/order-queue')
        time.sleep(2)

    def disconnect():
        conn.disconnect()

class PedidoStatus(Enum):
    CREATED = 'Created'
    PENDING = 'Pending'
    CONFIRMED = 'Confirmed'
    FAILED = 'Failed'

@dataclass
class Product:
    def __init__(self, id, nome, quantidade, status):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.status = status

    id: str
    nome: str
    quantidade: int
    status: PedidoStatus