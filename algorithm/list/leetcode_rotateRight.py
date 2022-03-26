# Definition for singly-linked list.
# https://leetcode-cn.com/problems/rotate-list/submissions/
# 需要看答案
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def CrateListNode(arr: list, index: int) -> ListNode:
    if index < len(arr):
        node = ListNode(val=arr[index], next=CrateListNode(arr, index + 1))
        # print(f"node={node.val}")
        return node


def ShowListNode(head: ListNode):
    print(head.val)
    if head.next != None:
        ShowListNode(head=head.next)


class Solution:
    def __init__(self, head, k):
        self.head = head
        self.k = k
        self.ans = self.rotateRight(head=self.head, k=self.k)

    def __str__(self) -> str:
        return str(self.ans)

    def rotateRight2(self, head: ListNode, k: int) -> ListNode:
        #边界条件
        if k == 0 or not head or not head.next:
            return head
        self.n = 0

        def gettail(head: ListNode):
            self.n = self.n + 1
            if head.next is None:
                return head
            return gettail(head=head.next)

        def sltelem(head: ListNode, wanted: int):
            if wanted == 1:
                return head
            return sltelem(head=head.next, wanted=wanted - 1)

        #将需要旋转的元素放置到链表头
        #1.找到这样一个元素wantednode:
        # 在新的list中是最后一个元素（n-k）
        tailnode = gettail(head)
        # print(f"n={self.n},tailnode={tailnode.val}")
        k = k % self.n
        if k == 0:
            return head

        wanted = self.n - k
        wantednode = sltelem(head, wanted=wanted)
        # print(f"wanted={wanted},wantednode={wantednode.val}")

        # #2.wantednode既为队尾巴,wantednode->next为新的队头
        new_header = wantednode.next
        tailnode.next = head
        wantednode.next = None

        return new_header

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next:
            return head

        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1

        #海象表达式
        #等价含义 add=n-k%n; if add == n: return head
        #ref:https://blog.csdn.net/qq_40244755/article/details/102685199
        if (add := n - k % n) == n:
            return head

        cur.next = head
        while add:
            cur = cur.next
            add -= 1

        ret = cur.next
        cur.next = None
        return ret


if __name__ == "__main__":
    head = [1, 2, 3, 4, 5]
    k = 2
    lnhead = CrateListNode(head, 0)
    # ShowListNode(lnhead)
    s = Solution(head=lnhead, k=k)
    ShowListNode(s.ans)
