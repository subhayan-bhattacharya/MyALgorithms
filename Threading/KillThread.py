from multiprocessing import Process
import time

def myWorker():
    t1 = time.time()
    print (f'Process started at {t1}')
    time.sleep(20)
    
myProcess = Process(target=myWorker)
print (f'Started process {myProcess}')
myProcess.start()
print (f'Terminating process {myProcess}')
myProcess.terminate()
myProcess.join()
print (f'Terminated process {myProcess}')