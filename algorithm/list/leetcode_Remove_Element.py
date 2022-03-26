# ref:https://leetcode-cn.com/problems/remove-element/
class Solution:
    def removeElement(self, nums, val: int) -> int:
        #解法1.速度慢,c++则可以通过下标循环移动来解决实现优化
        while val in nums:
            nums.remove(val)
        #print(nums)
        return len(nums)

    #优化解法,遇到非指定的元素,才生成.指定的元素不加入
    def removeElement_improve(self, nums: list[int], val: int) -> int:
        a = 0
        b = 0

        while a < len(nums):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1
        return b


if __name__ == "__main__":
    nums_list = [[3, 2, 2, 3], [0, 1, 2, 2, 3, 0, 4, 2], []]
    s = Solution()
    for nums in nums_list:
        print(nums)
        val = input("输入删除的值:")
        print(s.removeElement(nums, int(val)))
