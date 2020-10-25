import threading
import time
import my_url
import re
#返回当前时间
def get_time():
    localtime = time.localtime(time.time())
    return time.asctime(localtime)
#线程函数:返回访问百度的时间
def fun1(url,pattren):
    src = my_url.Get_Url(url)
    result = re.findall(pattren,src)
    print(f"url is {url},return result is {result}")
    
#多线程调用函数
def main():
    print(f"主线程开始:localtime is "+get_time())
    
    #定义各个线程的传入参数
    thread_args_list = ["http://www.baidu.com" , "http://bilibili.com" , "http://www.csdn.net"]
    pattren = "<title>(.*)</title>"
    
    #创建线程
    threads_list = []
    for thread_args in thread_args_list:
        #指定函数和参数
        threads_list.append(threading.Thread(target=fun1,args=(thread_args,pattren,)))
    #函数开始
    for threads in threads_list:
        threads.start()
    #等待所有子线程结束,并回收
    for threads in threads_list:
        threads.join()
        
    print(f"主线程结束:localtime is "+get_time())
    
if __name__ == "__main__":
    main()