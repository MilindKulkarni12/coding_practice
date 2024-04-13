class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, top_h = stack.pop()
                max_area = max(max_area, top_h * (i - idx))
                start = idx

            stack.append((start, h))
        n = len(heights)
        for i, h in stack:
            max_area = max(max_area, h * (n - i))

        return max_area
