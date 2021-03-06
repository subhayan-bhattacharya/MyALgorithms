import threading
import urllib.request
import time

def downloadImage(imagePath, filename):
    print(f'Downloading image from {imagePath}')
    urllib.request.urlretrieve(imagePath, filename)

def executeThread(i):
    imageName = r"C:\Users\SUSUBHAT.ORADEV\Desktop\Codes\Current\Threads\images" + "\\" + str(i) + ".jpg"
    downloadImage("https://httpbin.org/image/jpeg", imageName)

def main():
    t0 = time.time()
    threads = []
    for i in range(10):
        thread = threading.Thread(target=executeThread, args=(i,))
        threads.append(thread)
        thread.start()
    for i in threads:
        i.join()
    t1 = time.time()
    totalTime = t1 - t0
    print(f"Total execution time : {totalTime}")

if __name__ == "__main__":
    main()
