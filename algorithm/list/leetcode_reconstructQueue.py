# ref:https://leetcode-cn.com/problems/queue-reconstruction-by-height/
class Solution:
    def __init__(self, peoples) -> None:
        self.peoples = peoples

    def reconstructQueue(self, peoples: list[list[int]]) -> list[list[int]]:
        #边界条件
        length = len(peoples)
        if length == 0 or length == 1:
            return peoples

        #revsort by h--->保证了前面的数字一定大于后面的数字
        # [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]
        # def cmpHigh(people: list[int]):
        #     return people[0]

        # peoples.sort(key=cmpHigh, reverse=True)

        # lambda的用法 https://zhuanlan.zhihu.com/p/80960485?ivk_sa=1024320u
        # sort的用法 https://docs.python.org/3/howto/sorting.html
        peoples.sort(key=lambda x: (-x[0], x[1]))
        # [[9, 0], [7, 0], [6, 0], [6, 2], [5, 3], [5, 2], [3, 0], [3, 4], [2, 7], [1, 9]]

        index = 1
        #接下来后面的数字往前挪,对于[h而言,后面的数字再往前挪也必然满足规则]
        while index < length:
            people = peoples.pop(index)
            #对于a[i]而言,a[0]~a[i-1] >=a[i]
            #case1.if a[0]~a[i-1] >a[i],那么a[i]放入任意位置均不会对前面有任何影响
            #case2.if 存在一个a[j]=a[i],j<=i-1,那么放入a[i]可能会影响所有的a[j]
            #Q:那么该如何考虑?
            #case2特殊处理:往前遍历所有的a[i],小的放前面
            peoples.insert(people[1], people)
            index += 1

        return peoples

    def reconstructQueue2(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        n = len(people)
        ans = list()
        for person in people:
            ans[person[1]:person[1]] = [person]
        return ans

if __name__ == "__main__":
    # qlist = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    # qlist = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
    qlist = [[9, 0], [7, 0], [1, 9], [3, 0], [2, 7], [5, 3], [6, 0], [3, 4],
             [6, 2], [5, 2]]

    s = Solution(qlist)
    ans = s.reconstructQueue(peoples=s.peoples)
    print(ans)
