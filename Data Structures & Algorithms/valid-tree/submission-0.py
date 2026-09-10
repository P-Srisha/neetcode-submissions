class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        edgeMap = {i : [] for i in range(n)}
        
        for u, v in edges:
            edgeMap[u].append(v)
            edgeMap[v].append(u)

        def dfs(current, parent):
            if current in visit:
                return False

            visit.add(current)

            for nei in edgeMap[current]:
                if nei == parent:
                    continue
                if not dfs(nei, current):
                    return False
            
            return True
            # visit.remove(current)

        if not dfs(0, -1):
            return False

        return len(visit) == n