class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort the input array
        n = len(nums)
        result = []

        for a in range(n - 3):
            # Skip duplicates for the first element
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            for b in range(a + 1, n - 2):
                # Skip duplicates for the second element
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                left = b + 1
                right = n - 1

                while left < right:
                    total = nums[a] + nums[b] + nums[left] + nums[right]

                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result.append([nums[a], nums[b], nums[left], nums[right]])

                        # Skip duplicates for the third and fourth elements
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

        return result