class Solution(object):
    def detectCycle(self, head):
        if not head:
            return None
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        # 无环
        if not (fast and fast.next ):
            return None

        p = head
        m = fast
        while p != m:
            p = p.next
            m = m.next
        return p
