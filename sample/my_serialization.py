# 为了将我们所操作的内容永久存储（保存到硬盘），需要引入"序列化"（顺序化），即
# pickling/serialization。
# 序列化将复杂数据结构（对象）转换为一个二进制数据集合（数据流），这样就可以把数据永久存储或通过网络发送，然后再重新把数据流恢复原来的对象内容。
# 变量/对象等从内存中变成可存储或传输的过程称之为序列化。
# Pickle.load需要以二進制讀寫
# Josn.load以文本讀寫即可
import pickle

Str = "HelloWorld"
#serialization
Data = pickle.dumps(Str)
print(Data
      )  #b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00\x8c\nHelloWorld\x94.'

#unserialization
print(pickle.loads(Data))

#serialization into file
TmpFile = open("./SerializationFile", "wb+")  #序列換文件是二進制,需要有b來打開,+表示文件指針在最前面
pickle.dump(Str,TmpFile)
TmpFile.close()

#unserialization from file
TmpFile = open("./SerializationFile", "rb+") 
print(pickle.load(TmpFile))
TmpFile.close()
