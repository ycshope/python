#operate操作
class Student():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    #operate<<
    def __str__(self):
        #print("name = %s,age = %d"%(self.__name,self.__age))注意是返回才能接收
        return ("name = %s,age = %d" % (self.__name, self.__age))

    #operate +
    def __add__(self, other):
        return self.__age + other.__age


if __name__ == "__main__":
    a = Student("kali", 19)
    print(a)  #定义了__str__后才可以使用
    b = Student("miku", 16)
    print(a + b)  #定义的__add__后才可以使用
    print("*" * 60)
    print(dir(operation))
