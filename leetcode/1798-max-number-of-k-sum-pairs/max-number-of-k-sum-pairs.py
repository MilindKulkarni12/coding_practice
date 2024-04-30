class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        found = defaultdict(bool)
        count = 0
        for i in nums:
            if i in found:
                if i == k-i and freq[i] < 2:
                    continue
                if freq[i] > 0 and freq[k-i] > 0:
                    count += 1
                    freq[i] -= 1
                    freq[k-i] -= 1
            else:
                found[k-i] = True
        return count

