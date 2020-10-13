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
    def reverse(self, x):
        #负数特殊处理
        Is_lt_zero = False
        if x < 0:
            Is_lt_zero = True 
            x *= -1
        ans = 0
        #翻转数字
        #print("x = %d"%(x))
        while int(x) != 0 : #python的类型个位数/10会转换为小数
            #print("x= %d, ans = %d"%(x,ans))
            ans *= 10
            ans += int(x%10)
            #边界条件可以提前
            if ans<-2147483648 or ans>2147483647:
                return 0
            x = int(x/10)
            
        if Is_lt_zero:
            ans *= -1
            ''''
        #边界条件
        if ans<-2147483648 or ans>2147483647:
            return 0
            '''
        return ans
    
if __name__ == "__main__":

    arr_x = [ 123, -123 , 120 , 0 ,1534236469]
    
    #Solution s     定义方法不对
    s = Solution()

    for x in arr_x:
        print(s.reverse(x))
    
