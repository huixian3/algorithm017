# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution(object):
    '''
    给定一个不含重复元素的整数数组 nums 。一个以此数组直接递归构建的 最大二叉树 定义如下：

    二叉树的根是数组 nums 中的最大元素。
    左子树是通过数组中 最大值左边部分 递归构造出的最大二叉树。
    右子树是通过数组中 最大值右边部分 递归构造出的最大二叉树。
    '''
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def recur(left, right):
            if left > right: return
            max_v, k = -sys.maxsize-1, -1
            # 找最大值->root
            for i in range(left, right + 1):
                if nums[i] > max_v:
                    max_v, k = nums[i], i
            node = TreeNode(max_v)
            node.left = recur(left, k-1)
            node.right = recur(k+1, right)
            return node

        return recur(0, len(nums)-1)