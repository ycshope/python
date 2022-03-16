import os


class My_File:
    def __init__(self, filename):
        file = open(filename, "r")
        containList = file.readlines()  #返回值是一个list,每个元素包含一行
        print(str(containList))
        file.close()


if __name__ == "__main__":
    # filename = "passwordlist.txt"
    # fp = My_File(filename=filename)
    a = "pass"
    b = ["pass", "you"]
    print(a == b)  #False
    print(a in b)  #True
