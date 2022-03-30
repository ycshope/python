# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
# Definition for a Node.
from binarytree import Node

# TODO:解法2


# 二叉树
# https://zhuanlan.zhihu.com/p/39220021
class neoNode(Node):
    def __init__(self,
                 val: int = 0,
                 left: 'Node' = None,
                 right: 'Node' = None,
                 next: 'Node' = None):
        self.next = next
        Node.__init__(self, value=val, left=left, right=right)


class Btree():
    def __init__(self, arrtree: list, tree: neoNode) -> None:
        self.arrtree = arrtree if arrtree else None
        self.tree = tree if tree else self.creatBtree()

    def creatBtree(self):
        def arr2tree(arrtree: list, index: int):
            if index < len(self.arrtree):
                node = neoNode(val=arrtree[index])
                node.left = arr2tree(arrtree, index * 2 + 1)
                node.right = arr2tree(arrtree, index * 2 + 2)
                return node
            else:
                return None

        root = arr2tree(self.arrtree, 0)
        return root

    def dspNoneBtree(self):
        def dsptree(node: neoNode):
            if node.next == None:
                print(f"val={node.val}")
            if node.left != None:
                dsptree(node.left)
            if node.right != None:
                dsptree(node.right)

        dsptree(node=self.tree)


class Solution:
    def connect(self, root: neoNode) -> neoNode:
        # 思路
        # 1.由于是满二叉树,找到最右边的节点即可,用bfs算法,每层最后一个节点必然他的next为#
        # 编码
        if not root:
            return root

        # 队列的使用
        # https://blog.csdn.net/qq_39478403/article/details/105828125
        # 广度遍历
        import collections
        Q = collections.deque([root])

        # 每次取出一层
        while Q:
            length = len(Q)

            for i in range(length):
                #除了数列最后一个,其他都有next
                elem = Q.popleft()

                if i + 1 < length:
                    # next一定是队头
                    # elem.next=Q[0].val
                    elem.next = Q[0]
                    # print(f"{elem.val} has next,next={Q[0].val}")

                if elem.left:
                    Q.append(elem.left)

                if elem.right:
                    Q.append(elem.right)

        return root


if __name__ == "__main__":
    root = [1, 2, 3, 4, 5, 6, 7]
    q = Btree(root, None)
    s = Solution()
    ans = s.connect(q.tree)

    checkans = Btree(arrtree=None, tree=ans)
    checkans.dspNoneBtree()
