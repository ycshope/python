# https://leetcode-cn.com/problems/group-anagrams/
class Solution:
    def __init__(self, s):
        self.ans = self.lengthOfLongestSubstring(s=s)

    def __str__(self) -> str:
        return str(self.ans)

    def lengthOfLongestSubstring(self, s: str) -> int:
        # 考点1:子问题划分
        # 考点2:滑动窗口
        # NOTE:关键思路:
        # 1.划分子问题:i从每一个字符开始的，不包含重复字符的最长子串
        # 2.找到子问题和子问题之间的关联性
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            # 求解从i开始的最长不重复子串
            # 已经解决了i-1个问题
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])

            #找到 lengthOfLongestSubstring[i]
            while rk < n - 1 and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
            
        return ans


if __name__ == "__main__":
    s_list = ["abcabcbb", "bbbbb", "pwwkew"]
    for s in s_list:
        q = Solution(s=s)
        print(q)
