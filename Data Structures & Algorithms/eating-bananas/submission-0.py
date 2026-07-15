class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles) + 1
        res = right
        def hours_needed(speed):
            return sum((pile + speed - 1) // speed for pile in piles)
        while left < right:
            mid = left + (right - left) // 2
            if hours_needed(mid) > h:
                left = mid + 1
            else:
                res = mid
                right = mid
        return res