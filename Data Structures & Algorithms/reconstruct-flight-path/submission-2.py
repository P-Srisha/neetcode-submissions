class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        out = collections.defaultdict(int)
        adj = collections.defaultdict(list)

        for u, v in sorted(tickets)[::-1]:
            out[u] += 1
            adj[u].append(v)

        res = []
        def dfs(node):
            while out[node] != 0:
                out[node] -= 1
                next_node = adj[node][out[node]]
                dfs(next_node)
            res.append(node)
            
        dfs("JFK")
        return res[::-1]