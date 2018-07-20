import threading
import time
import random

def threadWorker():
    print (f'Current thread is {threading.current_thread()}')
    
threads = []

for i in range(10):
    thread = threading.Thread(target=threadWorker)
    thread.start()
    threads.append(thread)
    
for thread in threads:
    thread.join()