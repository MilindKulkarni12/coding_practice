class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # adj_list = defaultdict(list)
        # for f in flights:
        #     s, d, p = f[0], f[1], f[2]
        #     adj_list[s].append((d, p))
        # visited = {}
        # def dfs(curr, k, curr_price):
        #     if curr == dst and k >= 0:
        #         return curr_price
        #     if k == 0:
        #         return float(inf)
        #     if visited.get((curr, k), -1) != -1:
        #         return visited[(curr, k)]
            
        #     visited[(curr, k)] = min(dfs(d, k-1, curr_price + p) 
        #         for d, p in adj_list[curr]) if len(adj_list[curr]) > 0 else float(inf) 
        #     return visited[(curr, k)]
            
        # price = dfs(src, k+1, 0)
        # return -1 if price == float(inf) else price
        INF = float(inf)
        dist = [INF]*(n) 
        dist[src] = 0 # start location

        for i in range(k + 1):
            dist_copy = dist.copy()
            for f, t, p in flights:
                dist[t] = min(dist[t], dist_copy[f] + p)

        return dist[dst] if dist[dst] != INF else -1
