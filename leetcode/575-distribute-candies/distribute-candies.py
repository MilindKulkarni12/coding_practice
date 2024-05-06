class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        freq = Counter(candyType)
        n = len(candyType) // 2
        return n if len(freq) >= n else len(freq)
