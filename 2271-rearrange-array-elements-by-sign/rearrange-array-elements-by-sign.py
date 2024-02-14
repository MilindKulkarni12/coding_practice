class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = 0
        neg = 0
        l = []
        turn = True
        while len(l) != len(nums):
            if turn and nums[pos] >= 0:
                l.append(nums[pos])
                pos += 1
                turn = False
            elif turn and nums[pos] < 0:
                pos += 1
            elif not turn and nums[neg] < 0:
                l.append(nums[neg])
                neg += 1
                turn = True
            else:
                neg += 1
        return l