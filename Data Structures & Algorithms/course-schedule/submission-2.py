class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = {i : 0 for i in range(numCourses)}
        preqs = collections.defaultdict(list) # this is to keep track of like say i finish course 1 then to what all courses is course 1 a prerequisite to. like if i finish course 1 then what all courses get unlocked

        for course in prerequisites:
            indegrees[course[0]] += 1
            preqs[course[1]].append(course[0])

        q = collections.deque([c for c in indegrees if indegrees[c] == 0])

        count = 0
        while q:
            c = q.popleft()
            count += 1
            for pres in preqs[c]:
                indegrees[pres] -= 1
                if indegrees[pres] == 0:
                    q.append(pres)

        return count == numCourses