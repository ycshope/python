#标准输出,类似c++
print("Is %s %d"%("Dec",23))
#连接字符串时必须是类型相同
#name=99
name="louis"
print("i am"+name)
#标准输入
myinput = input("输入一个数字")
print(myinput)
#无论什么类型都会转换为str
print(type(myinput))
#强制转换类型,类型不符合会报错
myinput=int(myinput)
print(type(myinput))
