# Sample code to see how threadcount is calculated.

import threading
import time

def worker(count):
    for c in range(count,-1,-1):
        threadname = threading.currentThread().getName()
        time.sleep(2)
        print ("Value of count {} from thread {}".format(c,threadname))
        threadcount = threading.active_count()
        print ("Threadcount is :",threadcount)
        print ("Active threads :",threading.enumerate())
        
mainthreadname = threading.currentThread().getName()
print ("Starting new thread from main thread:",mainthreadname)
t1 = threading.Thread(target=worker,args=(10,))
t1.start()
time.sleep(5)
print ("main thread exiting!")