#https://leetcode-cn.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        #思路:字典,如果出现重复那么就结束
        if len(nums)<2:
            return False
        dict = {}
        for k in nums:
            if dict.get(str(k)):
                return True
            dict[str(k)] = 1
        return False
    #最优解
    def ref_containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)


if __name__ == "__main__":
    # nums=[1, 2, 3, 1]
    # nums = [1, 2, 3, 4]
    nums = []
    s = Solution()
    print(s.containsDuplicate(nums=nums))
