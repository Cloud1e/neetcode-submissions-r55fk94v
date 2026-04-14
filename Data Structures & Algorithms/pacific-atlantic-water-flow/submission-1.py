class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        can_reach_pacific = set()
        can_reach_atlantic = set()
        m, n = len(heights), len(heights[0])
        def dfs(x: int, y: int, target_set: set(),  prev_height: int):
            if x < 0 or y < 0 or x >= m or y >= n or (x, y) in target_set or heights[x][y] < prev_height:
                return
            target_set.add((x, y))
            dfs(x, y + 1, target_set, heights[x][y])
            dfs(x, y - 1, target_set, heights[x][y])
            dfs(x + 1, y, target_set, heights[x][y])
            dfs(x - 1, y, target_set, heights[x][y])

        def bfs(x: int, y: int, target_set: set()):
            q = deque()
            q.append(x, y)

            while q:
                x, y = q.popleft()
                for dir_x, dir_y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    next_x, next_y = x + dir_x, y + dir_y
                    if next_x < 0 or next_y < 0 or next_x >= m or next_y >= n or (next_x, next_y) in target_set or heights[next_x][next_y] > heights[x][y]:
                        continue
                    q.append((next_x, next_y))
                    target_set.add((next_x, next_y))
            
        for i in range(m):
            dfs(i, 0, can_reach_pacific, 0)
        for j in range(n):
            dfs(0, j, can_reach_pacific, 0)


        for i in range(m):
            dfs(i, n - 1 ,can_reach_atlantic, 0)
        for j in range(n):
            dfs(m - 1, j ,can_reach_atlantic, 0)

        return list(can_reach_atlantic.intersection(can_reach_pacific))