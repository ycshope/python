'''
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1

'''
class Solution:
    def reverse(self):
        Reverse_Begin = 0
        #特殊情况,0直接返回
        if self.x == 0:
            return 0
        #特殊情况,负数提取符号不翻转
        elif self.x < 0
            is_lt_zero = 1
        #转换成字符串
        self.x = str(self.x).reverse()
        #最后把前面的0给消除,最后再转换成数字返回
        if(self)
        return self.x
        
    def __init__(self, x):
        self.x = x
        #print("self.x = %d"%(self.x))
    
if __name__ == "__main__":

    arr_x = [ 123, -123 , 120 , 0 ]
    
    for x in arr_x:
        class_x = Solution(x)
        print(class_x.reverse())
    
