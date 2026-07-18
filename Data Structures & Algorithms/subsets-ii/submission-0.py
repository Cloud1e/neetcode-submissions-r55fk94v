class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort()
        def backtrack(start_index: int) -> None:
            res.append(path[:])
            for i in range(start_index, len(nums)):
                if i > start_index and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
        
        backtrack(0)
        return res
