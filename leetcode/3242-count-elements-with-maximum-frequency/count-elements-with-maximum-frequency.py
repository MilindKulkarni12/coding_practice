class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = max(freq.values())
        c = 0
        for v in freq.values():
            if v == max_freq:
                c += v
        return c
