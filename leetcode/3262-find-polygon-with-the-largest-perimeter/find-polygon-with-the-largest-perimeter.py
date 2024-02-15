class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sides = sorted(nums)
        curr_sum = sides[0] + sides[1]
        max_per = -1

        for i in range(2, len(sides)):
            # print(sides[i], curr_sum, max_per)
            if curr_sum > sides[i]:
                max_per = curr_sum + sides[i]
            curr_sum += sides[i]
        
        return max_per
