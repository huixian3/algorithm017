学习笔记
## 散点记录
####  HashMap总结
查找 & 删除 时间复杂度O(1)

####  python
collections等用法：https://docs.python.org/zh-cn/3/library/collections.html
d=collections.deque() #
    - d.append
    - d.appendleft
    - d.pop
    - d.popleft
res = collections.defaultdict(list) #初始化value为list的字段

#### 堆
1. 底层数据结构？
2. 堆操作复杂度？

python： 
    - 最小堆 heapq，查找&删除时间复杂度 = log(n)
    - 底层操作数据结构=列表，但是元素顺序较重要
C++：大顶堆 priority_queue
#### 算法
堆排序：https://www.geeksforgeeks.org/heap-sort/

## 总结
弱点：堆 & 队列，使用方法


## TODO
1. 树，BFS 和 DFS遍历
    - BFS： 队列
    - DFS： 栈
2. 排序的复杂度为什么是 nlog(n)；
    貌似快排的复杂度不是

