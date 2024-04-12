class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        mx_left = height[left]
        mx_right = height[right]
        water = 0
        while left < right:
            if height[left] <= height[right]:
                left += 1
                mx_left = max(mx_left, height[left])
                water += mx_left - height[left]
            else:
                right -= 1
                mx_right = max(mx_right, height[right])
                water += mx_right - height[right]
        return water
