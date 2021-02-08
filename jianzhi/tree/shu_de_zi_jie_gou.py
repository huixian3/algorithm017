# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        # 递归判断B是否在以A为根节点的树中
        def iscontain(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return iscontain(A.left, B.left) and iscontain(A.right, B.right)

        # 从根节点开始 or 左子树 or 右子树 包含树B
        if not B or not A:
            return False
        return iscontain(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
