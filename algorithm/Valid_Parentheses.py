'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        #边界情况,奇数不可能匹配
        if  len(s)%2:
            return False
            
        #用list实现栈
        stack = []
        #左边栈
        l = ["(", "[", "{"]
        #右边的索引
        counterpart = {")":"(" ,"]":"[" ,"}":"{"}
        for i,brackets in enumerate(s):
            #如果是左边括号,那么直接进栈
            if brackets in l:
                stack.append(brackets)
            #不是左边括号就直接匹配,匹配失败就直接报错
            else:
                #遗漏情况,空栈时候弹出
                #问题出现的原因:以为空list弹出结果是None,实际上空list弹出是报错
                if len(stack) == 0:
                    return False
                top_element = stack.pop()   #栈顶可以用stack[-1]来代替
                if  counterpart.get(brackets) != top_element:
                    return False
        #不能丢掉,异常输入是"(("
        if(len(stack) == 0): #优化 return not stack
            return True
        else:
            return False
#优化1
class Solution:
    def isValid(self, s: str) -> bool:
        if  len(s)%2: return False
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?'] #用于解决空栈被弹出的bug,这个符号一定不会被匹配
        for c in s:
            if c in dic: stack.append(c)
            elif dic[stack.pop()] != c: return False 
        return len(stack) == 1


if __name__ == "__main__":
    str_list = ["()", "()[]{}", "(]", "([)]", "{[]}","{[]}(}","{}[","){"]
    #str_list2 = ["){"]#遗漏情况
    for i,str in enumerate(str_list,1):
        s = Solution()
        print("sample#%d:"%(i))
        print(s.isValid(str))