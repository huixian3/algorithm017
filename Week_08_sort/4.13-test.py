class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next
#
#
# @param head ListNode类 the head
# @param l int整型 left
# @param r int整型 right
# @return ListNode类
#
class Solution:
    def reversePartLinkedlist(self , head , l , r ):
        # write code here
        def revert(head, end):
            prev = end.next
            tail = head
            while head != end:
                tmp = head.next
                head.next= prev
                prev = head
                head = tmp
            end.next = prev
            return end, tail

        dummy = ListNode(0, head)
        i = 0
        # 保留反转前一个节点
        prev, h = dummy, dummy
        while h:
            if i == l-1:
                prev = h
                revert_head = h.next
            if i == r-1 or not h.next.next:
                revert_tail = h.next
                print(revert_tail.val)
                print(revert_head.val)
                revert_head, revert_tail = revert(revert_head, revert_tail)
                print(revert_tail.val)
                print(revert_head.val)
                prev.next = revert_head
                break
            i += 1
            h = h.next
        return dummy.next

node = Solution().reversePartLinkedlist(ListNode(1,ListNode(2,ListNode(3, ListNode(4)))), 1,3)
while node:
    print('res',node.val)




