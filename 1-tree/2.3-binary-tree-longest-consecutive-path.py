"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys
class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # DFS
        self.max = 0
        def dfs(node, last, length): # 遍历记录连续路径的长度

            if not node:
                self.max = length if self.max < length else self.max
                return

            if node.val != last + 1:
                self.max = length if self.max < length else self.max
                length = 0

            dfs(node.left, node.val, length+1)
            dfs(node.right, node.val, length+1)

        dfs(root, -1, 0)
        return self.max

        # recursive
        self.longest = 0
        def recur(root): # 返回输入节点开始的最长连续路径
            if not root:
                return 0

            left = recur(root.left)
            right = recur(root.right)
            slongest = 1
            if root.left and root.val + 1 == root.left.val:
                slongest = max(slongest, left + 1)

            if root.right and root.val + 1 == root.right.val:
                slongest = max(slongest, right + 1)
            self.longest = max(self.longest, slongest)
            return slongest
        recur(root)
        return self.longest

