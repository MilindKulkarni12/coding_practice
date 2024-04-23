class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heavy_stones = [-s for s in stones]
        heapq.heapify(heavy_stones)

        while len(heavy_stones) > 1:
            y = heapq.heappop(heavy_stones)
            x = heapq.heappop(heavy_stones)
            
            if x != y:
                z = -y - (-x)
                heapq.heappush(heavy_stones, -z)
            
        return -heavy_stones[0] if heavy_stones else 0


