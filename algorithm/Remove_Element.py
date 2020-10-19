'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
 

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or nums = [2,3,0,0], your answer will be accepted.
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3]
Explanation: Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4. Note that the order of those five elements can be arbitrary. It doesn't matter what values are set beyond the returned length.
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100

'''
class Solution:
    def removeElement(self, nums, val: int) -> int:
        #解法1.速度慢,c++则可以通过下标循环移动来解决实现优化
        while val in nums :
            nums.remove(val)
        #print(nums)
        return len(nums)
     #优化解法,遇到非指定的元素,才生成.指定的元素不加入
     '''
     说是删除，其实删除很费时间。
双指针其实就是两个数，分别代表两个index，表示数组中第几个数的意思。
比如这里，我们让a代表一个index，b代表一个index
然后我们让a一直往后移动，相当于nums[a]从数组第一个数遍历到最后一个数。
当且仅当我们发现nums[a] != val的时候，我们把这个数拷贝到b指向的位置，默认b是从0开始的，然后b += 1指向下一个位置。

这样我们就保证了前b个数，就是我们要的结果。不重复的数。
99.33%的时间效率。诶哟不错哦。

'''
    def removeElement_improve(self, nums: List[int], val: int) -> int:
        a = 0
        b = 0

        while a < len(nums):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1
        return b
      
if __name__ == "__main__":
    nums_list = [[3,2,2,3], [0,1,2,2,3,0,4,2], []]
    s = Solution()
    for nums in nums_list :
        print(nums)
        val = input("输入删除的值:")
        print(s.removeElement(nums , int(val)))