class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 二分查找，查找左右边界
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left)//2

            if nums[mid] == target:
                # 查左边界
                l, r = mid-1, mid+1
                while l >= left and nums[l] == target:
                    l -= 1
                # 查右边界
                while r <= right and nums[r] == target:
                    r += 1
                return [l+1, r-1]

            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        return [-1, -1]

