class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = 1
        suffix_product = 1
        res = [1] * n
        for i in range(n):
            res[i] = prefix_product
            prefix_product *= nums[i]
        print(res)
        for i in range(n - 1, -1, -1):
            res[i] *= suffix_product
            suffix_product *= nums[i]
        return res