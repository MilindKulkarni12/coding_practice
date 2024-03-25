class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = defaultdict(bool)
        i = 0
        for num in nums:
            if d[num]:
                nums[i] = num
                i += 1
            d[num] = True
        
        return nums[:i]
        
