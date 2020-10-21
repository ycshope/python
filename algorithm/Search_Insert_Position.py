'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0 #会导致查找值为-1
Example 5:

Input: nums = [1], target = 0
Output: 0
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

'''
class Solution:
    #在low和high中查找对应的元素target
    #注意元素至少为1个
    def Bi_search(self, nums:list, target:int, low:int , high:int):
        #定义中间元素
        mid = (low + high)//2
        #print("mid="+str(mid))
        #print("查找区间:"+str(nums[low:high+1]))
        #print("指定元素"+str(nums[mid]))
        #函数边界 1.元素找到 2.到达边界
        '''if nums[mid] == target or low == high:
            return mid
            会有bug：
            Input: nums = [1,3,5,6], target = 0 
            mid=-1
        '''
        if nums[mid] == target or low >= high: 
            return max(mid,0)
        #中间元素比目标元素大,那么在左边区间,否则在右边区间
        if nums[mid] > target :
            #return self.Bi_search(self, nums, target, low, high-1) 递归注意不需要带上self
            return self.Bi_search(nums, target, low, mid-1)
        else :
            return self.Bi_search(nums, target , mid+1, high)
    
        
    def searchInsert(self, nums: List[int], target: int) -> int:
        #方法1.找不到就直接添加,然后再排序,最后再找下标
        #方法2.直接二分查找,返回下标。没有那么直接插入
        #便捷外直接返回
        if target>nums[-1]: 
            return len(nums)
        elif target<nums[0]:
            return 0
        #特殊处理:
        nums.append(100000)
        #print("长度为:"+str(len(nums)))
        index = self.Bi_search(nums, target,0 ,len(nums)-1)
        #没有找到元素
        #当前目标打于index,那么插入index之后
        if nums[index] < target:
            index +=1
            #nums.insert(index+1,target)
        #当前目标小于index,那么插入index之前
            #nums.insert(index,target)
        nums.pop()
        #print("after="+str(nums))
        return index
        
if __name__ == "__main__":
    #Q = {[1,3,5,6]:7 ,[1,3,5,6]:0, [1]:0} key不允许是list
    Q = {5:[1,3,5,6], 2:[1,3,5,6], 7:[1,3,5,6], 0:[1,3,5,6]}
    Q1 = {0:[1]}
    s = Solution()
    for key in Q.keys():
        #print("key="+str(Q.get(key)))
        print("target="+str(key))
        print(s.searchInsert(Q.get(key), key))
    
    