class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pair = defaultdict(bool)
        pair_count = 0
        n = len(nums)
        for num in nums:
            if pair.get(num, False):
                pair[num] = False
                pair_count += 1
            else:
                pair[num] = True
        return [pair_count, n - 2*pair_count]
