#except用与try的错误处理,使得程序不继续往后执行
# 异常定义
# 程序运行会出现各种各样的问题，例如语法编写错误或文件读写错误等，出现各种各样的bug。
# 默认情况下，程序会马上停止执行，并根据错误情况，反馈异常情况（显示栈追踪），方便程序员进行排错和调试哪个位置出了问题？出现的是哪种类型的错误？
# 本质上讲，异常是一种类，并且有很多子类，基类为BaseException。
# 异常捕获

try:
    '''
    输如非int时会提示:
    ValueError: invalid literal for int() with base 10: 'asd'           
    '''
    age = int(input("age: "))
    income = 10000
    risk = income / age  #age = 0时报错：    ZeroDivisionError: division by zero
    print(f"{age}")
# except ValueError:     #错误的信息必须对应,age为0时,无法调用本条异常处理
#     print("invalue type of age")
# except ZeroDivisionError:   #解决错误0的问题
#     print("can not division by zero")
# except:   #所有異常不需要用括號
#     print("input error! your age must be a number!")
except (ValueError, ZeroDivisionError):  #多個輸出
    print("input error! can not division by zero or invalue type of age")
else:  #除了上面兩個的異常,時候顯示
    print("執行成功!")
finally: #不管try的結果是啥最後都可能會執行
    print("輸入結束...")
