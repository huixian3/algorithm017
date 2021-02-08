# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # TODO 前序遍历顺序不正确 先左节点，后右节点 配合 先进后出 notack
        # if not root:
        #     return
        # stack = collections.deque([root])
        # # cur level
        # pre = None
        # while stack:
        #     node = stack.popleft()
        #     if pre:
        #         pre.right = node
        #         pre.left = None
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        #     pre = node
        # return

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
            left, right = curr.left, curr.right
            if right:
                stack.append(right)
            if left:
                stack.append(left)
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







