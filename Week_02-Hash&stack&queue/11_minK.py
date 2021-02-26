#!/usr/bin/python3
# coding=utf-8
# from collections \
import heapq
def getLeastNumbers(arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: List[int]
    """
    if arr == None or len(arr) <= k:
        return arr
    if k == 0:
        return list()
    # 87% sort
    # arr.sort()
    # return arr[:k]

    # 45% 堆
    # 1. 建堆k个大小，大顶堆，遇到小于顶部元素的堆，替换，将小的元素放到堆顶，然后往下移
    # python heapq为小顶堆，所以将数组元素先取负，之后再建堆
    hp = [-x for x in arr[:k]]
    heapq.heapify(hp)
    for e in arr[k:]:
        if -hp[0] > e:
            heapq.heappop(hp)
            heapq.heappush(hp, -e)
    res = [-x for x in hp]
    return res


    # 11% 2. 小顶堆，全部push，之后逐个取出。
    heapq.heapify(arr)
    res = []
    for i in range(k):
        res.append(heapq.heappop(arr))
    return res

print(getLeastNumbers([0,0,1,2,4,2,2,3,1,4], 8))