import threading
import time
import random

def myChildThread():
    print (f'Child thread name {threading.current_thread()}')
    print (f'Main thread is -----')
    print (f'Main thread for this child is {threading.main_thread()}')
    
    
child = threading.Thread(target=myChildThread)
child.start()
child.join()
    