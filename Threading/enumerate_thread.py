import threading
import time
import random

def myThread(i):
    print (f'Thread started {i}')
    time.sleep(random.randint(1,5))
    print (f'Thread {i} finished')
    
def main():
    for i in range(10):
        thread = threading.Thread(target=myThread,args=(i,))
        thread.start()
    print (f'Enumerating threads : {threading.enumerate()}')
    time.sleep(4)
    print(f'Checking active threads : {threading.active_count()}')
    print (f'Checking the current running threads : {threading.enumerate()}')
    
if __name__ == "__main__":
    main()