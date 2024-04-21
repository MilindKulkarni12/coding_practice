class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        adj_list = defaultdict(list)

        for s, d in edges:
            adj_list[s].append(d)        
            adj_list[d].append(s)        

        q = deque([source])
        vis = set([source])

        while q:
            curr = q.popleft()
            if curr == destination:
                return True
            for nei in adj_list[curr]:
                if nei not in vis:
                    q.append(nei)
                    vis.add(nei)
        return False
