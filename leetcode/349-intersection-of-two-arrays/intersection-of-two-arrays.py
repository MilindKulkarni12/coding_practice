class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {k: True for k in nums1}
        return [k for k in list(set(nums2)) if freq.get(k, False)]
