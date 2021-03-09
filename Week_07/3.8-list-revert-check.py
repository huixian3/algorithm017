class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class solution:
    def revert(self, head, tail):
        cur = head
        prev = tail.next
        # 注意 prev == tail, 代表tail已经反转完成
        while prev != tail:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return tail, cur

    # k个一组反转
    def revert_k_m(self, head, k):
        dummy = ListNode(0, head)
        prev = dummy

        while head:
            tail = prev
            for i in range(k):
                tail = tail.next
                if not tail: return dummy.next
            head, tail = self.revert(head, tail)

            # 处理翻转后衔接
            prev.next = head
            prev = tail
            head = tail.next
        return dummy.next


    # 反转前k个节点
    def revert_k_node(self, head, k):
        i = 1
        tail = head

        while i < k and head.next:
            head = head.next
            i += 1
        new_head, new_tail = self.revert(tail, head) # revert
        return new_head

input = ListNode(0, ListNode(2, ListNode(3, ListNode(4, None))))

res = solution().revert_k_m(input, 2)
while res:
    print(res.val)
    res = res.next