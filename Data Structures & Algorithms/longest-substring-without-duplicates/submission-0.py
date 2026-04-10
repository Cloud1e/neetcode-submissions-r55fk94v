class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_to_last_seen_index = {}
        left, right = 0, 0
        n = len(s)
        max_length = 0
        while right < n:
            char = s[right]
            if char in char_to_last_seen_index and char_to_last_seen_index[char] >= left:
                left = char_to_last_seen_index[char] + 1
            char_to_last_seen_index[char] = right
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length
            