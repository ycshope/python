import os


class My_File:
    def __init__(self):
        while True:
            print('''
                Hello,i am file_assistant,u can ether a word as follow,i can do that:
                mkdir 
                write
                read
                cp
                exit
            ''')
            order = input()
            if order == "mkdir":
                self.mkdir()    #注意调用本函数时需要调用指米国对象
            elif order == "write":
                self.write()
            elif order == "read":
                self.read()
            elif order == "cp":
                self.cp()
            elif order == "exit":
                break
        
    def mkdir(self): #创建目录
        dir = input("input a dir:")
        os.mkdir(dir)
        
    def write(self): #写文件
        filename = input("input a filename:")
        file = open(filename,"w")   #file类型
        contain = input("input a contain:")
        file.write(contain)   #默認不會加換行字符,需要自行添加
        file.flush()#清空缓存
        file.close()   #文件需要關閉后才能讀取到剛寫入的内容
        
    def read(self): #读文件
        filename = input("input a filename:")
        file = open(filename,"r")   #file类型
        contain = file.readlines()  #返回值是一个list,每个元素包含一行
        print(str(contain))
        file.close()
     
    def cp(self): #拷贝文件
        src_filename = input("input a src filename:")
        dst_filename = input("input a dst filename:")
        src_file = open(src_filename,"r")
        dst_file = open(dst_filename,"w")
        while True:
            buf = src_file.readline()
            if buf == "": #读到结束
                break
            dst_file.write(buf)
        src_file.close()
        dst_file.close()
            

if __name__ == "__main__":
    fp = My_File()
    