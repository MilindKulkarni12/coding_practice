class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = float(-inf)
        s = sum(nums[0: k])
        max_sum = s
        for i in range(k, len(nums)):
            s -= nums[i-k]
            s += nums[i]
            max_sum = max(s, max_sum)
        return max_sum / k
