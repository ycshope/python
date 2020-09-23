#定义函数注意不要携带类型
def function1(a,b):
    print("我是"+__name__+"函数内的调用,如果tab不对其,那么可能不再函数体内")
    print(a,b)
    print(type(a),type(b))

if __name__ == "__main__":
    #这种写法用于单元测试,防止别的模块调用时会调用到下面的代码
    print("我是函数外,请注意间隔")
    a=function1(9,"hello")
    print(a)
    print(type(a))
    #__name__是表示当前模块的名
    print("funcion的模块名为"+__name__)