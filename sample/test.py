import os

if __name__ == "__main__":
    filename = "sample/dict.py"
    file = open(filename, "r",encoding="utf-8")  #file类型
    for i in file:
        print(f"{i}.....")
    file.close()
