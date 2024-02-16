class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        freq = dict(sorted(freq.items(), key=lambda x: x[1]))
        remove = 0
        for key, val in freq.items():
            if val <= k:
                remove += 1
                k -= val
            if k == 0:
                break
        return len(freq.keys()) - remove