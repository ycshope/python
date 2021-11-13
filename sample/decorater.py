'''
装饰器的概念:
可以同一个类给另一个类添加功能
称第一个类为一个装饰器
本质和C++的多态没什么区别
原则不修改原来的类的代码

主要用法:
本來已經有了一個函數,希望添加新的功能并且不改變原有的功能

裝飾器與閉包:
    僅僅是傳入參數的不同,裝飾器的傳參是函數,閉包傳參是數據類型
'''
#装饰器,把需要装饰的函数作为参数
def Digivice(base):
    def evolve():   #闭包
        base()      #先調用原函数
        #装饰的函数
        if base.__name__ == "Agumon":
                print("evolve to Greymon")
        elif base.__name__ == "Greymon":
            print("evolve to Metal_Greymon")
        elif base.__name__ == "Metal_Greymon":
            print("evolve to War_Greymon")
    return evolve

def Metal_Garurumon(base):
    def Funsion_Digivice():
        base()
        if base.__name__ == "War_Greymon":
            print("Funsion evolve to Omegamon")
    return Funsion_Digivice
 
def Evil_Digivice(base):
    def evolve():
        base()
        print("evlove to Skull_Greymon")
    return evolve

@Evil_Digivice
@Digivice   #添加修饰器
# 多个装饰器的话，顺序很重要，先调用的要放在源函数的最近的位置。
def Agumon():
    print("Agumon")

@Digivice
def Greymon():
    print("Greymon")

@Digivice
def Metal_Greymon():
    print("Metal_Greymon")

@Metal_Garurumon
def War_Greymon():
    print("War_Greymon")

#閉包
def out_fun2():
    a = 3
    def in_fun2():
        return a * a
    return in_fun2  # <function out_fun2.<locals>.in_fun2 at 0x000001B80FD1E8C0>

if __name__ == "__main__":
    Agumon()
    Greymon()
    Metal_Greymon()
    War_Greymon()
    d = out_fun2()
    print(d)  #返回結果是一個函數地址

    print(d())   #9

import math
def fun(n):
    for i in range(n):
        yield math.pow(i,2)


