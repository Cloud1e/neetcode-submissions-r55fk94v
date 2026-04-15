import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # def partition(left, right):
        #     pivot_index = random.randint(left, right)
        #     pivot_value = nums[pivot_index]

        #     lt, gt, i = left, right, left
        #     while i <= gt:
        #         if nums[i] < pivot_value:
        #             nums[i], nums[lt] = nums[lt], nums[i]
        #             lt += 1
        #             i += 1
        #         elif nums[i] > pivot_value:
        #             nums[i], nums[gt] = nums[gt], nums[i]
        #             gt -= 1
        #         else:
        #             i += 1
        #     return lt, gt

        #     return store_index

        # def quickSelect(left, right):
        #     if left == right:
        #         return nums[left]
            
        #     target_index = n - k

        #     lt, gt = partition(left, right)

        #     if lt <= target_index <= gt:
        #         return nums[target_index]
        #     elif target_index > gt:
        #         return quickSelect(gt + 1, right)
        #     else:
        #         return quickSelect(left, lt - 1)


        # return quickSelect(0, n - 1)

        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]