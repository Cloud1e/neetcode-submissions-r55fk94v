class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = 1
        suffix_product = 1
        res = [1] * n
        for i in range(1, n):
            prefix_product *= nums[i - 1]
            res[i] = prefix_product

        print(res)
        for i in range(n - 2, -1, -1):
            suffix_product *= nums[i + 1]
            res[i] *= suffix_product
        return res