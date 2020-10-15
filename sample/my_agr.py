#必备传参
def fun1(a,b):
    print("必备传参")
    print(a)
    print(b)
 
#命名传参(可以选择根据名字传参)
def fun2(d,e):
    print("命名传参")
    print(d)
    print(e)
    
#缺省传参,缺省参数只能在最右边
def fun3(a,b,c=4):
    print("缺省传参")
    print(a)
    print(b)
    print(c)

#不定长传参关键字 *args
def fun4(a,*args):
    #*arg返回类型是一个元组
    print("不定长传参")
    print(a)    #返回第一个参数
    print(args)    #返回多余参数

def fun5(a,**kwarg):#不定长传参关键字 **kwarg
    #**kwarg返回类型是dict
    print("不定长传参")
    print(a)    #返回第一个参数
    print(kwarg)    #返回多余参数
    
if __name__ == "__main__":
    a = 1
    b = 2
    fun1(a,b)
    print("-"*50)
    fun2(e=a,d=b)
    print("-"*50)
    fun3(a,b)
    print("-"*50)
    fun4(1,2,3,4,5,6,7)
    print("-"*50)
    fun5(1,name="Harry Potter",age=20) #注意key不能是str,这是定义
    