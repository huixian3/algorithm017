# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 右中左，第k个节点
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.res = -1
        def dfs(node):
            if not node: return
            dfs(node.right)
            if self.k == 0: return
            self.k -= 1
            if self.k == 0: self.res = node.val
            dfs(node.left)
        dfs(root)
        return self.res


    # def kthLargest(self, root: TreeNode, k: int) -> int:
    #     def dfs(root):
    #         if not root: return
    #         dfs(root.right)
    #         if self.k == 0: return
    #         self.k -= 1
    #         if self.k == 0: self.res = root.val
    #         dfs(root.left)

    #     self.k = k
    #     dfs(root)
    #     return self.res




