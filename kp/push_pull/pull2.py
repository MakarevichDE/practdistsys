import time
import zmq
import random


consumer_id = random.randrange(1,1000)
print "Я клиент #%s" % (consumer_id)
context = zmq.Context()
# recieve work
consumer_receiver = context.socket(zmq.PULL)
consumer_receiver.connect("tcp://192.168.56.101:5557")
# send work
consumer_sender = context.socket(zmq.PUSH)
consumer_sender.connect("tcp://192.168.56.101:5558")
    
while True:
    work = consumer_receiver.recv_json()
    data = work['num']
    result = { 'consumer' : consumer_id, 'num' : data}
    if data%2 == 0: 
         consumer_sender.send_json(result)