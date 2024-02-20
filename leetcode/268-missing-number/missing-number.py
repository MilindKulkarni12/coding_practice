class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = -1
        for i in range(len(nums)+1):
            if i in nums:
                continue
            else:
                missing = i
                break
        return missing
