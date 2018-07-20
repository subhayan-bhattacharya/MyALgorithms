import threading
import time
import random

def myThread(i):
    print (f'Thread started {i}')
    time.sleep(random.randint(1,5))
    print (f'Thread {i} finished')
    
def main():
    for i in random.randint(2,50)):
        thread = threading.Thread(target=myThread,args=(i,))
        thread.start()
        
    time.sleep(4)
    print (f'Total number of active threads : {threading.active_count()}')
    
if __name__ == "__main__":
    main()
