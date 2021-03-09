'''
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 优先队列： 链表内元素排序，之后构造node及其关系
        # heapq 模块可以接受元组对象，默认元组的第一个元素作为priority，即按照元组的第一个元素构成小根堆
        if not lists: return None
        nodelist = []
        n = len(lists)
        for i in range(n):
            if lists[i]:
                heapq.heappush(nodelist, (lists[i].val, i))
                lists[i] = lists[i].next
        dummy = res = ListNode(0)
        while nodelist:
            val, index = heapq.heappop(nodelist)
            res.next = ListNode(val)
            res = res.next
            # 加入下一个节点
            if lists[index]:
                heapq.heappush(nodelist, (lists[index].val, index))
                lists[index] = lists[index].next
        return dummy.next

        # 分治合并两个链表，时间复杂度=O(kn×logk)、空间复杂度=O(logk) 栈空间
        def merge_devide(start, end): # 归并，并返回 merge 后头节点
            if start >= end: return lists[start]
            mid = (start + end) >> 1
            left = merge_devide(start, mid)
            right = merge_devide(mid+1, end)
            # print(left)
            # print(right)
            head = res = ListNode(0)
            while left and right:
                if left.val < right.val: res.next, left = left, left.next
                else: res.next, right = right, right.next
                res = res.next
            res.next = left if left else right
            # print(head)
            return head.next

        if not lists: return None
        n = len(lists)
        return merge_devide(0, n-1)




