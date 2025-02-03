import threading
import time
def deamon_threads():
    while True:
        print("deamon threads is running")
        time.sleep(2)
thread=threading.Thread(target=deamon_threads,daemon=True)
thread.start()
time.sleep(3)
print("main thread is closed")