'''
    一、python3对多线程的支持是threading模块，应用这个模块可以创建多线程程序，并在多线程间进行同步和通讯
    二、创建线程的方法有两个
    三、通过threading.Thread直接在线程中运行函数
    四、通过继承threading.Thread类来创建线程
'''

# 五、用thread.Thread直接在线程中运行函数
import threading
import time

import filelock


def Thread_function_one(x, y):
    for i in range(x, y):
        print(i)

# 六、通过继承thread.Thread类来创建线程
# 这种方法只需要重载threading.Thread类的run方法，然后调用start（）开启线程就可以了
class Thread_function_three(threading.Thread):
    def run(self):
        for i in range(1, 20):
            print(i)
mythread_one = Thread_function_three()
mythread_two = Thread_function_three()

# 七、join（）作用是调用join（）的线程阻塞知道某一线程结束才继续执行
class Thread_function_four(threading.Thread):
    def run(self):
        self.i = 1
        print('{}'.format(self.i))
        self.i = self.i + 1
        time.sleep(1)
        print('{}'.format(self.i))
        time.sleep(1)
my_test_thread = Thread_function_four()

# 八、isAlive（）这个方法用于判断线程是否运行
# 1、当线程未调用start（）来开启时，isAlive（）会返回False
# 2、当线程已经执行后并结束时，isAlive（）也会发挥False
class Thread_function_five(threading.Thread):
    def run(self):
        time.sleep(2)
my_test_isalive_thread = Thread_function_five()

# 九、name属性表示线程的线程名默认是Thread-x，由1开始，第一个创建的线程名字就是THread-1
class Thread_function_verver(threading.Thread):
    def run(self):
        pass
test_mythread_one = Thread_function_verver()
test_mythread_two = Thread_function_verver()

# 十、daemon属性用来设置线程是否随主线程退出而退出
# 当daemon=False时，线程不会随主线程退出而退出（默认时，就是daemon=False）
# 当daemon=True时，当主线程结束，其他子线程也就会被强制结束
class Thread_function_eight(threading.Thread):
    def run(self):
        time.sleep(2)
        print("My thread over!")
test_mythreadd = Thread_function_eight()

# 线程的同步--锁
'''
当一个进程拥有多个线程之后，如果他们各做各的任务互没有关系还行，但既然属于同一个进程，他
们之间总是具有一定关系的。比如多个线程都要对某个数据进行修改，则可能会出现不可预料的结果，
为保证操作正确，就需要引入锁来进行线程间的同步。
threading模块提供了RLock锁（可重入锁）。对某一时间只能让一个线程操作的语句放到RLock的
acquire方法和release方法之间。即acquire（）方法相当于给RLock锁上锁，而release（）相当于解锁。
'''
class Thread_function_nine(threading.Thread):
    def run(self):
        global x
        lock.acquire()
        x += 10
        print("{}:{}".format(self.name, x))
        lock.release()

if __name__ == '__main__':
    print("Test threading!")
    # 用thread.Thread直接在线程中运行函数
    # test_one = threading.Thread(target=Thread_function_one, args=(1, 6))
    # test_two = threading.Thread(target=Thread_function_one, args=(10, 16))
    # test_one.start()
    # test_two.start()

    # 通过继承thread.Thread类来创建线程
    # mythread_one.start()
    # mythread_two.start()

    # join（）作用是调用join（）的线程阻塞知道某一线程结束才继续执行
    # my_test_thread.start()
    # my_test_thread.join()
    # my_test_thread.join()
    # print("Main thread voer!")

    # isAlive（）这个方法用于判断线程是否运行
    # print(my_test_isalive_thread.is_alive())
    # my_test_isalive_thread.start()
    # print(my_test_isalive_thread.is_alive())
    # time.sleep(3)
    # print(my_test_isalive_thread.is_alive())

    # name属性表示线程的线程名
    # test_mythread_one.name = 'Thread-ta'
    # test_mythread_two.start()
    # test_mythread_one.start()
    # print(test_mythread_one.name)
    # print(test_mythread_two.name)

    '''
    daemon属性用来设置线程是否随主线程退出而退出
    当 daemon = False 时，线程不会随主线程退出而退出（默认时，就是 daemon = False）
    当 daemon = True 时，当主线程结束，其他子线程就会被强制结束
    '''
    # def main():
    #     test_mythreadd.daemon = True
    #     test_mythreadd.start()
    #     print("Main thread over!")
    # main()

    # 线程的同步--锁
    x = 0
    lock = threading.RLock()
    def main():
        l = []
        for i in range(5):
            l.append(Thread_function_nine())
        for i in l:
            i.start()

    main()