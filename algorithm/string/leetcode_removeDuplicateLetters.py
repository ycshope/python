# https://leetcode-cn.com/problems/remove-duplicate-letters/
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        #思路:1.枚举
        # 找出所有除后的结果,进行排序

        #思路:2.贪心+回溯

        stack = []
        import collections
        remain_counter = collections.Counter(s)

        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and remain_counter[
                        stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            remain_counter[c] -= 1
        return ''.join(stack)


if __name__ == "__main__":
    s = "cbacdcbc"
    q = Solution()
    q.removeDuplicateLetters(s)
