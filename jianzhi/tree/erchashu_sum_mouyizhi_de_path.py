# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        # DFS
        res = []
        def dfs(node, l, s):
            # end
            if not node:
                return
            if not node.left and not node.right:
                if node.val + s == sum:
                    res.append(l + [node.val])
                return
            # handle next level
            if node.left: dfs(node.left, l + [node.val], s+node.val)
            if node.right: dfs(node.right, l + [node.val], s+node.val)
            # reverse
            
        dfs(root, [], 0)
        return res


