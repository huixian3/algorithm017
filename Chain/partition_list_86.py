# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        # 分割成两个链表，之后进行合并
        min_dummy = ListNode(0)
        max_dummy = ListNode(0)
        min_tail = min_dummy
        max_tail = max_dummy
        while head:
            if head.val < x:
                min_tail.next = head
                min_tail = min_tail.next
            else:
                max_tail.next = head
                max_tail = max_tail.next
            head = head.next
        min_tail.next = max_dummy.next
        max_tail.next = None
        return min_dummy.next

