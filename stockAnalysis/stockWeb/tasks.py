from celery import Celery

import time

#app = Celery('tasks', backend='amqp', broker='pyamqp://')
app = Celery('tasks', backend="amqp", broker='amqp://guest@localhost:5672//')


@app.task
def add(x, y):    
    return x + y