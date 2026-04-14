class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = deque()
        INF = pow(2, 31) - 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        
        while q:
            x, y, cur_steps = q.popleft()
            for dir_x, dir_y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                next_x, next_y = x + dir_x, y + dir_y
                if next_x < 0 or next_y < 0 or next_x >= m or next_y >= n or grid[next_x][next_y] != INF:
                    continue
                q.append((next_x, next_y, cur_steps + 1))
                grid[next_x][next_y] = cur_steps + 1
        
        