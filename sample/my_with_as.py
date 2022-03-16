#異常處理with as
# with…as
# with类似finally的功能，用于实现程序不管是否异常，都能正常关闭
# with 表达式 as 变量
# 不管是否出现异常，通过with语句执行的，最终在内存中需要清除。
import os
import time


class My_with_as():
    def __init__(self):
        # print(f"pwd=={os.getcwd()}")
        with open("D:\\git\\python\\sample\\my_url.py", "r",
                  encoding='utf-8') as TmpFile:  #open的结果返回给Tmpfile
            for line in TmpFile:   #说明文件类型以能遍历
                print(line)
                time.sleep(0.5)
            TmpFile.close()


if __name__ == '__main__':
    tf = My_with_as()
