class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        # left_max_height: max (height[0:l])
        # right_max_height: max(height[r: ])
        left_max_height, right_max_height = height[0], height[n - 1]
        left, right = 0, n - 1
        while left < right:
            if left_max_height < right_max_height:
                left += 1
                res += max(0, left_max_height - height[left])
                left_max_height = max(left_max_height, height[left])
            else:
                right -= 1

                res += max(0, right_max_height - height[right])
                right_max_height = max(right_max_height, height[right])
        return res