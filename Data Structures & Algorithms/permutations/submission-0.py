class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = []
        res = []
        used = [False] * n

        def backtracking():
            if len(path) == n:
                res.append(list(path))
                return
            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtracking()
                path.pop()
                used[i] = False
        backtracking()
        return res