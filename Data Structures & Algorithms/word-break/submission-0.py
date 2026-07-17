class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        word_set = set(word_dict)
        for i in range(1, n + 1):
            for j in range(0, i):
                if dp[j] and s[j : i] in word_set:
                    dp[i] = True
                    break

        return dp[n]