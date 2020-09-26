import random
#从choice,可以从序列中随机选出一个元素
print("从choice,可以从序列中随机选出一个元素")
print(random.choice(range(20)))

#随机生成一个[0,1)的数
print("-"*50)
print("随机生成一个[0,1)的数")
print(random())

#打乱次序
print("-"*50)
print(random.shuffle(range(20)))