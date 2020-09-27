#!/usr/bin/python3
# coding=utf-8
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    # 两个链表循环遍历：逐个取两个链表中的最小的节点，赋值给新的节点
    res = ListNode()
    res.next = None
    p_head = res
    while l1 and l2:
        if l1.val <= l2.val:
            res.next = l1
            l1 = l1.next
            res = res.next
        elif l1.val > l2.val:
            res.next = l2
            l2 = l2.next
            res = res.next
    # 一句话，替代下面四行
    # res.next = l1==None? l2 : l1
    if l1 != None:
        res.next = l1
    elif l2 != None:
        res.next = l2
    return p_head.next

    # 递归：两个链表的合并 = minNode + 剩下两个链表的合并;时间复杂度=n
    # if l1 == None:
    #     return l2
    # if l2 == None:
    #     return l1
    # if l1.val <= l2.val:
    #     l3 = self.mergeTwoLists(l1.next, l2)
    #     l1.next = l3
    #     return l1
    # else:
    #     l3 = self.mergeTwoLists(l1, l2.next)
    #     l2.next = l3
    #     return l2