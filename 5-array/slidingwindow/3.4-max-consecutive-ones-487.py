def findMaxConsecutiveOnes(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #滑动窗口法
    l, r = 0, 0
    num0 = 0 #记录窗口中0的个数
    res = 0
    while r < len(nums):
        ch = nums[r]
        if ch == '0': num0 += 1
        r += 1
        while num0 > 1:
            if nums[l] == 0:
                num0 -= 1
            r += 1
        res = max(res, r-l)
    return res




    # while q < len(nums):
    #     if nums[q] == 0:
    #         num0 += 1
    #     q += 1
    #     while num0 > 1:
    #         if nums[p] == 0:
    #             num0 -= 1
    #         p += 1
    #     res = max(res, q-p)
    # return res
