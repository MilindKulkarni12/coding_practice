class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal_matrix = [1, 1]
        if rowIndex < 2:
            return pascal_matrix[:rowIndex+1]
        
        for i in range(2,rowIndex+1):
            row=[1] + [pascal_matrix[j] + pascal_matrix[j+1] for j in range(i-1)] + [1]
            pascal_matrix = row
        
        return pascal_matrix
        