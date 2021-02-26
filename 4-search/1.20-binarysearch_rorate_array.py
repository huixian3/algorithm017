
class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left <= right:
            middle = left + (right-left) // 2
            if nums[middle] == target:
                return middle
            if nums[left] <= nums[middle]:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1


print(Solution().search([5,6,0,2,3,4], 0))