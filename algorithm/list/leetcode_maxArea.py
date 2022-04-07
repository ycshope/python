# https://leetcode-cn.com/problems/container-with-most-water/
#wp:
# https://leetcode-cn.com/problems/container-with-most-water/solution/container-with-most-water-shuang-zhi-zhen-fa-yi-do/
class Solution:
    #超时
    def maxArea(self, height: list[int]) -> int:
        #分析:短板效应越长不一定是越好,主要看的是两个边界的高度
        #解法1:暴力猜解
        #max(min(a[i]~a[j])*(j-i)),其中0<=i<j<=n-1

        #解法2:优化,双指针
        #问题划分:先计算以a[n]为最右边的最大值,再计算从a[n-1]为右边的最大值....a[1]为右边的最大值
        #ans=max(maxcnt[j]),j from n-1 to 0
        #如果a[j]<MAX(a[j+1]~a[n-1]),那么显然maxcnt[j]<MAX(maxcnt[j+1]),那么就可以不用计算
        #如果a[j]>MAXa(a[j+1]~a[n-1])，那么可以拿进来计算,
        i = 0
        j = len(height) - 1
        maxr = 0
        maxcnt = 0
        #ans=max(maxcnt[j]),j from n-1 to 0
        while j >= 0:
            #如果a[j]<MAX(a[j+1]~a[n-1]),那么显然maxcnt[j]<MAX(maxcnt[j+1]),那么就可以不用计算
            if height[j] > maxr:
                #如果a[j]>MAXa(a[j+1]~a[n-1])，那么可以拿进来计算,
                maxr = height[j]

                #计算maxcnt[j]
                i = 0
                maxl = 0

                while i < j:
                    #如果a[i]<=max(a[0]~a[i-1]),那么直接跳过,否则计算值
                    if height[i] > maxl:
                        maxcnt = max(maxcnt, min(height[i], maxr) * (j - i))
                        maxl = height[i]
                    i += 1
            #右指针向左移动
            j -= 1

        return maxcnt

    #双指针,动态规划
    #简化问题+分析+抽象能力
    def ref_maxArea(self, height: list[int]) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res

if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s=Solution()
    s.maxArea(height)
    pass
