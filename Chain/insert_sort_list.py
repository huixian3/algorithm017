class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# 头插法 需多复习，没看太明白
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 3 1 4 5 2 3
        dummy = ListNode(0)
        curr = head
        while curr:
            prev = dummy
            temp = curr.next
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            curr.next = prev.next
            prev.next = curr
            curr = temp
        return dummy.next

Solution().insertionSortList()