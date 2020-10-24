'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:
Input: root = [3,9,20,None,None,15,7]
Output: 2
Example 2:

Input: root = [2,None,3,None,4,None,5,None,6]
Output: 5
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000

'''
#学习点:队列 deque
# Definition for a binary tree node.
from collections import deque
#创建一棵树,以node作为根节点,
def Create_Tree(gen_list:list):
    #print(f"gen_list={gen_list}")
    #边界条件:没有元素
    if len(gen_list) == 0:
        return None
    Root = TreeNode(gen_list[0])
    q = deque()
    q.append(Root)
    i = 1
    max_len = len(gen_list)
    while i < max_len:
    #每次出队列一个元素,作为父节点
        root = q.popleft()
        #print(f"root={root.val}")
    #读取的一个元素作为左节点,如果读取的节点是None那么不入队,否则入队
        if i < max_len and gen_list[i]:
            node = TreeNode(gen_list[i])
            root.left = node
            q.append(node)
            #print(f"root.left={root.left.val}")
        i += 1    
    #读取的第二个元素作为右边节点,如果读取的节点是None那么不入队,否则入队
        if i < max_len and gen_list[i] :
            node = TreeNode(gen_list[i])
            root.right = node
            q.append(node)
            #print(f"root.right={root.right.val}")
        i += 1
    return Root
 
    
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    '''思路1:BFS
            时间o(n),空间o(n)
            用列队实现
            Q1.怎么知道深度?
            A: deep(node.clid)=deep(node)+1
            如果通过列队来实现BFS有如下特性:
                1.新进队的
    '''
    def minDepth(self, root: TreeNode) -> int:
        #边界条件：空树
        if root is None:
            return 0
        #叶子节点开始返回1
        if root.left is None and root.right is None:
            return 1
        #非叶子节点返回左右节点中较小的深度
        #边界条件:某个节点为单臂
        deep = 10000
        if root.left is not None:
            deep = min(self.minDepth(root.left),deep)
        if root.right is not None:
            deep = min(self.minDepth(root.right),deep)
        return deep+1

        '''
        优化1
        childDepth的解释：

            如果左子树深度、右子树深度均不为0，则用min取其中最小值
            如果有一个为0，取其中非0的数；都为0，取0
            ( 有一个为零，一个不为零，说明此节点不是叶子节点，要计算深度必须还要往下)
        '''
    def minDepth_2(self, root: TreeNode) -> int:
        if not root : return 0
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        childDepth = min(leftDepth, rightDepth) if leftDepth and rightDepth else leftDepth or rightDepth
        return 1 + childDepth
        
    #BFS： 按层遍历，寻找第一个叶子结点
    def minDepth_3(self, root: TreeNode) -> int:
        if not root:
            return 0
        #定义元组,同时记录深度
        q = deque([(root, 1)])
        while q:
            node, depth = q.popleft()
            #找到第一个叶节点,直接返回结果
            if not node.left and not node.right:
                return depth
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
                
        return 0


        
if __name__ == "__main__":
    root_list = [[3,9,20,None,None,15,7], [2,None,3,None,4,None,5,None,6], []]
    s = Solution()
    for root in root_list:
        root_Node = Create_Tree(root)
        print(f"minDepth={s.minDepth(root_Node)}")