#!/usr/bin/python3
# coding=utf-8
def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    def traverse(node, res):
        if node == None:
            return
        traverse(node.left, res)
        res.append(node.val)
        traverse(node.right, res)
    res = []
    traverse(root, res)
    return res