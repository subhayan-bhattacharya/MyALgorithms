import threading
import time

def threadWorker():
    print ("Thread in running state")
    time.sleep(10)
    print ("Terminating")
    
myThread = threading.Thread(target=threadWorker)

myThread.start()

myThread.join()

print("Thread enters dead state")