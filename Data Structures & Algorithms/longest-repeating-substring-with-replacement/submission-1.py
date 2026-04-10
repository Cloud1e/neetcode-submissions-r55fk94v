class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        right = 0
        history_max_freq = 0
        counter = Counter()
        while right < n:
            counter[s[right]] += 1
            history_max_freq = max(history_max_freq, counter[s[right]])
            if right - left + 1 > history_max_freq + k:
                counter[s[left]] -= 1
                left += 1
            right += 1
        return right - left
