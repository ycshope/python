# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/


class Solution:
    def findMin(self, nums: list[int]) -> int:
        #case1:最简单的方法,利用python返回
        # return min(nums)

        #case2:二分,
        # 每次寻找一个非递增的区间(a[low]>a[high]),将它拆分为一个单调递增,另一个非但递增的区域,直到没办法划分为止
        def findmin(nums: list[int], low: int, high: int) -> int:
            #边界条件:两边指针合拢
            if low >= high:
                return nums[high]

            #边界条件:无法再找到无序子串
            if nums[low] < nums[high]:
                return nums[low]

            mid = (low + high) // 2

            #前半段是顺序,那么结果在后半段; 当结果只有两个元素时会出现=
            if nums[low] <= nums[mid]:
                return findmin(nums=nums, low=mid + 1, high=high)
            #否则结果在前半段
            else:
                return findmin(nums=nums, low=low + 1, high=mid)

        length = len(nums)
        return findmin(nums=nums, low=0, high=length - 1)

    def findMin_ref(self, nums: list[int]) -> int:    
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot 
            else:
                low = pivot + 1
        return nums[low]

if __name__ == "__main__":
    # nums = [3, 4, 5, 1, 2]
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # nums = [11, 13, 15, 17]
    # nums = [4, 5, 6, 7, 8, 9, 10, 0]
    nums = [4]
    ans = Solution()
    print(ans.findMin(nums))
