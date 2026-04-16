class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj={i:[] for i in range(numCourses)}
        indegree={i:0 for i in range(numCourses)}
        for course,pre in prerequisites:
            adj[pre].append(course)
            indegree[course]+=1
        q=deque()
        for ind in indegree:
            if indegree[ind]==0:
                q.append(ind)
        
        visited=[]

        while(q):
            course=q.popleft()
            visited.append(course)

            for nei in adj[course]:

                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        
        if len(visited)==numCourses:
            return visited
        return []
