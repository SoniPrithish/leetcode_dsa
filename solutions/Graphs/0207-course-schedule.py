class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dep={i:0 for i in range(numCourses)}
        adj = {i: [] for i in range(numCourses)}
        visited=set()
        for course, pre in prerequisites:
            adj[pre].append(course)
            dep[course] += 1
        q=deque()
        for vertex in dep:
            if dep[vertex]==0:
                q.append(vertex)
        
        while(q):
            curr=q.popleft()
            visited.add(curr)
            for  nei in adj[curr]:
                dep[nei]-=1
                if dep[nei]==0:
                    q.append(nei)
        return len(visited)==numCourses
