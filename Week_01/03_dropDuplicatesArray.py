#!/usr/bin/python3
# coding=utf-8

class Solution(object):
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[j]:
                if i-j >1:
                    nums[j+1] = nums[i]
                j = j+1
        return j+1


print(Solution.removeDuplicates([1,1,2,3,4]))
