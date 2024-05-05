class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        paths = []
        adj_list = defaultdict(list)
        heapq.heappush(paths, (0, k, k))
        for s, e, w in times:
            adj_list[s].append((e, w))

        # print(adj_list)
        vis = set()
        total_time = 0
        time_dict = defaultdict(int)
        
        while paths and len(vis) < n:
            # print(paths)
            curr_time, src, end = heapq.heappop(paths)
            total_time = curr_time
            if end in vis:
                continue

            vis.add(end)
            time_dict[src] = max(time_dict[src], curr_time)
            
            # print(time_dict)
            for nxt, wt in adj_list[end]:
                if nxt not in vis:
                    heapq.heappush(paths, (total_time + wt, end, nxt))
        
        return total_time if len(vis) == n else -1

        """
            1 -- 2
            |  /
            | /
            3
        """
