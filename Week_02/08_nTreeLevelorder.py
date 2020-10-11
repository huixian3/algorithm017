#!/usr/bin/python3
# coding=utf-8

# TODO
# BFS 使用队列实现 queue deque
# 栈 用于深度优先搜索
import collections
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        # 77.9% 递归：保存每个节点的level，每层的顺序保持就可以
        def levelSave(node, level):
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            for child in node.children:
                levelSave(child, level+1)
        if not root:
            return list()
        result = []
        levelSave(root, 0)
        return result

        # 77.9% BFS 逐层遍历
        # if not root:
        #     return list()
        # d = collections.deque()
        # res = []
        # d.append(root)
        # while d:
        #     r = []
        #     for i in range(len(d)):
        #         node = d.popleft()
        #         r.append(node.val)
        #         for child in node.children:
        #             d.append(child)
        #     res.append(r)
        # return res

        # BFS PYTHON代码简化
        d, res = [root] if root else [], []
        while d:
            res.append([node.val for node in d])
            d = [child for node in d for child in node.children]
        return res


