import threading
import time
import random

def threadWorker():
    print (f'Thread starting is  {threading.currentThread().getName()}')
    print (f'Starting {threading.current_thread()}')
    time.sleep(10)
    print (f'Thread exiting is {threading.currentThread().getName()}')
    print (f'Ending {threading.current_thread()}')
    
for i in range(10):
    threadName = "ThreadName-" + str(i)
    thread = threading.Thread(name=threadName,target=threadWorker)
    thread.start()
    
print (f'{threading.enumerate()}')
    