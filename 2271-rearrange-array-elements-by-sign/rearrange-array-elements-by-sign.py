class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = 0
        neg = 0
        l = []
        turn = True
        while len(l) != len(nums):
            if turn:
                while nums[pos] < 0:
                    pos += 1
                l.append(nums[pos])
                pos += 1
                turn = False
            else:
                while nums[neg] >= 0:
                    neg += 1
                l.append(nums[neg])
                neg += 1
                turn = True
        return l