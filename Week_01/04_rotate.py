#!/usr/bin/python3
# coding=utf-8

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 利用数据反转，反转三次
        def reverse(nums, i, j):
            while i < j:
                nums[j], nums[i] = nums[i], nums[j]
                i = i+1
                j = j-1
        length = len(nums)
        k = k % length
        if length < 2 or k <=0:
            return nums
        reverse(nums, 0, length-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, length-1)
        # 环形移动，直接将元素移动n个位置，首先移动n%k=0 之后n%k=1



        # 超出时间限制   移动n次 递归，移动n次 = 移动n-1次 + 移动1次
        # length = len(nums)
        # if length < 2:
        #     return nums
        # else:
        #     for i in range(k):
        #         temp = nums[-1]
        #         nums[1:] = nums[0:length-1]
        #         nums[0] = temp
        # return nums



        # 超出时间限制
        # if k == 0 or nums == None:
        #     return nums
        # value_last = nums[-1]
        # length = len(nums)
        # for j in range(1, length):
        #     nums[length -j] = nums[length -j -1]
        # nums[0] = value_last
        # self.rotate(nums, k-1)
        # return nums


