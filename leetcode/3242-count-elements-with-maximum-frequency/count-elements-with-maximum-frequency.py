class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        return sum([v for v in freq.values() if v == max(freq.values())])
        # c = 0
        # for v in freq.values():
        #     if v == max_freq:
        #         c += v
        # return c
