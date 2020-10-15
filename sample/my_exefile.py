#二进制文件的操作
import struct   #二进制的头文件

def My_Write():
    file = open("./kali","w")
    #写入二进制文件
    '''
        pack表示打包成二进制,
        第一个参数是输入的数据类型,
        4s标识第一个miku是个4位的str
        i表示第二个是6是个int
        d表示第三个是3.14是个double
        b"miku"格式化字符串的值在Python的类型是bytes类型。所以我们在bytes类型前面加上一个b就可以解决这个问题了
       注意struct.pack的返回值是一个bytes,所以要转换成str
    '''
    data = struct.pack("4sid",b"miku",6,314)
    print(type(data))
    file.write(str(data))
    file.close()

def My_Read():
    file = open("./kali","r")
    #读取二进制文件
    '''
        unpack的返回值是一个元组
        unpack后的第一个参数和输入的含义一样,
        第二个参数标识要处理的二进制,注意类型必须是bytes
    '''
    data = file.read()
    print(type(data))
    (name,age,identy) = struct.unpack("4sid",bytes(data))
    printf("name : "+name)
    printf("age : "+age)
    printf("id : "+identy)
    file.close()

if __name__ == "__main__":
    My_Write()
    My_Read()
