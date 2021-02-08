# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def recur(left, right):
            if left > right: return
            max_v, k = -sys.maxsize-1, -1
            for i in range(left, right + 1):
                if nums[i] > max_v:
                    max_v, k = nums[i], i
            node = TreeNode(max_v)
            node.left = recur(left, k-1)
            node.right = recur(k+1, right)
            return node

        return recur(0, len(nums)-1)