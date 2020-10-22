'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000

'''
# Definition for a binary tree node.
import queue
#创建一棵树,以node作为根节点,node.val=list[i]
def Create_Tree(gen_list:list, i:int):
    #边界条件,直接返回空节点
    if i >= len(gen_list) or gen_list[i] is None:
        return None
    node = TreeNode(val = gen_list[i])
    node.left = Create_Tree(gen_list, i*2+1)
    node.right = Create_Tree(gen_list, i*2+2)
    str = f"node={node.val}"
    if node.left is not None:
        str += f",lchild={node.left.val}"
    if node.right is not None:
        str += f",rchild={node.right.val}"
    print(str)
    return node
    
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def Is_leaf(self, node:TreeNode):
        return node.left is None and nodes.right is None
    #def minDepth(self, root: TreeNode) -> int:
    '''思路1:BFS
            时间o(n),空间o(n)
            用列队实现
            Q1.怎么知道深度?
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
    
        
if __name__ == "__main__":
    root_list = [[3,9,20,None,None,15,7], [2,None,3,None,4,None,5,None,6], [None]]
    s = Solution()
    for root in root_list:
        root_Node = Create_Tree(root,0)
        print(f"minDepth={s.minDepth(root_Node)}")