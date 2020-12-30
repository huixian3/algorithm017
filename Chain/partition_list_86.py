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
        # 逐段将小于x的node转移到头部
        cur = head
        prev = head
        while cur:

            if cur.val < x:
                t_h = cur
                t_t = cur
                while cur and cur.val < x:
                    t_t = cur
                    prev = cur
                    cur = cur.next
                temp_head = head
                head = t_h
                prev.next = cur
                t_t.next = temp_head
            else:
                prev = cur
                cur = cur.next
        return head

        # 分割成两个链表，之后进行合并

