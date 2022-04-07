# 因数分解后，找到两个素数3和5，使得3*5=15，按从小到大排列后，输出3 5
# 分两个问题:1.计算所有小于num的因素ans[] 2.查看是否存在这样的ans[i]*ans[j]=num
# 分析:如果存在这样的因素那么他们的最大值x必然满足x*x<=num,也就是找到从1~根号x的两个因素

#判断x是否是因素
from tokenize import maybe


def isWantedType(x):

    if x == 1 or x == 2 or x == 0:
        return True

    for i in range(2, x):
        if i * i > x:
            break
        if x % i == 0:
            return False

    return True


if __name__ == "__main__":
    WantedType = []
    for i in range(3, 2147483648):
        if i * i > 2147483648:
            break
        if isWantedType(i):
            WantedType.append(i)
    # print(WantedType)
    while True:
        try:
            num = int(input())
            if num == 1 or num == 2 or num == 0:
                print("-1 -1")
            else:
                for i in WantedType:
                    if i * i > num:
                        print("-1 -1")
                        break

                    if num % i != 0:
                        continue
                    else:
                        maybe = int(num / i)
                        if maybe == i:
                            continue
                        if maybe in WantedType:
                            print(f"{i} {maybe}")
                            break
                    # 分两个问题:1.计算所有小于num的因素ans[] 2.查看是否存在这样的ans[i]*ans[j]=num

        except:
            break
