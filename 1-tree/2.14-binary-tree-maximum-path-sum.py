# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = -int(1e9)
        def maxpath(root): # 函数功能：当前节点开始的路径和
            if not root:
                return 0
            left = max(0, maxpath(root.left))
            right = max(0, maxpath(root.right))
            value = left + right + root.val
            self.res = max(self.res, value)
            return max(left, right) + root.val
        maxpath(root)
        return self.res
