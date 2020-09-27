#!/usr/bin/python3
# coding=utf-8

def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # 暴力枚举，两层嵌套循环，遍历数据nums，返回target index
    # hash表存储
    # 双指针，以左指针为依据循环

    if nums == None:
        return None
    # 暴力枚举
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]


    # hash表

    # hash_set = {}
    # for i in range(len(nums)):
    #     if hash_set.get(target - nums[i]) is not None:
    #
    #         return [hash_set.get(target-nums[i]),i]
    #     hash_set[nums[i]]=i

