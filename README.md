# Chasing the rabbit
Playing around with Python, Pika and RabbitMQ\
(Based on https://www.rabbitmq.com/tutorials)

#### Installation instructions
* Pika needs a local rabbitmq server which can be run with the offical docker image of rabbitmq: \
`docker run -d --hostname my-rabbit --name some-rabbit -p 8080:15672 -p 5672:5672 rabbitmq:3-management`

#### Management Console
* http://localhost:8080/
* guest/guest
