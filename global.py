#全局变量
num = 10

def GetValue():
    #局部变量
    #num = 100
    #如果需要访问全局变量,需要先声明
    global num
    num = 100

GetValue()

print(num)