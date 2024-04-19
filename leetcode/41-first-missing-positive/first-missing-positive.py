class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        found = [False]*len(nums)
        n = len(nums)

        for num in nums:
            if 0 < num <= n:
                found[num-1] = True
        # print(found)
        for i, f in enumerate(found):
            if not f:
                return i+1
        return n+1