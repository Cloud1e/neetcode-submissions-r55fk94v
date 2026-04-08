class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n - 1
        while left < right:
            if target - numbers[left] == numbers[right]:
                return [left + 1, right + 1]
            elif target - numbers[left] < numbers[right]:
                right -= 1
            else:
                left += 1
        return [-1, -1]