class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        count = 0
        time = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                if grid[i][j] == 1:
                    count += 1
        
        while q:
            x, y, cur_time = q.popleft()
            time = max(time, cur_time)
            for dir_x, dir_y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                next_x, next_y = x + dir_x, y + dir_y
                if next_x < 0 or next_y < 0 or next_x >= m or next_y >= n or grid[next_x][next_y] != 1:
                    continue
                q.append((next_x, next_y, cur_time + 1))
                grid[next_x][next_y] = 2
                count -= 1
        return time if count == 0 else -1
