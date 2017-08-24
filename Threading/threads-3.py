import time
import logging
import threading

logging.basicConfig(filename="threading.log",level=logging.DEBUG)

def worker(count):
    for c in range(count,-1,-1):
        threadname = threading.currentThread().getName()
        threadcount = threading.active_count()
        threadnames = threading.enumerate()
        logging.debug("Child thread: {} continuing with threadcount {} {} and counter value: {}".format(threadname,threadcount,threadnames,c))
        time.sleep(2)
    
mainthread = threading.currentThread().getName()
print ("Starting main thread:",mainthread)
t1 = threading.Thread(target=worker,args=(10,))
#t1.setDaemon(True)
t1.start()
time.sleep(5)
#t1.join()
print ("Attempting to close main thread:",mainthread)