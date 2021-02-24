# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = collections.deque([root]) if root else []
        res = []
        while queue:
            size = len(queue)
            level = collections.deque()
            for i in range(size):
                node = queue.popleft()
                # 和层次遍历唯一的区别：每层根据 层奇偶 判断添加顺序。
                if not len(res)%2: level.append(node.val)
                else: level.appendleft(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(list(level))
        return res