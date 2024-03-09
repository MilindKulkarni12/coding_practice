class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        max_c = 0
        n = len(citations)
        
        # 0 1 3 5 6
        for i, c in enumerate(citations):
            if n - i >= c:
                max_c = c
            else:
                max_c = max(max_c, n - i)
        return max_c
