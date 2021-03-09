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
        '''
        给定一个链表和一个特定值 x，对链表进行分隔
        使得所有小于 x 的节点都在大于或等于 x 的节点之前。
        你应当保留两个分区中每个节点的初始相对位置。
        
        思路：
        1. 分成两个链表，
        2. 进行合并，处理链接处 
        '''
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

