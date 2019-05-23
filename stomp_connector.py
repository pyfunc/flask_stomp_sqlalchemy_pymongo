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
        user, err = User.Schema().loads(message)
        print(user,flush=True)
        print(message,flush=True)


class Connector():
    def connect():
        conn = stomp.Connection()
        conn.set_listener('', MyListener())
        conn.start()
        conn.connect('admin', 'admin', wait=True)
        conn.subscribe(destination='/queue/order-queue', id=1, ack='auto')

        user = User("Danilo","50","RedBull",15,OrderStatus.CREATED)
        user_json = User.Schema().dumps(user)
        user_str = user_json.data
        
        conn.send(body=user_str, destination='/queue/order-queue')
        time.sleep(2)
        conn.disconnect()

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
    status: OrderStatus