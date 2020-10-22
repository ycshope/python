#import function
from function import function1  #指定module的某个函数

def function_2():
    print("调用import的脚本的函数function1")
    #function.function1("hello",1)  #引入整个模块,那么需要指定 module.function
    function1("hello",1)    #引入单个   不需要指定module

#如果引用的别的文件有指令在函数外,那么会先执行别的代码,后执行函数
function_2()
print("import的模块名为"+__name__)

'''
python多文件编程会分主次模块,
直接执行的是主模块,模块名为__main__,
import的模块为次模块,模块名既为本身
'''