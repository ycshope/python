#https://leetcode-cn.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #思路:哈希
        # 如果发现taget-a[i]的标记位存在,那么就是直接返回i和hash[taget-a[i]]
        length = len(nums)

        Hash = {}
        #1.查找标记
        for i in range(0, length):
            #2.如果标记存在则返回
            if (v := Hash.get(target - nums[i])) != None:
                return [v, i]
            #3.进行标记
            Hash[nums[i]] = i


if __name__ == "__main__":
    nums, target = [3,3], 6
    s = Solution()
    print(s.twoSum(nums=nums, target=target))
