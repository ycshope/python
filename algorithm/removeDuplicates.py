'''
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

 

示例 1:

给定数组 nums = [1,1,2], 

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。


解题思路:
1.问题分析:
设：unit[i]表示长度为i的数组的不含重复元素的个数的长度
则：
i==0,unit[i]=1
i>0:
    if num[i] in num[0:i]:
        dupnum +=1
    else:
        unit[i] = unit[i-1] + 1


解法有问题:没有把重复元素移除
2.移除重复元素的方法:
如果元素重复,那么把重复和最后一个数组交换丢到最后
算法设计:

i = 0
while i < nums_length:
    #如果有重复元素
    #最终的数组长度-1
    #把重复的元素换到最后一位
    if num[i] in num[:i]:
        dupnum +=1
        nums_length -= 1
        swap(nums[i],nums[nums_length])
    #没有重复元素
    #元素后移
    else:
        i++
'''
class Solution:
    def removeDuplicates_1(self, nums):
        length = len(nums)
        unit_num = 0
        if length == 0 or length == 1:
            return length
        for i,elem in enumerate(nums):
            # print(f"num[:{i}]={nums[:i]}") # 输出nums[0]~nums[i-1]
            if elem not in nums[:i]:
                unit_num += 1
            # print(f"unit_num={unit_num}")
        return unit_num

    def removeDuplicates_2(self, nums):
        i,nums_length = 0,len(nums)
        if nums_length <= 1:
            return nums_length
        while i < nums_length:
            #如果有重复元素
            if nums[i] in nums[:i]:
                #最终的数组长度-1
                nums_length -= 1
                #把重复的元素换到最后一位
                nums[i],nums[nums_length] = nums[nums_length],nums[i]
            #没有重复元素
            else:
                #元素后移
                i += 1
            # print(f"nums[:{i}]={nums[:i]},nums[{i}]={nums[i]},nums_length={nums_length},nums={nums}")
        return nums_length

    def removeDuplicates(self, nums):
        length = len(nums)
        if length == 0 or length == 1:
            return length
        i = 0
        while i < length:
            # print(f"num[:{i}]={nums[:i]}") # 输出nums[0]~nums[i-1]
            if nums[i] in nums[:i]:
                nums.pop(i)
                length -= 1
            else:
                i += 1
        return length

if __name__ == "__main__":
    sample_list = [[],[1],[1,1,2],[0,0,1,1,1,2,2,3,3,4],[1,2,3,4],[1,1,1,1]]
    s = Solution()
    for sample in sample_list:
        print(f"sample={sample}")
        print(s.removeDuplicates(nums=sample))
        print(f"after_sample={sample}")
        print("-"*50)

