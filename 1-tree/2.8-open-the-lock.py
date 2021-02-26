class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        # BFS N叉树层次遍历
        # 1. 终止
        # 2. 可尝试迭代的点
        queue = collections.deque()
        queue.append('0000')
        level = 0
        # 操作函数
        def up(node, i):
            node1 = list(node)
            print(node1)
            if node1[i] == '9': node1[i] = '0'
            else: node1[i] = chr(ord(node1[i]) + 1)
            return ''.join(node1)
        def down(node, i):
            node1 = list(node)
            if node1[i] == '0': node1[i] ='9'
            else: node1[i] = chr(ord(node1[i]) - 1)
            print(node1)
            return ''.join(node1)
        #
        while queue:
            #
            size = len(queue)
            level += 1
            for _ in range(size):
                node = queue.popleft()
                deadends.append(node)
                for i in range(len(node)):
                    node_up = up(node, i)
                    node_down = down(node, i)
                    # 终止条件
                    if node_up == target or node_down == target: return level
                    # 记录下一层的节点
                    if node_down not in deadends: queue.append(node_down)
                    if node_up not in deadends: queue.append(node_up)
        return -1
# 优
class Solution(object):
    def openLock(self, deadends, target):
        def neighbors(node):
            for i in xrange(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]

        dead = set(deadends)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target: return depth
            if node in dead: continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1








