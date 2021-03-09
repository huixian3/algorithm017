class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# 头插法 需多复习，没看太明白

'''
147. 对链表进行插入排序
插入排序 时间复杂度O(N^2)  
需要知道插入位置的前一个节点所以要判断next指针
'''
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 正常插入排序 O(n*n)
        # 维护 dummy 亚节点，用于在head之前插入节点
        # 维护lastsorted 节点，和当前节点比较，判断是否需从前往后判断
        if not head: return head
        dummy = ListNode(0, head)
        curr = head.next
        last_sorted = head
        while curr:
            tmp = curr.next
            if curr.val >= last_sorted.val:
                last_sorted = curr
                # last_sorted = last_sorted.next
            elif curr.val < last_sorted.val:
                prev = dummy
                while prev.next and prev.next.val <= curr.val:
                    prev = prev.next
                last_sorted.next = curr.next
                curr.next = prev.next
                prev.next = curr

            curr = tmp #last_sorted.next
        return dummy.next

        # 头插法
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