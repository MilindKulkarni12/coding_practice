class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            distances.append(((x**2 + y**2), x, y))
        heapq.heapify(distances)
        ans = []
        while k > 0:
            d, x, y = heapq.heappop(distances)
            ans.append([x, y])
            k -= 1
        return ans