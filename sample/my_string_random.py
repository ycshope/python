import random
#从choice,可以从序列中随机选出一个元素
print("从choice,可以从序列中随机选出一个元素")
print(random.choice(range(20)))#返回值是一个数元素,所以可以直接输出

#随机生成一个[0,1)的数
print("-"*50)
print("随机生成一个[0,1)的数")
print(random.random())

#随机生成一个整数
print("-"*50)
print("随机生成一个整数")
print(random.randint(10,20))


#打乱次序
print("-"*50)
My_List = [i for i in range(0,20)]
#print(random.shuffle(range(20)))   返回值是空不是一个list不能这么写,
random.shuffle(My_List)
print(My_List)

#string的in用法,和raw用法(可以把转意字符化成普通字符)
print("string的in用法,和raw用法(可以把转意字符化成普通字符)")
print("-"*50)
str1 = "Hello World!"
strsub = "ello"
print(strsub in str1)
str2 = "kali\n"
print("转义:"+str2)
str3 = r"kali\n"
print("非转义:"+str3)

#string.find和stl中的几乎一样
#找不到会返回-1
print("-"*50)
print("str的方法")
print("find")
str4 = "i love cat,cat love me"
print("str4="+str4)
print("find cat:"+str(str4.find("cat")))
print("find cat from r:%d"%(str4.rfind("cat")))
print("find doge:%d"%(str4.find("doge")))
print("count cat:%d"%(str4.count("cat")))
#在python中,str是常量,所以不能直接修改(str[0]="t",或者直接replace也不行)
#note:删除可以直接dststr=""
print("replace:format:str.replace(srcstr,dststr,start,end)="+str4.replace("cat","doge"))
print("raw str="+str4)
#split的常用方法,取文件后缀
print("split format:str.split('spl',split_count),return type is list")
file = [" kali.c"," kali.cpp"," kali.py"," kali.sh"]
for t_file in file:
    if t_file.split(".")[-1] == "py":
        print(t_file)
        print(t_file.strip())#strip可以把空格给分开

#打印当前文件中的所有.py的文件
print("打印当前文件中的所有.py的文件")
print("-"*50)
import os   #系统包
dir = os.listdir("./") #当前文件的所有文件,返回值是list
for t_file in dir:
    if t_file.split(".")[-1] == "py":
        print(t_file)

'''命令行输入
    import os
    os.(TAB)可以找到所有OS的函数
    常见的有mkdir,fork,详情可以help

    其他方法:
        str.capitalize() 字符串首字母大写
        str.endswith()  是否以某个结尾
        str.startswith()    是否以某个开头
'''

#join连接函数,返回值为str
print("*"*50)
print("join连接函数,返回值为str")
print("x".join("ABC"))
print("x".join("A"))
print("x".join(["aa","bb","cc"]))

#生成一个随机的16位序列号
print("*"*50)
print("生成一个随机的16位序列号")
import string
data = string.digits+string.ascii_letters #生成全部大小写组合
print(data)
print("方法1:")

seq = []    #生成序列
for i in range(6):
    subseq = ""
    for j in range(4):
        subseq += random.choice(data)
    seq.append(subseq)

print("-".join(seq))

#方法2
print("方法2:")
Seq_List = []

def Get_subseq():
    return  "".join(random.sample(data,4)) #random.sample(data,4):随机取出4个不一样的值,生成一个list
    
def Get_seq():
    return "-".join([Get_subseq() for i in range(6)])
    
print(Get_seq())

#格式化输出
name = "kali"
age = 19
str1 = f'i am {name} , {age} years old'
print(str1)
    
#格式化输出
