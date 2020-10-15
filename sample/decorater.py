'''
装饰器的概念:
可以同一个类给另一个类添加功能
称第一个类为一个装饰器
本质和C++的多态没什么区别
原则不修改原来的类的代码
'''
#装饰器,把需要装饰的函数作为参数
def Digivice(base):
    def evolve():   #闭包
        base()      #继承原函数
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

if __name__ == "__main__":
    Agumon()
    Greymon()
    Metal_Greymon()
    War_Greymon()
    