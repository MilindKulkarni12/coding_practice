class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        freq = Counter(candyType)
        n = len(candyType)
        
        unique = 0
        for k, v in freq.items():
            if v < 2:
                unique += 1
        
        if len(freq) >= (n // 2):
            return n // 2
        
        return len(freq) 
