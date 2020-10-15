def DoubleValue(num):
    return num*2

#写法1
def GetValue1(num):
    my_list = []    #不定义下面的列表没法返回函数
    for i in range(num):
        my_list.append(DoubleValue(i))
    return my_list
    
#写法2:重点
def GetValue2(num):
    '''
        1.表示返回的是数组
        2.表示DoubleValue(i)执行了num次
        3.把DoubleValue(i)的每次结果放入list中
    '''
    return [DoubleValue(i) for i in range(num)]

if __name__ == "__main__":
    num = int(input("enter a num,return double list"))
    print(GetValue1(num))
    print(GetValue2(num))
        
