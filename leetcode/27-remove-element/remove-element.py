class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if val > 50:
            return n
        for i in range(n):
            if nums[i] == val:
                nums[i] = 51
        nums.sort()
        return n - nums.count(51)
