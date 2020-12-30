# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 暴力遍历两次:第一次计算链表长度，第二次取第 L-n+1 个node

        # 入栈
        # dummy = ListNode(0, head)
        # stack = list()
        # cur = dummy
        # while cur:
        #     stack.append(cur)
        #     cur = cur.next

        # for i in range(n):
        #     stack.pop()

        # prev = stack[-1]
        # prev.next = prev.next.next
        # return dummy.next

        # 栈
        # if n < 1 or not head:
        #     return head
        # stack= list()
        # cur = head
        # while cur:
        #     stack.append(cur)
        #     cur = cur.next
        # for i in range(n):
        #     stack.pop()
        # if stack:
        #     prev = stack[-1]
        #     prev.next = prev.next.next
        # else:
        #     head = head.next
        # return head




        # 快慢指针
        if n < 1 or not head:
            return head
        fast = head
        slow = head
        i = 0
        while fast:
            if i > n:
                slow = slow.next
            fast = fast.next
            i = i + 1
        if i > 1:
            slow.next = slow.next.next
        else:
            return head.next
        return head




