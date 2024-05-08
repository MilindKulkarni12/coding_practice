class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        n = len(scores)
        pos = {scores[i]: i for i in range(n)}
        pos = sorted(pos.items(), key=lambda x: x[0], reverse=True)
        # print(pos)
        ans = [0] * n
        for i, val in enumerate(pos):
            s, p = val
            if i > 2:
                ans[p] = str(i+1)
            elif i == 0:
                ans[p] = 'Gold Medal'
            elif i == 1:
                ans[p] = 'Silver Medal'
            else:
                ans[p] = 'Bronze Medal'
                
        return ans
