import zmq
import time
 
context = zmq.Context()
push_socket= context.socket(zmq.PUSH)
 
push_socket.bind('tcp://192.168.56.101:5557')
 
 
for x in xrange(20):
    msg = { 'num' : "Сообщение № " str(x) }
    print "->",msg
    push_socket.send(msg)
    #Pause 1 second
    time.sleep(1)