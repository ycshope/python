#zip主要是生成一個元組列表
a1 = ['a', 'b', 'c']
a2 = [1, 2, 3]

t_zip = zip(a1, a2)
print(t_zip)  #<zip object at 0x000001E33D490600> 返回值是内存地址
b=list(t_zip)
print(b)  #[('a', 1), ('b', 2), ('c', 3)]
