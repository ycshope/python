'''
case1:正好为三个数时唯一解
[-1,2,1,-4]
case2:大于三个数时呢?
threeSumClosest[i]:为a[0]~a[i]的最优解,其中组成的元素为:num[0]~num[3]
threeSumClosest[i+1]=Closest(threeSumClosest[i],a[i+1]+threeSumClosest[i]-num[x])
time(On)
'''
# https://leetcode-cn.com/problems/3sum-closest/

from dataclasses import replace
from pickle import TRUE

#核心:问题拆分,将最接近的threeSumClosest(taget)个数变为twoSumClosest(taget-a[i])
class Solution:
    def __init__(self, nums, target) -> None:
        self.nums = nums
        self.target = target
        self.ans = self.threeSumClosest(nums=self.nums, target=self.target)

    def __str__(self) -> str:
        return str(self.ans)

    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = 10**7

        # 根据差值的绝对值来更新答案
        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur

        # 枚举 a
        for i in range(n):
            # 保证和上一次枚举的元素不相等
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 使用双指针枚举 b 和 c
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                # 如果和为 target 直接返回答案
                if s == target:
                    return target
                update(s)
                if s > target:
                    # 如果和大于 target，移动 c 对应的指针
                    k0 = k - 1
                    # 移动到下一个不相等的元素
                    while j < k0 and nums[k0] == nums[k]:
                        k0 -= 1
                    k = k0
                else:
                    # 如果和小于 target，移动 b 对应的指针
                    j0 = j + 1
                    # 移动到下一个不相等的元素
                    while j0 < k and nums[j0] == nums[j]:
                        j0 += 1
                    j = j0

        return best

    #解法错误--贪心算法
    def threeSumClosest2(self, nums: list[int], target: int) -> int:

        lens = len(nums)
        #case1:正好为三个数时唯一解
        if lens == 3:
            return sum(nums)
        # 贪心算法:
        # threeSumClosest[i]:为arr[0]~arr[i]的最优解,其中组成的元素为: Closestnum[0~2]
        # threeSumClosest[i+1]=Closest(threeSumClosest[i],a[i+1]+threeSumClosest[i]-num[x])

        # 本体并不是贪心解法
        # 并不是单纯的 Closest(threeSumClosest[i],a[i+1]+threeSumClosest[i]-num[x])
        # 没有考虑到 threeSumClosest[i]和threeSumClosest[i-2]的关系 有可能存在
        # threeSumClosest[i-2]+a[i+1] > threeSumClosest[i]+ a[i+1]
        # threeSumClosest[i-2]+a[i] < threeSumClosest[i-1]+a[i]
        Closestnum = [nums[0], nums[1], nums[2]]
        Closestsum = sum(Closestnum)
        # print(f"Closestnum={Closestnum},Closestsum={Closestsum}")

        #case2:贪心算法,从start=3开始
        start = 3
        i = start

        while i < lens:

            print(f"i={i}")
            CurClosestsum = Closestsum
            replacedindex = -1
            for index, num in enumerate(Closestnum):
                cursum = Closestsum - num + nums[i]
                # print(f"i={i},index={index},cursum={cursum}")
                # threeSumClosest[i+1]=Closest(threeSumClosest[i],a[i+1]+threeSumClosest[i]-num[x])
                if abs(target - cursum) < abs(target - CurClosestsum):
                    replacedindex = index
                    CurClosestsum = cursum

            Closestsum = CurClosestsum
            if replacedindex != -1:
                print(f"Closestnum from {Closestnum} to ")
                Closestnum[replacedindex] = nums[i]
                print(f"{Closestnum}")

            if Closestsum == target:
                return target

            i += 1

        return Closestsum

if __name__ == "__main__":
    # nums = [-1, 2, 0, -4, 4, 2]
    # target = 1

    nums = [0, 0, 0]
    target = 1

    nums = [1, 2, 4, 8, 16, 32, 64, 128]
    target = 82

    ans = Solution(nums=nums, target=target)
    print(ans)
