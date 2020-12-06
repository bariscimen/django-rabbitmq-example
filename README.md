
# Django Distributed System Example with Celery  
  
The purpose of this repository is to show event-based development practices on [Django](https://www.djangoproject.com/).  
 
In this example, there are two microservices: Order Application and Invoice Application. When an order is created on the Order App, it sends a message to the Invoice App via RabbitMQ to create an invoice for the order. Then, the Invoice App calculates the total taxes and creates an invoice.
 
## Installation  
  
Development environment requirements:  
  
- [Docker](https://www.docker.com)  
- [Docker Compose](https://docs.docker.com/compose/install/)  
  
Setting up your development environment on your local machine:  
```bash  
$ git clone https://github.com/bariscimen/django-rabbitmq-example
$ cd django-rabbitmq-example  
$ docker-compose up -d  
```  
  
Now you can access the order application UI and create random orders to examine the operations of the distributed system via [http://localhost:8080](http://localhost:8080).  
 
## Accessing The RabbitMQ Server  
  
The RabbitMQ instance will be started as a container by the docker-compose.   
You can access the instance via [http://localhost:15672](http://localhost:15672). Default `username:password` is `guest:guest`.  

#### Credits

- Django
- Celery
- React
- RabbitMQ
- PostgreSQL

