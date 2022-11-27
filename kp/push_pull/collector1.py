import time
import zmq
import pprint

context = zmq.Context()
results_receiver = context.socket(zmq.PULL)
results_receiver.bind("tcp://192.168.56.101:5558")
collecter_data = {}
for x in xrange(20):
    result = results_receiver.recv_json()
    if collecter_data.has_key(result['consumer']):
        collecter_data[result['consumer']] = collecter_data[result['consumer']] + 1
    else:
        collecter_data[result['consumer']] = 1
    if x == 999:
        pprint.pprint(collecter_data)

