#except用与try的错误处理,使得程序不继续往后执行
try:
    '''
    输如非int时会提示:
    ValueError: invalid literal for int() with base 10: 'asd'           
    '''
    age = int(input("age: "))
    income = 10000
    risk = income / age #age = 0时报错：    ZeroDivisionError: division by zero
    print(f"{age}") 
except ValueError:     #错误的信息必须对应,age为0时,无法调用本条异常处理                                                                 
    print("invalue type of age")
except ZeroDivisionError:   #解决错误0的问题
    print("can not division by zero")