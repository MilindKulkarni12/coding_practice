class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # return sorted([i**2 for i in nums])
        numsq = list(nums)
        s, e = 0, len(nums) - 1
        i = len(nums) - 1
        while i >= 0:
            if abs(nums[s]) <= abs(nums[e]):
                numsq[i] = nums[e]**2
                e -= 1
            else:
                numsq[i] = nums[s]**2
                s += 1
            i -= 1
        return numsq
