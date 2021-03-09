class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class solution:
    def revert(self, head, tail):
        cur = head
        dummy = tail.next
        while head != tail:
            temp = head.next
            head.next = dummy
            dummy = head
            head = temp
        # tail.next = head
        return tail, cur
    def revert_k_node(self, head, k):
        i = 0
        tail = head

        while i < k and head:
            head = head.next
            i += 1

        concur = head
        new_head, new_tail = self.revert(tail, head) # revert
        if concur: new_tail.next = head.next

        return new_head

input = ListNode(0, ListNode(2, ListNode(4, None)))

res = solution().revert_k_node(input, 2)
while res:
    print(res.val)
    res = res.next