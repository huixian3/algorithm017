# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        path_list = collections.defaultdict(int)
        res = []
        # 1. 以自己为根的二叉树长什么样？ 树的序列化
        # 2. 以别的节点为跟的二叉树集合
        # 3. 判断是否有出现过，if not 存储；else 结果 + 1
        def dfs(root): # 函数功能：找到当前节点的树结构，空节点补充"#"
            if not root: return "#"
            left = dfs(root.left)
            right = dfs(root.right)
            # 注意：此处不能用中序遍历，
            cur_path = left + ',' + right + ',' + str(root.val)
            # 3. 判断该条子路是否出现过，以及去重
            if path_list[cur_path] == 1: res.append(root)
            path_list[cur_path] = path_list[cur_path] + 1
            return cur_path

        dfs(root)
        return res


