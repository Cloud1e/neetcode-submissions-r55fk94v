class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        s1_counter = [0] * 26
        s2_counter = [0] * 26
        for i in range(n1):
            s1_counter[ord(s1[i]) - ord('a')] += 1
        left = 0
        matches = 0

        for right in range(n2):

            # add right char in window
            right_char_index = ord(s2[right]) - ord('a')
            s2_counter[right_char_index] += 1

            if right - left + 1 > n1:
                left_char_index = ord(s2[left]) - ord('a')
                s2_counter[left_char_index] -= 1
                left += 1
            if right - left + 1 == n1 and s2_counter == s1_counter:
                return True
        return False
