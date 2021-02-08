# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        i, j = 0, 0
        l_node, r_node = head, head
        while r_node:
            r_node = r_node.next
            j += 1
            if j > k:
                l_node = l_node.next
        return l_node


