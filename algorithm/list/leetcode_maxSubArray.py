#https://leetcode-cn.com/problems/maximum-subarray/
class Solution:
    #1.最简化解法:
    #求出所有的sum[i][j]即可,时间复杂度:o(n^2)
    #i从左往右,j也从左往右
    def maxSubArray(self, nums: list[int]) -> int:
        #sum[i][j]表示从a[i]+...+a[j]的合
        #结果为max(sum[i][j]),0<=i<=j<=n-1
        lenth = len(nums)
        ans = -0x3f3f3f3f
        #计算以a[i]开始的和
        for i in range(lenth):
            sum = 0
            # 计算sum[i][j]
            for j in range(i, lenth):
                sum += nums[j]
                ans = max(ans, sum)

        return ans

    #2.优化
    #2.1问题分解:
    # dp[i]为{以i为结尾的最大和的连续子数组},显然ans=max{dp[i]}(0<=j<=n-1)

    #2.2每个问题该如何求解?
    #由于必须以a[i]结尾,所以只需要找到开头即可,假设为a[x](0=<x<=i)
    #结果为dp[i]=max(sum[x][i])

    #2.3子问题和子问题之间是否有什么联系?
    #dp[i]和dp[i+1]的关系?
    #dp[i+1]=max(dp[i-1]+a[i],a[i]) 

    def ref_maxSubArray(self, nums: list[int]) -> int:
        lenth = len(nums)
        ans = -0x3f3f3f3f
        #计算以a[i]开始的和sum[i][x]
        for i in range(lenth):
            sum = 0
            # 计算sum[i][j],求出max(sum[i][j])
            for j in range(i, lenth):
                sum += nums[j]
                ans = max(ans, sum)

        return ans


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [-2, 1, -3, 4]
    s = Solution()
    print(s.maxSubArray(nums=nums))
