'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?

 

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false
 

Constraints:

-231 <= x <= 231 - 1

'''
class Solution:
    def isPalindrome_str(self, x):
        if x < 0 :
            return False
        #转换成str
        str_x = str(x)
        #翻转
        str_x_rev = str_x[::-1]
        #print("str_x = "+str_x)
        #print("str_x_rev = "+str_x_rev)
        #直接对比
        #print("id_str_x = %d"%(id(str_x)))
        #print("id_str_x_rev = %d"%(id(str_x_rev))) 即便值一样,也无法确保id一样
        return True if str_x == str_x_rev else False

    def isPalindrome_int(self, x):
        if x < 0 :
            return False
        #翻转
        x_rev,x_t = 0,x
        while x_t != 0:
            x_rev = x_rev*10 + x_t%10   
            x_t //= 10
        
        return True if x_rev == x else False
        
    def isPalindrome_int(self, x: int) -> bool:
        """
        只反转后面一半的数字!!(节省一半的时间)
        """
        if x < 0 or (x!=0 and x%10==0):
            return False
        elif x == 0:
            return True
        else:
            reverse_x = 0
            while x > reverse_x:    #优化,提前一般结束,然后分奇数和偶数判断
                remainder = x % 10
                reverse_x = reverse_x * 10 + remainder
                x = x // 10
            # 当x为奇数时, 只要满足 reverse_x//10 == x 即可
            if reverse_x == x or reverse_x//10 == x:
                return True
            else:
                return False
    
 