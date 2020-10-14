'''
Given a 32-bit signed integer, reverse digits of an integer.
Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
 
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
#学习内容：1.除号引起的类型转换 2.str的截取 3.条件赋值语句 4.//号的应用
class Solution:
    def reverse(self, x):
        #负数特殊处理
        Is_lt_zero = False
        if x < 0:
            Is_lt_zero = True 
            x *= -1
        ans = 0
        #翻转数字
        while x != 0 : 
            #print("x= %d, ans = %d"%(x,ans))
            ans *= 10
            ans += int(x%10)
            #边界条件可以提前
            if ans<-2147483648 or ans>2147483647:
                return 0
            x = int(x/10) #在进行过第一次的x/10以后,x就从int转换成float了
            
        if Is_lt_zero:
            ans *= -1
            ''''
        #边界条件
        if ans<-2147483648 or ans>2147483647:
            return 0
            '''
        return ans
    
    #参考解法1
    #字符串的截取string[start : end : step]
    #[start:end:step]表示从string的第start个索引位置开始到第end个索引之间截取子串，截取的步长是step
    def reverse_force(self, x):
        if -10 < x < 10:
            return x
        str_x = str(x)
        if str_x[0] != "-":
            str_x = str_x[::-1] 
            x = int(str_x)
        else:
            str_x = str_x[:0:-1]
            x = int(str_x)
            x = -x
        return x if -2147483648 < x < 2147483647 else 0
        
    #参考解法2
    def reverse_better(self, x):
        y, res = abs(x), 0  #多个变量赋值
        # 则其数值范围为 [−2^31,  2^31 − 1]
        boundry = (1<<31) -1 if x>0 else 1<<31 #这种写法类似gen_list,c++的:?
        while y != 0:
            res = res*10 +y%10
            if res > boundry :
                return 0
            y //=10 #//= 取整除赋值运算符 c //= a 等效于 c = c // a,也就是不转换类型
        return res if x >0 else -res
    
if __name__ == "__main__":

    arr_x = [ 123, -123 , 120 , 0 ,1534236469]
    
    #Solution s     定义方法不对
    s = Solution()

    for x in arr_x:
        print(s.reverse(x))
