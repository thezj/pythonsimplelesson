import _thread
import threading
import time
import queue
'''
#为线程定义一个函数
def print_time(threadname, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print('{0},{1}'.format(threadname, time.time()))


try:
    _thread.start_new_thread(print_time, ('thread1', 1))
    _thread.start_new_thread(print_time, ('thread2', 1))
except:
    print('error:无法启动线程')
while 1:
   pass



#创建一个锁
threadLock = threading.Lock()
threads = []


class printtimethread(threading.Thread):
    def __init__(self, name, counter, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
        self.delay = delay

    def run(self):
        print(self.name + '开始')
        #获取锁，用于线程同步
        threadLock.acquire()
        while self.counter:
            time.sleep(self.delay)
            print('{0}:{1}'.format(self.name, time.time()))
            self.counter -= 1
        print(self.name + '退出')
        #释放锁，开启下一个线程
        threadLock.release()


#创建新线程
thread1 = printtimethread('thread-1', 3, 1)
thread2 = printtimethread('thread-2', 3, 1)

#开启新线程
thread2.start()
thread1.start()
#阻塞等待线程结束
thread1.join()
thread2.join()


print('主线程结束')

'''

queuelock = threading.Lock()
threadlist = ['t1', 't2', 't3', 't4', 't5', 't6']
threads = []

workqueue = queue.Queue(10)
namelist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#队列填充数据
for word in namelist:
    workqueue.put(word)


class processdatethread(threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q

    def run(self):
        print(self.name, '开启')
        times = 0
        while not workqueue.empty():
            queuelock.acquire()
            data = self.q.get()
            queuelock.release()
            print('{0}:processing----{1}'.format(self.name, data))
            time.sleep(1)
            times += 1
        print(self.name, '关闭',times,'次工作')


for tname in threadlist:
    thread = processdatethread(tname, workqueue)
    thread.start()
    threads.append(thread)

# 等待所有线程完成
for t in threads:
    t.join()

print('退出主线程')