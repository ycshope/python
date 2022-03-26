# https://leetcode-cn.com/problems/validate-stack-sequences/
class Solution:
    def validateStackSequences(self, pushed: list[int],
                               popped: list[int]) -> bool:

        #边界条件:pushed为空
        pushedlength= len(pushed)

        class Stack():
            def __init__(self):
                self.stack = []

            def push(self, value):
                self.stack.append(value)

            def pop(self):
                if self.stack:
                    self.stack.pop()
                else:
                    raise LookupError('stack is empty!')

            def is_empty(self):
                return self.stack == []

            def top(self):
                return self.stack[-1]

        s = Stack()
        pushedindex = 0
        for pop in popped:
            # 假设出栈的元素为pop[i],那么他要么就是在push中,要么在stack中
            # 1.如果stack.top为pop[i],那么直接出栈
            if not s.is_empty() and pop == s.top():
                s.pop()
            elif pushedindex < pushedlength:
                # 2.在pushed[j]从前往后找到pop[i]
                while pushedindex < pushedlength:
                    if pushed[pushedindex] != pop:
                        s.push(pushed[pushedindex])
                        pushedindex = pushedindex + 1
                    else:
                        pushedindex = pushedindex + 1
                        break
            else:
                return False

        return True

    def validateStackSequences2(self, pushed, popped):
        j = 0
        stack = []
        for x in pushed:
            stack.append(x)
            #写法很简介
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j == len(popped)


if __name__ == "__main__":
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    # pushed = [1, 2, 3, 4, 5]
    # popped = [4, 3, 5, 1, 2]
    #注意是每个值都不能重复
    # pushed = [1, 2, 7, 2, 3]
    # popped = [2, 3, 7, 2, 1]
    s = Solution()
    ans = s.validateStackSequences(pushed=pushed, popped=popped)
    print(f"{ans}")
