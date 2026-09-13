class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)

        for u, v in sorted(tickets)[::-1]:
            adj[u].append(v)

        res = []
        def dfs(node):
            while adj[node]:
                next_node = adj[node].pop()
                dfs(next_node)
            res.append(node)
            
        dfs("JFK")
        return res[::-1]