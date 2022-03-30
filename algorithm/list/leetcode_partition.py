# https://leetcode-cn.com/problems/partition-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Link:
    def __init__(self, linknode: ListNode, listnode: list) -> None:
        self.linknode = linknode if linknode else None
        self.listnode = listnode if listnode else None

    def createLink(self):
        def list2link(listnode: list, index: int) -> ListNode:
            if index < len(listnode):
                linknode = ListNode(val=listnode[index])
                linknode.next = list2link(listnode, index + 1)
                return linknode
            return None

        if self.listnode is None:
            return ListNode()
        self.linknode = list2link(listnode=self.listnode, index=0)

    def Link2List(self):
        head = self.linknode
        tlist = []
        while head:
            tlist.append(head.val)
            head = head.next
        return str(tlist)
        # print(str(tlist))


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        #思路1:双指针,发现小于的就加入新列表,大于的保留,最后小的列表拼接大的链表
        #编码1:相当困难

        #思路2:小于的保留,大于的放入一个list,最后将这个list转换为link并添加到末尾

        #思路3:用带有头节点的small和lager,最后合并即可

        # 边界条件,均为空
        if head == None:
            return head

        small = ListNode()
        lager = ListNode()

        # small和lager的当前指针,用于取出head的节点
        small_node = small
        lager_node = lager

        # lager_header用于最后的拼接
        lager_header = lager

        while head:
            #小于x的节点放入small
            if head.val < x:
                small_node.next=head
                small_node=small_node.next
                head=head.next
                small_node.next=None
            #大于等于x的节点放入lager
            else:
                lager_node.next=head
                lager_node=lager_node.next
                head=head.next
                lager_node.next=None
         
        # 连接头和尾部
        small_node.next=lager_header.next

        return small.next


if __name__ == "__main__":
    head = [1, 4, 3, 2, 5, 2]
    x = 3
    testh = Link(linknode=None, listnode=head)
    testh.createLink()
    # testh.Link2List()
    s = Solution()
    testh.linknode = s.partition(testh.linknode, x)
    print(testh.Link2List())
