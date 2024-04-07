class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        zeros = [0]*n 
        zeros[0] = 1 if nums[0] == 0 else 0
        for i in range(1, n):
            if nums[i] == 0:
                zeros[i] = zeros[i-1] + 1
        # print(zeros)
        return sum(zeros)
