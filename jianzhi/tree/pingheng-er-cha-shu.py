# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # def deep(node):
        #     if not node: return 0
        #     return max(deep(node.left), deep(node.right)) + 1
        #
        # if not root: return True
        # dis = deep(root.right) - deep(root.left)
        # # 注意需要分别判断左右子树是否平衡 self.isBalanced(root.left) and self.isBalanced(root.right)
        # return dis >= -1 and dis <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


        # 以下方法进行剪枝，效率较高
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            if left == -1: return -1
            right = recur(root.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1

