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

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res