# 9=9  <---1个数,显然自身是最优解
# 9=4+5 <---2个数:则有x+x+1=T  ->求出x即可
# 9=2+3+4  <---3个数： x+x+1+x+2=T ->求出X即可
# x的取值: 1~T/2
# 思路: 先找两个数字累加=T,再找3个数累加=T,找到x即可....
# 滑动窗口:1 2 3 4 5 6 7 8 9
# Result:3


#求连续num个数字的和等于T
def qureyX(T: int, num: int):
    # x+0 ,....x+num-1=num*x+0~num-1=num*x+sum(range(0,num-1))=num*x+S=T  -> T-S=num*x -> x=(T-S)/num
    #这里num越大x越小
    S = sum(range(0, num))

    #提前判空条件,已经不可能有解大于num个数
    if T - S < 0:
        return -1

    #求出x
    x = (T - S) / num

    #x必须>=1,且为正数
    if x >= 1 and x % 1 == 0:
        return int(x)
    else:
        #x不为int时不算
        return 0


if __name__ == "__main__":
    while True:
        try:
            # T = 10
            ans_list = []
            T = int(input())
            if T == 1:
                print("1=1")
                print(f"Result:1")
                continue
            #找出对应的x
            for i in range(1, T):
                x = qureyX(T, i)
                if x == -1:
                    break
                elif x == 0:
                    continue
                else:
                    ans_list.append([x, i])
                    # print(f"x,i={x,i}")
            base_form = f"{T}="
            # 输出对应的x
            for ans in ans_list:
                cur_form = base_form
                for num in range(0, ans[1]):
                    if num != 0:
                        cur_form = cur_form + "+"
                    cur_form = cur_form + f"{ans[0] + num}"
                print(f"{cur_form}")
            print(f"Result:{len(ans_list)}")
            #暂时先不考虑边界条件
        except:
            break
