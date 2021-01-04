class Solution:
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
                p.next.random = p.random.next
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
