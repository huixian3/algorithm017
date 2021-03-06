

### 学习笔记

**面试时解题四个步骤：**
- 弄懂题目意思
- 想所有可能方法，并陈述
- 比较各种方法的时间和空间复杂度，找出最优的方案
- 写 + 测试

**题目练习方法：**
- 读题&思考，多条思路全部写下来；
- 不会的话，立马看题解；
    - 多读代码，尤其是优质代码；
- 记忆&自己写；
- 刷国际站题解（discuss），去掉-cn即可。

**加速核心思想：**
- 升维，利用附加信息（有序）
- 空间换时间

**刷题误区：**
- 只刷一遍

## 复杂度分析
该课程主要介绍复杂度的分析，分为空间复杂度和时间复杂度。
教学示例：climbing stairs

### 时间复杂度
- 评估的是代码运行的次数，对代码性能影响较大。
    - 表示：和n的关系，包括常数O(1)、线性O(n)、对数以及指数等等。

随着n增大，时间复杂度的变化：
![62a1496acb7e3c887810f330663e3bbc.png](evernotecid://19F582B4-8D95-4C07-A16B-4B46BF46857F/appyinxiangcom/11473862/ENResource/p526)

**Tips**
1. 关于递归的复杂度计算，可画出递归树；
2. 时间复杂度可通过主定理进行计算(master theorem）：
![0868cf6b85eb1625c1aa7c7169c1eef3.png](evernotecid://19F582B4-8D95-4C07-A16B-4B46BF46857F/appyinxiangcom/11473862/ENResource/p527)

    - 二叉树 O(n)
    - 图 O(n)
    - 搜索算法DFS、BFS O(logn)
    - 二分查找 O(n)
    
    
### 空间复杂度
1. 关于数组，一维数据复杂度 O(n);二维数组复杂度O(n^2);
2. 递归的空间复杂度为 递归树的深度最大值
3. 程序的总空间复杂度为 二者的最大值

### 问题 TODO
1 python 如何实现双指针

### 作业
1 分析 Queue 和 Priority Queue 的源码
- Queue：Interface
- Priority Queue：Queue的实现类
    - 底层数据结构 Array
