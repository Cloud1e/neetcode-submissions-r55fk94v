class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len_s, len_t = len(s), len(t)
        if len_s < len_t:
            return ""
        target_counter = Counter(t)
        window_counter = Counter()

        matches = 0
        min_len = float('inf')
        res = ''
        left = 0
        for right in range(len_s):
            window_counter[s[right]] += 1
            if window_counter[s[right]] == target_counter[s[right]]:
                matches += 1
            while matches == len(target_counter) and left <= right:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left: right + 1]
                window_counter[s[left]] -= 1
                if window_counter[s[left]] == target_counter[s[left]] - 1:
                    matches -= 1
                left += 1
        return res