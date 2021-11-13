#父类
class Father:
    def __init__(self,name):
        print("Father __init__")
        self.__name = name
        self.gun = True
    def Show(self):
        print("Father Show")
        print(self.__name)
        print(self.gun)
    def __del__(self):
        print("Father __del__")
    @property
    #主要用來獲取私有變量,Q:普通函數不是也可以嗎？
    def ChName(self):
        return self.__name
    
    @ChName.setter
    #property+setter可以實現函數的讀寫
    def ChName(self, name):
        self.__name=name
#子类
class Children(Father):
    def __init__(self,name,age):
        '''
            c++子类的构造默认会调用父类的
            python需要手动调用父类的构造函数
        '''
        print("Children __init__")
        Father.__init__(self,name)  #注意调用父函数时也需要self参数
        self.age = age
    def Show(self):
        #重写
        print("Children Show")
        #print(self.__name) 无法调用父成员的私有属性
        Father.Show(self) #只能通过调用父成员的函数来查看私有
        print(self.age)
        print(self.gun)   #繼承父屬性
    def __del__(self):
        print("Children __del__")

#python不需要多态 
def CallShow(doge):
    doge.Show()

if __name__ == "__main__":
    #继承
    print("继承")
    F1 = Father("OS")
    F1.Show()
    
    C1= Children("Linux",40)
    C1.Show()
    
    #多态
    print("*"*50)
    print("多态")
    CallShow(F1)
    CallShow(C1)

    #裝飾器
    # F1.ChName("hack!!")  ??
