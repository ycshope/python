a=set("abcde")
print(a) #{'e', 'a', 'd', 'b', 'c'}  顺序似乎是不一样,并且類型也被轉換額
b=set([1,"nihao",True])  
print(b)  #{1, 'nihao'} 集合的類型只能是list or string
b.update("adc")
print(b) #{1, 'a', 'nihao', 'c', 'd'}

c=frozenset([1,3,4])    #不可變集合
