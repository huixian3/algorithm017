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
        # 快慢指针
        if n < 1 or not head:
            return head
        fast = head
        slow = head
        i = 0
        while fast:
            if i > n: # fast 走 n+1 步之后，slow 开始
                slow = slow.next # slow 恰好能到达 倒数第 n+1 个节点。
            fast = fast.next
            i = i + 1
        if i > n:
            slow.next = slow.next.next
        else:
            return head.next
        return head


        # 借助栈 pop n 个节点，修改上一个节点的 next 即可。
        if n < 1 or not head:
            return head
        stack= list()
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        for i in range(n):
            stack.pop()
        if stack:
            prev = stack[-1]
            prev.next = prev.next.next
        else:
            head = head.next
        return head




