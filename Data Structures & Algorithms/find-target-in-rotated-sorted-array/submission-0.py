class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                # left part is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            
            else:
                # right part is sorted
                if nums[mid] < target <= nums[right - 1]:
                    left = mid + 1
                else:
                    right = mid
        return -1