import time
import sys

import stomp

from marshmallow_dataclass import dataclass
from enum import Enum

import json
from recordclass import recordclass

import simplejson

def encode_complex(obj):
    if isinstance(obj, complex):
        return [obj.real, obj.imag]
    raise TypeError(repr(obj) + " is not JSON serializable")

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        #print('received a message "%s"' % message, flush=True)
        # Parse into a mutable object
        #data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
        #data = '{"quantity": 15, "name": "Danilo", "orderId": "50", "status": "Created", "productName": "RedBull"}'
        #user = json.loads(data, object_hook=lambda d: recordclass('X', d.keys())(*d.values()))
        user, err = User.Schema().loads(message)
        print(user,flush=True)
        print(message,flush=True)
        #print(str(user),flush=True)
        #print('queue processada!',flush=True)

class Connector():
    def connect():
        conn = stomp.Connection()
        conn.set_listener('', MyListener())
        conn.start()
        conn.connect('admin', 'admin', wait=True)
        conn.subscribe(destination='/queue/order-queue', id=1, ack='auto')

        #x = X()
        #x.name = "John Doe"
        #user_str = simplejson.dumps(x, default=encode_complex)

        user = User("Danilo","50","RedBull",15,OrderStatus.CREATED.value)
        user_json = User.Schema().dumps(user)
        user_str = user_json.data
        
        conn.send(body=user_str, destination='/queue/order-queue')
        time.sleep(2)
        conn.disconnect()

class X:
    name: str

class OrderStatus(Enum):
    CREATED = 'Created'
    PENDING = 'Pending'
    CONFIRMED = 'Confirmed'
    FAILED = 'Failed'

@dataclass
class User:
    def __init__(self, name, orderId, productName, quantity, status):
        self.name = name
        self.orderId = orderId
        self.productName = productName
        self.quantity = quantity
        self.status = status

    name: str
    orderId: str
    productName: str
    quantity: int
    status: str