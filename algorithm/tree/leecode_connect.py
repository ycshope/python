# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
# Definition for a Node.
class Node:
    def __init__(self,
                 val: int = 0,
                 left: 'Node' = None,
                 right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # 思路
        # 1.由于是满二叉树,找到最右边的节点即可,用bfs算法,每层最后一个节点必然他的next为#
        # 编码
        # 1.bfs+queue,难度比较大
        pass


if __name__ == "__main__":
    pass
