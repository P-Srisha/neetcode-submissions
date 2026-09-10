class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = {i : 0 for i in range(numCourses)}
        pres = {i : [] for i in range(numCourses)}

        for c, pre in prerequisites:
            indegrees[c] += 1
            pres[pre].append(c)

        q = collections.deque([c for c in indegrees if indegrees[c] == 0])
        print(q)

        res = []
        while q:
            crs = q.popleft()
            res.append(crs)

            for pre in pres[crs]:
                indegrees[pre] -= 1
                if indegrees[pre] == 0:
                    q.append(pre)

        return res if len(res) == numCourses else []