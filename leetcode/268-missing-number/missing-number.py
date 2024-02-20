class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        found = [False]*(len(nums)+1)
        for i in nums:
            found[i] = True

        for i in range(len(nums)):
            if not found[i]:
                return i
        return len(nums)