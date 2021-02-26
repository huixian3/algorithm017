# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
反转从位置m到n的链表。请使用一趟扫描完成反转。
说明:1 ≤ m ≤ n ≤ 链表长度。
'''
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return null
        cur, prev = head, None
        # 找到反转起始位
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m-1, n-1
        # 保存开始翻转的前一位
        tail, con = cur, prev
        # 开始反转
        while n > 0:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            n = n-1
        # 处理翻转前后链表链接
        tail.next = cur
        if con:
            con.next = prev
        else:
            head = prev
        return head