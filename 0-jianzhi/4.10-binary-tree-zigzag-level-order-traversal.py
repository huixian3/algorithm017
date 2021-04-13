# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = deque([root]) if root else deque()
        level = 0
        res = []
        while queue:
            cur = collections.deque()
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if level&1 == 0: cur.append(node.val)
                else: cur.appendleft(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            level += 1
            res.append(list(cur))
        return res
