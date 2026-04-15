class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegrees = [0] * numCourses
        for course, pre_course in prerequisites:
            graph[pre_course].append(course)
            indegrees[course] += 1
        
        q = deque(i for i in range(numCourses) if indegrees[i] == 0)
        res = []
        while q:
            cur_course = q.popleft()
            res.append(cur_course)
            for next_course in graph[cur_course]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    q.append(next_course)
        return res if len(res) == numCourses else []
            
        

        