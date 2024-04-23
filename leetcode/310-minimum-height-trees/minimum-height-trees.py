class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for v1, v2 in edges:
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)

        leaves = deque()
        node_count = {}
        for v, nei in adj_list.items():
            edge_count = len(nei)
            if edge_count == 1:
                leaves.append(v)
            node_count[v] = edge_count
        
        while leaves:
            if n <= 2:
                return list(leaves)
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                n -= 1
                for nei in adj_list[leaf]:
                    node_count[nei] -= 1
                    if node_count[nei] == 1:
                        leaves.append(nei)
        return [0]
