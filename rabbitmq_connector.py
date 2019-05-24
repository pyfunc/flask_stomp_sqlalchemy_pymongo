import pika

class RabbitCli():

    def send(self, nome, quantidade):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='pedidos_de_produtos')

        channel.basic_publish(exchange='',
                      routing_key='pedidos_de_produtos',
                      body='{"nome":"'+nome+'","quantidade":"'+quantidade+'","status":"Created","id":123}')
        print(" [x] Sent Message!", flush=True)

        connection.close()

    def receive(self):
        pass