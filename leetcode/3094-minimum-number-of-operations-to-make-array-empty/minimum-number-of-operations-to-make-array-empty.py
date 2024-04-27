class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nc = Counter(nums)
        if 1 in nc.values():
            return -1
        
        res = 0
        for i in nc.values():
            if i % 3 == 0:
                res += int(i/3)
            else:
                res += (1 + int(i/3))
        return res
