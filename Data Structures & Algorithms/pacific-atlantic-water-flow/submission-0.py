class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        can_reach_pacific = set()
        can_reach_atlantic = set()
        m, n = len(heights), len(heights[0])
        def dfs(x: int, y: int, target_set: set(), visited: set(), prev_height: int):
            if x < 0 or y < 0 or x >= m or y >= n or (x, y) in visited or heights[x][y] < prev_height:
                return
            visited.add((x, y))
            target_set.add((x, y))
            dfs(x, y + 1, target_set, visited, heights[x][y])
            dfs(x, y - 1, target_set, visited, heights[x][y])
            dfs(x + 1, y, target_set, visited, heights[x][y])
            dfs(x - 1, y, target_set, visited, heights[x][y])

        visited = set()
        for i in range(m):
            dfs(i, 0 ,can_reach_pacific, visited, 0)
        for j in range(n):
            dfs(0, j ,can_reach_pacific, visited, 0)


        visited = set()
        for i in range(m):
            dfs(i, n - 1 ,can_reach_atlantic, visited, 0)
        for j in range(n):
            dfs(m - 1, j ,can_reach_atlantic, visited, 0)

        return list(can_reach_atlantic.intersection(can_reach_pacific))