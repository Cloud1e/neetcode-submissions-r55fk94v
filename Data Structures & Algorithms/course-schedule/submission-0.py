class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        graph = defaultdict(list)
        indegrees = [0] * n
        count = 0
        for course, preCourse in prerequisites:
            graph[preCourse].append(course)
            indegrees[course] += 1
        q = deque()
        for i in range(n):
            if indegrees[i] == 0:
                q.append(i)

        while q:
            u = q.popleft()
            count += 1
            for v in graph[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    q.append(v)
        return count == numCourses