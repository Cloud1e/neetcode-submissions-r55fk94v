class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num, freq in counter.items():
            buckets[freq].append(num)
        res = []
        for freq in range(n, -1, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
            
        return res