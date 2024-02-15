class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = 0, 1
        l = list(nums)
        i = 0
        while i < len(nums):
            if nums[i] >= 0:
                l[pos] = nums[i]
                pos += 2
            else:
                l[neg] = nums[i]
                neg += 2
            i += 1
        return l