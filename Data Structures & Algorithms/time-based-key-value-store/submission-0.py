class TimeMap:

    def __init__(self):
       self.history = defaultdict(list) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.history[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        left, right = 0, len(self.history[key])
        res = ''
        while left < right:
            mid = left + (right - left) // 2
            if self.history[key][mid][0] <= timestamp:
                res = self.history[key][mid][1]
                left = mid + 1
            else:
                right = mid
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)