# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # 输入: 1->2->3->3->4->4->5
    # 输出: 1->2->5
    '''

    '''
    '''
    思路：考虑 next 和 next.next 是否重复，重复的节点循环遍历去除
    '''
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        cur = dummy
        while cur and cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                temp = cur.next
                while temp and temp.next and temp.val == temp.next.val:
                    temp = temp.next
                cur.next = temp.next
                #此时不移动cur结点！！
            else:
                cur = cur.next
        return dummy.next
