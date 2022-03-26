class Solution:
    def __init__(self, strs):
        self.strs = strs
        self.ans = self.groupAnagrams2(strs=self.strs)

    def __str__(self) -> str:
        return str(self.ans)

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        import collections
        d = collections.defaultdict(list)
        #思路:字母异位词的set均相同,那么让他们为一组即可
        # 1.取出list[i]
        for st in strs:
            # 先排序字母后生成key
            # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
            key = "".join(sorted(st))
            # 全部归为一类
            d[key].append(st)
        # 2.如果没有那么新增set(list[i])
        # 3.如果有set(list[i]),那么扔进set(list[i])
        return list(d.values())

    def groupAnagrams2(self, strs: list[str]) -> list[list[str]]:
        import collections
        d = collections.defaultdict(list)
        #思路:字母异位词的hash均相同,那么让他们为一组即可
        for st in strs:
            c_hash = [0] * 26
            #取出每个char生成hash
            for ch in st:
                c_hash[ord(ch) - ord('a')] += 1
            #dict的key只能由数字、字符串、元组等不可变对象组成
            d[tuple(c_hash)].append(st)

        return list(d.values())


# https://leetcode-cn.com/problems/group-anagrams/

if __name__ == "__main__":
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # [["bat"],["nat","tan"],["ate","eat","tea"]]
    strs2 = [""]
    # [[""]]
    strs3 = ["a"]
    # [["a"]]
    strs_list = [strs1, strs2, strs3]
    for strs in strs_list:
        q = Solution(strs=strs)
        print(q)
    #考点:数据结构的使用
    # import collections
    # s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    # d = collections.defaultdict(list)
    # for k, v in s:
    #     d[k].append(v)
    # [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

    # print(d.items())
    #ref:
    # https://docs.python.org/zh-cn/3/library/collections.html#collections.defaultdict
