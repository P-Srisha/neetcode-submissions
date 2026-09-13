class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        tickets.sort()
        for u, v in tickets[::-1]:
            adj[u].append(v)

        res = []
        stack = ["JFK"]

        while stack:
            curr = stack[-1]
            if not adj[curr]:
                res.append(stack.pop())
            else:
                stack.append(adj[curr].pop())

        return res[::-1]