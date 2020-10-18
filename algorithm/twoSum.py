'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''
#由于数据范围过大,所有不合适用散列表,选择用dict作为索引,特殊情况是没有东西

class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    def twoSum(self):
        My_Dict = {}
        for i in range(len(self.nums)): #遍历self.nums,优化写法2   https://www.runoob.com/python/python-func-enumerate.html
            #if(My_Dict.get(self.nums[i])):
            #   print("%s is exists!"%(self.nums[i]))
            #print(My_Dict.get(self.nums[i]))   没有返回值就是None
            #print(type(My_Dict.get(self.nums[i])))  <class 'NoneType'>
            key = self.nums[i]
            pair_key = self.target - key #寻找target匹配
            print("pair_key = "+str(pair_key))
            if(My_Dict.get(pair_key) != None):
                return [My_Dict.get(pair_key), i]
            else:
                My_Dict.update({key:i})
            print(My_Dict)
            
        return []
       
def twoSum(nums, target): #优化写法3
    hashmap={}
    '''
    enumerate会遍历nums,返回两个值,i是下标key,num是nums[i],
    可以通过enumerate(nums,1)定义索引自定义所以的下标,默认是0
    '''
    for i,num in enumerate(nums):
        if hashmap.get(target - num) is not None:
            return [i,hashmap.get(target - num)]
        hashmap[num] = i #这句不能放在if语句之前，解决list中有重复值或target-num=num的情况


if __name__ == "__main__":
    
    My_List = []
    target = 6
    s1 = Solution(My_List,target)
    print(s1.twoSum())

