import zmq
 
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://192.168.56.101:5556")
socket.setsockopt(zmq.SUBSCRIBE, "netherlands")
socket.setsockopt(zmq.SUBSCRIBE, "germany")
 
while True:
    print  socket.recv()