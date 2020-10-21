#!/usr/bin/python
#运算表达式
#不支持++,但可以+= 
a = 5.0
b = 2.5

print("运算表达式")
print(a + b)
print(a - b)
print(a - b)
print(a ** b)  #次幂
print(a / b)    #浮点数会保留小数
print(a // b)   #a除b向下取整
print(a % b)

#逻辑表达式

print("逻辑表达式")
c = True
d = False
print(not c)
print(c and d)
print(c or d)
print(c is d) #a和b是同一个对象(id相同)
print(c is not d) #a和b不是同一个对象

#关系表达式

a = 3
b = 4
print("关系表达式")
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#位运算

print("位运算")
a = 3
b = 4
print(~a)
print(a << b)
print(a >> b)
print(a & b) 
print(a | b)
print(a ^ b)    #异或

#分支语句
    
if a > b:
    print("a > b")
elif a == b:
    print("a == b")
else:
    print("a < b")

#循环语句
'''
passwd = 1
while passwd == 1 :  #和c一样,无限循环
    passwd = input("输入0结束循环")
    print("你输入了:%d",passwd)
    passwd = int(passwd)
    
print("结束循环")
'''
#while和else搭配使用
turn = 3
passwd = 9 
while turn :
    guess_passwd = int(input("请输入密码: "))
    if guess_passwd == passwd:
        print("密码输入成功")
        break;
    turn -= 1
else:
    print("密码输入错误超过3次")#break结束的不会走这
print("游戏结束")

#for语句
mylist = [1,"python",True,4.4,[1,2,4],["a","b"]] #list的元素类型没有限制
print(type(mylist))
print(mylist)
for var in mylist:
    print(var)
    print(type(var))
    if type(var) is list:   #这里的is和==是等价
        print("i am list")

#查看list的方法用help(list)
print("list的方法")

#list的方法
mylist = []
#append加入元素,也可以加入数组作为元素
mylist.append(10)
mylist.append(13)
mylist.append(15)
mylist.append(14)
mylist.append(19)
mylist.append(14)
print(mylist)
#len是类似sizeof的函数或者是操作符
print(len(mylist))
#count是计算list中某个元素出现的次数
print(mylist.count(14))
#reverse翻转
print(mylist.reverse())#返回值为None
print(mylist)
#sort排序,没返回值
print(mylist.sort())#返回值为None
print(mylist)
#in关键字
print(14 in mylist)
#remove只能移除需要从左往右的第一个参数
mylist.remove(14)
print(mylist)
#另外一种常见的遍历方法
for _ in mylist:
    print(_)
#取元素
print(mylist[0])    #和c++一样
print(mylist[-1])   #从右往左数第一个
print(mylist[:])    #从0开始到结束
print(mylist[2:])   #从2开始到结束
print(mylist[1:3])   #从2开始到第3个
#连个list合并
mylist1 = [True,"python"]
mylist2 = mylist + mylist1
print(mylist2) 