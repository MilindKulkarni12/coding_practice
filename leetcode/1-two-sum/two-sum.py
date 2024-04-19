class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_dict = {}

        # Iterate through the array
        for i, num in enumerate(nums):
            # Check if the complement of the current number exists in the dictionary
            if target - num in complement_dict:
                # If it does, return the indices of the current number and its complement
                return [complement_dict[target - num], i]
            # Otherwise, store the current number and its index in the dictionary
            complement_dict[num] = i

        # If no solution is found, return an empty list
        return []