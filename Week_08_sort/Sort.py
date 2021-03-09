#!/usr/bin/python3
# coding=utf-8
import heapq
# 选择排序
class Choice(object):
    def sort(self, a):
        '''
        :param a: int[]
        :return: int[]
        '''

        for i in range(len(a)):
            min, index = a[i], i
            for j in range(i+1, len(a)):
                if min > a[j]:
                    min, index = a[j], j
            if i != index:
                a[i], a[index] = a[index], a[i]
        return a

class HeapSort(object):
    def sort(self, a):
        '''
        :param a: int[]
        :return: int[]
        '''
        heapq.heapify(a)
        return [heapq.heappop(a) for i in range(len(a)) ]
# 交换排序
class Maopao(object):
    def sort(self, a):
        '''
        :param a: int[]
        :return: int[]
        '''
        for i in range(len(a)-1):
            for j in range(len(a) - i - 1):
                if a[j] > a[j+1]:
                    a[j+1], a[j] = a[j], a[j+1]
        return a

class RapidSort(object):

    # 前序遍历
    def rapid(self, a, begin, end):
        if begin >= end:
            return
        pivot = self.partition(a, begin, end)
        self.rapid(a, begin, pivot-1)
        self.rapid(a, pivot+1, end)

    def partition(self, a, begin, end):
        pivot = end
        counter = begin
        for i in range(begin, end):
            if a[i] < a[pivot]:
                a[counter], a[i] = a[i], a[counter]
                counter += 1
        a[counter], a[pivot] = a[pivot], a[counter]
        return counter

    def sort(self, a):
        '''
        :param a: int[]
        :return: int[]
        '''
        self.rapid(a, 0, len(a)-1)
        return a



# # 插入排序
class Insert(object):
    def sort(self, a):
        '''
        :param a: int[]
        :return: int[]
        '''
        if len(a) <= 1:
            return a
        for i in range(1, len(a)):
            j = i-1
            key = a[i]
            while j >= 0 and a[j] > key:
                a[j+1] = a[j]
                j -= 1
            a[j+1] = key

        return a

# # 归并排序  -> 后序遍历
class Merge(object):
    def sort(self, a):
        '''
        :param a: int[]
        :return: int[]
        '''
        # 思想，分治
        self.merge_sort(a, 0, len(a)-1)
        return a

    def merge(self, a, begin, mid, end):
        temp = []
        i= begin
        j = mid+1
        while i <= mid and j <= end:
            if a[i] <= a[j]:
                temp.append(a[i])
                i += 1
            else:
                temp.append(a[j])
                j += 1
        if i <= mid:
            temp.extend(a[i:mid+1])
        if j <= end:
            temp.extend(a[j:end+1])
        for p in range(len(temp)):
            a[begin + p] = temp[p]

    def merge_sort(self, a, begin, end):
        if begin >= end:
            return
        mid = (begin + end) >> 1
        self.merge_sort(a, begin, mid)
        self.merge_sort(a, mid+1, end)
        self.merge(a, begin, mid, end)

#



a = [3,42,12,3,4,1,-1,3,7,4]
print(RapidSort().sort(a))



