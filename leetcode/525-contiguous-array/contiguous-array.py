class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        # curr_sum = 0
        pref = {}
        # for i in range(1, n):
        #     if nums[i] == 1:
        #         curr_sum += 1
        #         pref[curr_sum] = i

        count = 0
        ans = 0
        for i in range(n):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            if count == 0:
                ans = i+1
            elif pref.get(count, -1) != -1:
                ans = max(ans, i - pref[count])
            else:
                pref[count] = i
        return ans
        # 0 1 


