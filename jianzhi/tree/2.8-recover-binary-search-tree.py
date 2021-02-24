# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    # Q：给你二叉搜索树的根节点 root ，该树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。
    # 问题的关键在于找到需要交换的两个node：first、second
    # 通过中序遍历，确认两个点，之后进行交换即可

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.first, self.second = None, None
        self.prev = None
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.prev and root.val < self.prev.val:
                self.first = self.first if self.first else self.prev
                self.second = root
            self.prev = root
            inorder(root.right)

        inorder(root)
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val
