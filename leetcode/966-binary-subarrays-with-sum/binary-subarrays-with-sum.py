class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        curr_sum  = 0
        ans = 0
        pref = defaultdict(int)
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum == goal:
                ans += 1
            ans += pref.get(curr_sum - goal, 0)
            pref[curr_sum] += 1
        return ans
