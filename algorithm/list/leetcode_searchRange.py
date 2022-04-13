#https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        #思路:先二分后顺序

        def BiSearch(nums: list[int], target: int, start: int, end: int):
            #边界
            if start > end or start < 0:
                return [-1, -1]
            # mid = int((start + end) / 2)
            #整除
            mid = (start + end) // 2
            num = nums[mid]

            #如果找到了那么就结束
            if num == target:
                #往前找相同的
                sindex, eindex = mid - 1, mid + 1
                #结果为(sindex,eindex)

                while sindex >= 0 and nums[sindex] == target:
                    sindex -= 1

                #往后找到相同的
                while eindex < len(nums) and nums[eindex] == target:
                    eindex += 1

                return [sindex + 1, eindex - 1]

            #nums[mid]<target,那么结果在(mid,end]
            elif num < target:
                return BiSearch(nums=nums,
                                target=target,
                                start=mid + 1,
                                end=end)
            else:
                #nums[mid]>target,那么结果在[start,mid)
                return BiSearch(nums=nums,
                                target=target,
                                start=start,
                                end=mid - 1)

        #边界条件长度为0直接返回
        if len(nums) == 0:
            return [-1, -1]

        return BiSearch(nums=nums, target=target, start=0, end=len(nums) - 1)

    def ref_searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def left_func(nums, target):
            n = len(nums) - 1
            left = 0
            right = n
            while (left <= right):
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                if nums[mid] < target:
                    left = mid + 1
            return left

        a = left_func(nums, target)
        b = left_func(nums, target + 1)
        if a == len(nums) or nums[a] != target:
            return [-1, -1]
        else:
            return [a, b - 1]

    def searchRange2(self, nums: list[int], target: int) -> list[int]:
        #思路:找到最小的target的下标

        def BiSearch(nums: list[int], target: int, start: int, end: int):
            #边界
            if start > end:
                return start
            if start < 0:
                return -1

            mid = (start + end) // 2
            num = nums[mid]

            #nums[mid]<target,那么结果在(mid,end]
            if num < target:
                return BiSearch(nums=nums,
                                target=target,
                                start=mid + 1,
                                end=end)
            else:
                #nums[mid]>=target,那么结果在[start,mid)
                return BiSearch(nums=nums, target=target, start=start, end=mid-1)

        #边界条件长度为0直接返回

        return BiSearch(nums=nums, target=target, start=0, end=len(nums) - 1)


if __name__ == "__main__":
    nums, target = [5, 7, 7, 7, 8, 10], 8
    # nums, target = [5, 7, 7, 8, 8, 10], 6
    # nums, target = [], 0
    s = Solution()
    print(s.searchRange2(nums=nums, target=target))
