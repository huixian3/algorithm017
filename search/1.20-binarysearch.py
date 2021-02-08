
class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left <= right:
            middle = left + (right-left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return -1

        # 下面递归解法有误，返回 None
        # def partition(arr, left, right):
        #     if left > right:
        #         return -1
        #     middle = (right + left) // 2
        #     if arr[middle] > target:
        #         partition(arr, left, middle-1)
        #     elif arr[middle] < target:
        #         partition(arr, middle+1, right)
        #     else:
        #         return middle
        #
        # l = partition(nums, 0, len(nums)-1)
        # return l
print(Solution().search([0,2,3,4,5,6], 0))