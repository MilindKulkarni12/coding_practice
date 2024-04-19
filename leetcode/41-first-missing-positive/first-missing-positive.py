class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # First pass: filter and restructure the array
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap the elements to their correct positions
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Second pass: find the first missing positive integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If no missing positive integer in the range [1, n]
        return n + 1
