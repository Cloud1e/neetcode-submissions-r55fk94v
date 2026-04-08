class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n - 1
        res = 0
        while left < right:
            left_height, right_height = heights[left], heights[right]
            if left_height < right_height:
                area = (right - left) * left_height
                left += 1
            else:
                area = (right - left) * right_height
                right -= 1

            res = max(area, res)
        return res