class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        """
        nums = 2, 3, 2, 1
        freq = 3, 2,-3, 1

        0 (2, 3) -> 3
        1 (2, 3) (3, 2) -> 3
        2 (2, 0) (3, 2) -> 2
        3 (2, 0) (3, 2) (1, 1) -> 2
        """
        
        # new_list = heapq.heapify(zip(freq, ))

        ans = []
        max_id = max_freq = -1
        lookup = defaultdict(int)

        for i in range(len(nums)):
            lookup[nums[i]] += freq[i]
            if nums[i] == max_id and lookup[nums[i]] > max_freq:
                max_freq = lookup[nums[i]]
            elif nums[i] == max_id:
                max_id, max_freq = sorted(lookup.items(), key=lambda x: x[1], reverse=True)[0]
            elif lookup[nums[i]] > max_freq:
                max_freq = lookup[nums[i]]
                max_id = nums[i]
            
            ans.append(max_freq)
        return ans
