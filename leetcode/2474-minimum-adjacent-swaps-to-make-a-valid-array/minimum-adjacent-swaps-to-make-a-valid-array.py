class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        elif n == 2:
            return 1 if nums[0] > nums[1] else 0
        
        mx = n - nums[::-1].index(max(nums)) - 1
        # print(mx, end=' ')
        
        
        mn = nums.index(min(nums))
        # mx = max(nums)
        # for i in range(n-1, -1, -1):
        #     if nums[i] == mx:
        #         mx = i
        #         break

        # print(mx)
        swaps = mn + n - mx - 1
        if mn > mx:
            swaps -= 1
        return swaps