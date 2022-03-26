# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# ref:https://leetcode-cn.com/problems/path-sum/
from os import lchflags


class Solution:
    def hasPathSum(self, root: list, targetSum: int) -> bool:
        #从下标开始,一直往下走,左节点i*2+1,右节点i*2+2
        nums=len(root)

        #node表示当前节点的下标,sum表示到当前节点的总和
        def dfs(node,sum):
            lchild=node*2+1
            rchild=node*2+2
            pass
        return dfs(0,0)

if __name__ == "__main__":
    Solution.hasPathSum (root=[5,4,8,11,None,13,4,7,2,None,None,None,1],targetSum = 22)
