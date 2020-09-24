#时间函数
import time

def Wait_Time(num):
    for i in range(num):
        time.sleep(1)   #等待疫苗
        print("*")

def Get_List(num):
    return [i for i in range(1,num)] #注意这种写法

if __name__ == "__main__":
    num = input("输入要等待的秒数")
    Wait_Time(int(num))
    My_list = Get_List(int(num))
    print(My_list)
    num = input("请输入要删除list的位数")
    #删除元素
    del My_list[int(num)]
    print(My_list)
    Default_List = Get_List(int(num))
    print(Default_List)
    print(["*"]*10) #list的乘法
    #print(cmp(Default_List,My_list)) #比较列表的元素内容
    print("最大值为:%d,最小值:%d,长度为:%d"%(max(My_list),min(My_list),len(My_list)))   #最大值,最凶啊只
    