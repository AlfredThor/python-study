import _thread
import time

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("{}:{}".format(threadName, time.ctime(time.time())))

if __name__ == '__main__':
    try:
        _thread.start_new_thread(print_time,("Thread-1", 2))
        _thread.start_new_thread(print_time,("Thread-2", 4))
    except:
        print("Error")
    while 1:
        pass