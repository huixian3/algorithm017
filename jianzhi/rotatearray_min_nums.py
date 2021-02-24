class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        # 旋转数组的最小数字
        # 二分查找
        if not numbers:
            return -1
        l, r = 0, len(numbers)-1
        while l < r:
            mid = (l + r) / 2
            if numbers[mid] < numbers[r]:
                r = mid
            elif numbers[mid] > numbers[r]:
                l = mid+1
            else:
                r = r-1
        return numbers[l]