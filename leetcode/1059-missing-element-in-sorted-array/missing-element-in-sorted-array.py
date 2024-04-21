class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        missing = -1
        prev = nums[0] - 1
        i = 0
        while k > 0:
            if i < len(nums) and nums[i] - prev != 1:
                prev += 1
                missing = prev
                k -= 1
            elif i == len(nums):
                prev += k
                return prev
            else:
                prev = nums[i]
                i += 1
        # print(missing)
        return missing
