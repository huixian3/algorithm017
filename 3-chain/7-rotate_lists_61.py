# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # 旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        '''
        链表旋转，处理旋转节点前后指针变化即可
        0. 处理旋转长度过大的情况，获取真实旋转次数
        1. 找到旋转前尾结点 -》旋转后，链接到初始的头节点； 
        2. 找到旋转点，也即是新的尾节点 和 头结点，尾结点.next=None
        '''
        if not head or k < 1:
            return head
        fast, slow = head, head
        # 链表长度=n+1,同时fast移动到之前tail
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

