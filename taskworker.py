import time, sys, Queue
from multiprocessing.managers import BaseManager

#create class QueueManager
class QueueManager(BaseManager):
    pass

#only get queue from the internet, just get name
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#connect server that is a excuting taskmanager.py computer
server_addr = '127.0.0.1'
print('Connect to server %s...' %server_addr)

#being the same of taskmanager.py
m = QueueManager(address=(server_addr, 5000), authkey='abc')

#connect the internet
m.connect()

#get the object Queue
task = m.get_result_queue()

#getting tasks from the task queue, writing the result in the result queue
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' %(n, n))
        r = '%d * %d = %d' %(n, n, n * n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')

#exit
print('worker exit.')
