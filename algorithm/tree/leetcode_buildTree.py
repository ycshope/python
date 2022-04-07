# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from binarytree import Node, build


#根据前序和后序列来生成二叉树
#先序的特点:根左右
#中心的特点:左根右
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Node:
        #划分出左右preorder和inorder的左右区域即可
        #1.选找出本树的根节点
        if (length := len(preorder)) == 0:
            return None
        rootVal = preorder[0]
        root = Node(value=rootVal)

        inorRootIndex = inorder.index(rootVal)
        # print(f"root={root.value},inorRootIndex={inorRootIndex}")

        #2.找出左子树所在的位置
        #inorRootIndex=2
        # rchildtree=inorderp[0:inorRootIndex],preorder[1:inorRootIndex+1]
        if inorRootIndex == 0:
            root.right = self.buildTree(preorder[0:inorRootIndex],inorder[1:inorRootIndex+1])
        else:
            pass
        # [0:2)[1:3)

        #3.找出右子树所在的位置
        # lchildtree=inorderp[inorRootIndex+1:],preorder[inorRootIndex:]
        # [3:)[2:)


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    s = Solution()
    s.buildTree(preorder, inorder)
