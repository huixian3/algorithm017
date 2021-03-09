class Solution:
    '''
    Q：给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
    要求返回这个链表的 深拷贝。
    '''
    '''
    思路：
    '''
    def copyRandomList(self, head):
        if not head:
            return None
        p = head

        # 在每个节点后面copy一个新节点
        while p:
            new_node = Node(p.val)
            new_node.next = p.next
            p.next = new_node
            p = new_node.next

        # 设置新节点的随机节点
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next # 新的random 也是新节点
            p = p.next.next

        dummy = Node(-1)
        cur = dummy
        # 抽离出新节点，原链表保持不变
        p = head
        while p:
            cur.next = p.next
            cur = p.next
            p.next = cur.next
            p = p.next
        return dummy.next
