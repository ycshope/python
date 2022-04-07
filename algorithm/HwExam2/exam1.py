# 给定一个只包含大写字母的字符串s，字符消除过程是如下进行的：
# 1)如果s包含长度为2的由相同字9母组成的子串，那么这些子串会被消除，余下的子串拼成新的字符串。例如”ABCCBCCCAA”中”CC”,”CC”和”AA”会被同时消除，余下”AB”, “C”和”B”拼成新的字符串”ABBC”。
# 2)上述消除会反复一轮一轮进行，直到新的字符串不包含相邻的相同字符为止。
# 例如”ABCCBCCCAA”经过一轮消除得到”ABBC”，再经过一轮消除得到”AC”
# 输入描述:
# 对于每个测试数据输入包括一行, 由大写字母组成的字符串s，长度不超过100.
# 输出描述:
# 对于每组测试数据, 若最后可以把整个字符串全部消除, 就输出 Yes, 否则输出 No.
# 示例:

# 输入：ABCCBA
# 输出：Yes

# 输入：ABCCCCCBBBBB
# 输出：No

#subst:length=2 and

# ABCCBA ->CC
# ABBA ->BB
# AA ->AA

#思路:每次消除string里面连续的两个字符,直到没有办法消除字母位置

#Q1:如何找到两个连续相同的字母?
#S1:直接判断i+1即可(0=<i<n-2)


def isduple(s: str, index: int):
    length = len(s)
    #后面没有元素
    if index >= length - 1:
        return False
    if s[index] == s[index + 1]:
        return True
    return False


#需要注意,可能不止遍历一次
#消除重复
def erase(s: str) -> str:
    ans = ""

    length = len(s)
    # print(length)
    #边界条件len=0,1
    if length < 2:
        return s

    #消除重复
    #最后一个下标是i-2
    # (0=<i<n-2)
    i = 0
    while i < length:
        # print(i)
        if not isduple(s, i):
            #没有重复,那么加入ans
            ans += s[i]
            i += 1
        else:
            #如果有重复,那么消除2个
            i += 2

    return ans


# 消除多次的最终结果
def solution(s: str):
    #循环消除
    #那么什么情况下能直到无法再消除？
    #消除前后完全相同
    curS = s
    while True:
        afterS = erase(curS)

        #消除后为"",返回True
        if afterS == "":
            return True
        #无法再消除,直接返回False
        if afterS == curS:
            return False
        else:
            curS = afterS
            print(f"curS={curS},afterS={afterS}")
            # ABCCCCCBBBBB ->ABCB


if __name__ == "__main__":
    s = "ABCCBA"
    s = "ABCCCCCBBBBB"
    res = solution(s)
    print(res)
