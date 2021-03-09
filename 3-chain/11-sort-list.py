# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 非递归 时间复杂度：O(NlogN) 空间复杂度：O(1)
        # 用循环代替递归操作，模拟归并排序的思路，也就是先两两合并、之后四个一起合并、之后 ……
        # 需记录：合并的长度、每次合并的起始点和终点
        h, length, intv = head, 0, 1
        while h: h, length = h.next, length + 1
        res = ListNode(0, head)
        # merge the list in different intv.
        while intv < length:
            # 当前哑节点和头节点；
            # 疑问：res.next 怎么更新为当前头节点的？
            # 答：prev 每轮循环开始为res-null，逐个赋值；所以res.next = new_head
            pre, h = res, res.next
            while h:
                # get the two merge head `h1`, `h2`
                h1, i = h, intv
                while i and h: h, i = h.next, i - 1
                if i: break # no need to merge because the `h2` is None.
                h2, i = h, intv
                while i and h: h, i = h.next, i - 1

                c1, c2 = intv, intv - i # the `c2`: length of `h2` can be small than the `intv`.
                # merge the `h1` and `h2`.
                while c1 and c2:
                    if h1.val < h2.val: pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else: pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2

                # handle 各段之间的链接。
                while c1 > 0 or c2 > 0: pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            intv *= 2
        return res.next


        # 递归 归并排序   时间复杂度：O(NlogN) 空间复杂度：O(logN)
        if not head or not head.next: return head
        # 找到链表中点  归并排序
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # slow: 上一个链表的终点
        # mid: 下一个链表的起点
        mid, slow.next = slow.next, None
        # 归并排序 后序遍历
        right = self.sortList(mid)
        left = self.sortList(head)
        h = res = ListNode(0)
        while left and right:
            if left.val <= right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next
        h.next = left if left else right
        return res.next

