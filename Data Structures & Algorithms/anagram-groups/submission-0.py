class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_to_strs = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            counter_to_strs[str(count)].append(s)
        return list(counter_to_strs.values())
