#python要么以空格作为函数,但需要带返回
def fun1():
    #要么带pass,要么带返回值(返回值可以为空).无论是pass还是空返回值,结果都是none
    #pass
    return

if __name__ == "__main__":
    ref=fun1()
    print(ref)