class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
            5: 0101
            6: 0110
            7: 0111
            &: 0100
            =: 4
        """
        cnt = 0
        while left != right:
            left >>= 1
            right >>= 1
            cnt += 1
        return left << cnt
