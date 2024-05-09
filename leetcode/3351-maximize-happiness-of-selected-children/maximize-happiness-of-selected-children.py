class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans = 0
        i = 0
        happiness = [-h for h in happiness]
        heapq.heapify(happiness)
        while i < k:
            curr = -heapq.heappop(happiness)
            # print(curr)
            if curr - i <= 0:
                return ans
            ans += curr - i
            i += 1
        return ans
