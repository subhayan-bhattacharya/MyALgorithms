import os

def child():
    print (f"We are in the child process which has a pid of {os.getpid()}")
    
def parent():
    print (f"We are in the parent process which has a pid of {os.getpid()}")
    ref = os.fork()
    if ref == 0:
        #We are in the child hence child specific code should run which is the child function
        child()
    else:
        print (f'Inside parent process which has a child having the pid {ref}')
        
parent()