class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        def dfs(x: int, y: int) -> None:
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] != '1':
                return
            grid[x][y] = '-1'
            dfs(x, y + 1)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x - 1, y)

        def bfs(x: int, y: int) -> None:
            q = deque()
            q.append((x, y))
            while q:
                cur_x, cur_y = q.pop()
                grid[cur_x][cur_y] = '-1'
                for dir_x, dir_y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    next_x, next_y = cur_x + dir_x, cur_y + dir_y
                    if next_x < 0 or next_y < 0 or next_x >= m or next_y >= n or grid[next_x][next_y] != '1':
                        continue
                    q.append((next_x, next_y))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    # dfs(i, j)
                    bfs(i, j)
        return res