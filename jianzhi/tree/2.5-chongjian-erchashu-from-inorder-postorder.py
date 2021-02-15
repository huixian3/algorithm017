# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # 前序
        def recur(root, left, right):
            if left > right: return
            node = TreeNode(postorder[root])
            index = in_dic[postorder[root]]
            node.left = recur(root-1-right + index, left, index-1)
            node.right = recur(root-1, index+1, right)
            return node

        if not inorder or not postorder or len(inorder) != len(postorder): return None
        in_dic = {}
        for i in range(len(inorder)):
            in_dic[inorder[i]] = i
        return recur(len(inorder) - 1, 0, len(inorder) - 1)
