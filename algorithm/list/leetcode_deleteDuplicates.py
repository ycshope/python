class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        #最简单的解法:从前往后用hash计算出现的次数,之后只保留对应的元素;  O(n)=2n

        #最优的解法: 每次到a[i]都会找到第一个和他不同的a[j],如果发现指针没有被挪动,那么加入,否则跳到下一个元素
        pass


if __name__ == "__main__":
    head = [1, 2, 3, 3, 4, 4, 5]
    head = [1, 1, 1, 2, 3]
    s = Solution()
