'''
闭包的特点
1.有内部函数
2.内部函数引用外部函数的变量，并传参给内部函数
3.外部函数返回内部函数(不是返回函数的返回值)
4.主要是写一些简单的对象,但会占用内存
'''

def out_fun():

    #count = 1
    count = [1]
    #内部函数
    def in_fun():
    #   count += 1  这个count和上面的作用域不一样
        count[0] += 1
        print(count[0])
        
    return in_fun

if __name__ == "__main__":

    c1 = out_fun()  #返回值是function
    print(type(c1))
    for i in range(4):
        c1()
    
    c2 = out_fun()
    #和上面引用的对象不一样
    for i in range(5):
        c2()