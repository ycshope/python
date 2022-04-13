class Solution():
    def getMaxReverseString(self, s: str):
        #Q:找出最长回文串
        #找到回文串相对而言比较简单,但是如何找到最长的子串是回文串是关键
        #方法1:枚举
        #以i为开头去找回文串,其中最大的回文串即为最大的
        #时间复杂度:O(n^3)
        #优化:贪心
        #回文串从大到小开始尝试,遇到大的就直接结束;第一个必然为最长的回文串;最糟糕情况为O(n^3),
        length = len(s)
        #边界条件为1,直接返回
        if length < 1 or length == 1:
            return s
        #判断从start开始的resplen个字符是否是回文
        def isReverseString(s: str, start: int, rsplen: int):
            length = len(str)

            #回文
            if start + rsplen > length - 1:
                return False

            #双指针判断回文
            

        #以i为开头去找回文串,其中最大的回文串即为最大的
        for i in range(0, length):
            #设置回文串长度,逐渐减少
            rsplen = length
            while rsplen:
                #如果对应的字串是回文,返回结果
                if isReverseString(s=s, start=i, rsplen=rsplen):
                    return s[i:i + rsplen]
                rsplen -= 1

        #其他情况,返回任意一个字符
        return s[0]


if __name__ == "__main__":
    String = "abacd"

    #其中包含回文串aba 
    s = Solution()
    print(s.getMaxReverseString(String))
