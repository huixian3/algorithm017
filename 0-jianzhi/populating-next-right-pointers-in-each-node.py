"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution(object):
    # 二叉树层次链接
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # 层次遍历，每层添加指针
        d = deque([root]) if root else deque()
        while d:
            n = len(d)
            for i in range(n):
                tmp = d.popleft()
                if i < n-1:
                    tmp.next = d[0] # 添加指针，直到当前层最后一个元素
                if tmp.left:
                    d.append(tmp.left)
                if tmp.right:
                    d.append(tmp.right)
        return root

