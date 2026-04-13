class MinStack:

    def __init__(self):
        self.st = []
        self.cur_min = float('inf')

    def push(self, val: int) -> None:
        if val < self.cur_min:
            self.cur_min = val
            self.st.append((val, val))
        else:
            self.st.append((val, self.cur_min))

    def pop(self) -> None:
        if not self.st:
            return
        self.st.pop()
        self.cur_min = self.st[-1][-1] if self.st else float('inf')

    def top(self) -> int:
        if not self.st:
            return -1
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.cur_min
