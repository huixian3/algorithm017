# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 房屋呈二叉树链接
    def rob(self, root: TreeNode) -> int:

        def recur(node):
            if not node:
                return 0, 0
            # a:不打劫   b:打劫
            left_a, left_b = recur(node.left)
            right_a, right_b = recur(node.right)
            node_a = max(left_a + right_b, left_a + right_a, left_b + right_b, left_b + right_a)
            node_b = left_a + right_a + node.val
            return node_a, node_b
        a, b = recur(root)
        return max(a,b)