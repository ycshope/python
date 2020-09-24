#!/usr/bin/python
#range(num)会返回一个0~num的列表
#循环四次
for i in range(3):
    print(i)
for i in range(1,3):    #也可以指定开头
    print(i)
    
def GetValue1(a):
    a = 100
def GetValue2(l):
    l[0] = 100

if __name__ == "__main__":
    print("值传递和引用传递")
    a=10
    GetValue1(a)
    print(a)    #结果是10,基本所有语言对于基本类型的传递都是值传递(和c类似)
    print("*"*30)
    mylist = [1,2,3]
    GetValue2(mylist) 
    print(mylist)   #结果第一个会被修改,基本所有语言对于复杂类型的传递都是引用传递(c除外)