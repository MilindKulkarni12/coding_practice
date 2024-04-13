class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def get_max_area(histogram):
            n = len(histogram)
            stack = []
            mx_area = 0
            for i, h in enumerate(histogram):
                start = i
                while stack and stack[-1][1] > h:
                    idx, top_h = stack.pop()
                    mx_area = max(mx_area, top_h * (i - idx))
                    start = idx
                stack.append((start, h))
            
            for i, h in stack:
                mx_area = max(mx_area, h * (n - i))
            
            return mx_area


        rows = len(matrix)
        cols = len(matrix[0])

        histogram = [0]*cols
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    histogram[j] += 1
                else:
                    histogram[j] = 0

            max_area = max(max_area, get_max_area(histogram))
        return max_area
