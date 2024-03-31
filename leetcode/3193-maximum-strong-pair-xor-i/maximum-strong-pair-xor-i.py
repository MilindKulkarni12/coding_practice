class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        left = 0
        right = 1
        ans = 0
        
        while right < n:
            x = nums[left]
            y = nums[right]
        
            if abs(x - y) <= min(x, y):
                ans = max(ans, x ^ y)

            right += 1
            if right == n:
                left += 1
                right = left + 1
        return ans

