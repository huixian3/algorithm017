# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    '''
    给你二叉树的根结点 root ，请你将它展开为一个单链表：
    要求：返回顺序和先序遍历相同
    '''
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # TODO 前序遍历顺序不正确 先左节点，后右节点 配合 先进后出 notack

        # 先右节点，后左节点 配合 后进先出 ack
        if not root:
            return

        stack = [root]
        prev = None

        while stack:
            curr = stack.pop()
            if prev:
                prev.left = None
                prev.right = curr
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            prev = curr


        # 后序遍历
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)

        # 处理当前节点
        left = root.left
        right = root.right
        root.right = left
        root.left = None
        while root.right:
            root = root.right
        root.right = right







