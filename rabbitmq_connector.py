import pika

class RabbitCli():

    def send(self, productname, quantity):
        print('send do cli', flush=True)
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='hello')

        channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='{"productName":"'+productname+'","quantity":"'+quantity+'","status":"Created","orderId":123}')
        print(" [x] Sent Message!", flush=True)

        connection.close()

    def receive(self):
        pass