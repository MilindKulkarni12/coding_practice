class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        size = len(original)
        if size != m * n:
            return []
        
        mat = [ 0 for _ in range(m)]
        j = 0
        for i in range(0, size, n):
            mat[j] = original[i: i + n]
            j += 1

        return mat
