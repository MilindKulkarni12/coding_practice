class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        mx = max(nums)
        ops = 0
        while mx != 0:
            mn = 101
            for num in nums:
                if num > 0:
                    mn = min(mn, num)
            nums = [x - mn for x in nums if x > 0]
            # print(mn, nums)
            mx = mx - mn
            ops += 1
        return ops
