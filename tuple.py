#元组,和list的主要区别是元素内容只是可读,可以通过help(tuple)来查看函数

def GetValue():
    usr = "kali"
    passwd = "1"
    uuid = 8040
    return (usr,passwd,uuid) #返回一个元组
    
#元组和list的转化
def TypeExchange(t):
    return(list(t)) #返回结果是一个list
    t_type = str(type(t))
    #if type(t) == "<class 'list'>":    这样写存在问题,因为type不是一个类型和"<class 'list'>"不是一个类型
    if t_type == "<class 'list'>":
        print("1")
        return list(t)
    #elif type(t) is "tuple":
    elif t_type == "<class 'tuple'>":
        print("2")
        return tuple(t)
    else:
        print("3")
        pass
    
if __name__ == "__main__":
    #元组支持多赋值
    usr , passwd , uuid = GetValue()
    print("usr = %s, passwd = %s, uuid = %s"%(usr,passwd,uuid))
    #元组的定义
    My_tuple = (1,2,3)
    print(My_tuple)
    print("after type change:")
    My_list = TypeExchange(My_tuple)
    print(My_list)
    print(type(list))
    