"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        #dfs 中序遍历
        self.prev = None
        self.head = None
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            # 处理当前节点
            #第一个节点为头节点，最后一个节点为尾结点；中间逐个进行节点链接即可
            if self.prev:
                self.prev.right = node
                node.left = self.prev
            else:
                self.head = node
            self.prev = node

            dfs(node.right)
        dfs(root)
        if self.prev and self.head:
            self.prev.right, self.head.left = self.head, self.prev
        return self.head





        # 未跑通；递归，分别将左右子树转成双向链表，之后处理链接处即可
        # if not root:
        #     return root
        # left, right = root.left, root.right
        # self.treeToDoublyList(left)
        # self.treeToDoublyList(right)
        #
        # mid1, head, mid2, tail = root.left, root.left, root.right, root.right
        # while head and head.left:
        #     head = head.left
        # while mid1 and mid1.right:
        #     mid1 = mid1.right
        #
        # while tail and tail.right:
        #     tail = tail.right
        # while mid2 and mid2.left:
        #     mid2 = mid2.left
        # if mid1 and mid2:
        #     mid1.right, mid2.left = mid2, mid1
        # if head and tail:
        #     head.left, tail.right = tail, head
        # return head


