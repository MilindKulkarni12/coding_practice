class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        curr_len = prev_len = max_len = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                max_len = max(max_len, curr_len + prev_len)
                prev_len = curr_len
                curr_len = 0
            else:
                curr_len += 1
        if curr_len == len(nums):
            return curr_len - 1
        return max(max_len, curr_len + prev_len)
