class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        lookup = defaultdict(bool)
        max_num = -1
        for n in nums:
            if n > 0:
                if lookup[-n] and n > max_num:
                    max_num = n
                else:
                    lookup[n] = True
            else:
                if lookup[abs(n)] and abs(n) > max_num:
                    max_num = abs(n)
                else:
                    lookup[n] = True
        return max_num
