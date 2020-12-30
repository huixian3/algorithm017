# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k < 1:
            return head
        fast, slow = head, head
        # 链表长度=n+1,同时fast移动到tail
        n = 0
        while fast and fast.next:
            fast = fast.next
            n = n+1
        # 处理k值
        k = k % (n+1)
        if k == 0:
            return head
        # 移动slow到旋转后的tail，其当前 next=new_head & next赋值为null
        for i in range(n-k):
            slow = slow.next

        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head

