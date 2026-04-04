class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = Counter()
        for c in s:
            counter[c] += 1
        for c in t:
            counter[c] -= 1
            if counter[c] < 0:
                return False
        return True