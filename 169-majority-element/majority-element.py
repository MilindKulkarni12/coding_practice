class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if count == 0:
                max_element = i
                count += 1
            elif max_element != i:
                count -= 1
            else:
                count += 1
        return max_element
    