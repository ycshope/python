class Student:
    #学生类
    School = "Linux"    #静态成员变量,python叫类的属性
    
    @classmethod    #声明静态成员函数,这个函数没有self
    def GetSchool(cls):
        print("GetSchool")
        #return self.School
        return cls.School
    
    def Show(self):
        #普通函数,在python中叫对象的方法
        print("__show__")
        print(self.name)
        print(self.age)
        print(self.__passwd)
        print(Student.School)   #调用静态成员 变量
    
    def __init__(self,name,age):
        #构造函数,self相当于c++中的this,python中self必须是显式,否则无法调用
        print("__init__")
        self.name = name    #成员对象不需要声明,在python中叫对象的属性
        self.age = age
        self.__passwd = "100"   #对象的私有属性
    
    def __ShowPassWd(self):  #对象的私有函数,无法访问
        print(self.__passwd)
    
    def Root(self):  #通过对象的函数访问对象的私有函数
        self.__ShowPassWd()
'''
    @classmethod        也没办法通过类的函数访问对象的私有函数
    def ROOT(cls):
        return cls.__ShowPassWd()   
'''        
        
    def __del__(self):
        #析构函数,但python不需要考虑内存释放问题
        print("__del__")

if __name__ == "__main__":
    #对象的属性和对象的函数
    print("*"*60)
    print("类的变量和类的成员函数")
    S1 = Student("kali",20)
    S1.Show()
    S2 = Student("Centos",18)
    S2.Show()
    #类的属性和类的函数
    print("*"*60)
    print("类的变量和类的成员函数")
    Student.School = "Windows"  
    print(Student.GetSchool())
    #del S1 默认会调用析构,不需要释放
    #无法修改对象的私有属性
    print("*"*60)
    print("无法修改私有成员")
    #print(S1.__passwd) 访问会自己报错
    S1.__passwd = "10"
    S1.Show()
    #无法访问对象的私有函数
    print("*"*60)
    print("无法访问对象的私有函数")
    S1.Root()
    #Student.ROOT()