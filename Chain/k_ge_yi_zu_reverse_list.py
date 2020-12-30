class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head, tail):
        cur = head
        prev = tail.next
        while prev != tail:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return tail, head

        # prev = tail.next
        # p = head
        # while prev != tail:
        #     nex = p.next
        #     p.next = prev
        #     prev = p
        #     p = nex
        # return tail, head

    def reverseKGroup(self, head, k: int):

        dummy = ListNode(0, head)
        prev = dummy

        # cur = head
        while head:
            tail = prev
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            head, tail = self.reverse(head, tail)
            prev.next = head
            prev = tail
            head = tail.next

        return dummy.next


