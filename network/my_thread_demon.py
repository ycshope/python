import threading
import queue
import time
#生产者消费者问题:queue+threading

#集成threading
class Run(threading.Thread):
    #初始化任务队列
    def __init__(self , name ,queue):
        #由于不会自动调用父进程的构造,所以先调用父进程的构造
        threading.Thread.__init__(self, name=name)
        #python中的队列用于线程之间的通讯,并且自带锁
        #Queue是先进先出队列
        #任务队列
        self.__queue = queue
        #线程名
        self.__name = name
    #重写run,start会默认执行
    #从列队中拿出元素
    def run(self):
        while not self.__queue.empty():
            data = self.__queue.get()
            print(f"{self.__name} : data ={data}")
            #time.sleep(0.01)   #不sleep,可能会导致部分线程没有启动
            
def Create_Threads(threads_count:int, data_list:list):
    #线程列表
    threads_list = []
    #线程数量
    threads_count = threads_count
    #任务队列
    run_queue = queue.Queue()
    
    #生成任务列队
    for data in data_list:
        run_queue.put(data)

    #生成线程列表    
    for i in range(threads_count):
        #!!!!!!!!!!列队相当于传值!!!!!!!!!!!
        threads_list.append(Run(queue=run_queue ,name=i))
        
    #线程列表启动
    for thread in threads_list:
        thread.start()
    
    #等待所有子线程结束,并回收
    for threads in threads_list:
        threads.join()
        

if __name__ == "__main__":
    data_list = []
    for i in range(1,255):
        data_list.append("192.168.3."+str(i))
    Create_Threads(threads_count=100 ,data_list=data_list)