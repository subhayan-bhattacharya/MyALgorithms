# Sample code to see how threadcount is calculated.

import threading
import time

def worker(count):
    for c in range(count,-1,-1):
        threadname = threading.currentThread().getName()
        time.sleep(2)
        print ("Value of count {} from thread {}".format(c,threadname))
        
mainthreadname = threading.currentThread().getName()
print ("Starting new thread from main thread:",mainthreadname)
t1 = threading.Thread(target=worker,args=(10,))
t1.start()
#t1.join()
#print ("Main thread {} ending after child thread exits:".format(mainthreadname))
while True:
    threadcount = threading.active_count()
    if threadcount > 0:
        print ("Threadcount is :",threadcount)
        time.sleep(5)
    else:
        print ("Threadcount is 0...exiting")
        break