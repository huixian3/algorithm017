class Solution(object):
    def exchange(self, array):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 双指针 快慢指针
        if not array:
            return array
        n = len(array)
        i, j = 0, 0
        while j < n:
            # 基数，需考虑将元素移到i所在位置，之后快慢指针都移动
            if array[j] & 1 == 1:
                temp = array[j]
                k = j
                while i < k:
                    array[k] = array[k-1]
                    k -= 1
                array[i] = temp
                i, j = i+1, j+1
                # 偶数，则快指针后移一位
            elif array[j] & 1 == 0:
                j += 1
        return array