class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = {i : 0 for i in range(numCourses)}
        preqs = collections.defaultdict(list)

        def getInDegrees():
            for course in prerequisites:
                indegrees[course[0]] += 1
                preqs[course[1]].append(course[0])
        
        getInDegrees()

        q = collections.deque([c for c in indegrees if indegrees[c] == 0])

        if not q:
            return False

        count = 0
        while q:
            c = q.popleft()
            count += 1
            for pres in preqs[c]:
                indegrees[pres] -= 1
                if indegrees[pres] == 0:
                    q.append(pres)

        return count == numCourses