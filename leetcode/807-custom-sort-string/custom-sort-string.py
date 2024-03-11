class Solution:
    def customSortString(self, order: str, s: str) -> str:
        o_dict = {order[i]: i for i in range(len(order))}
        ans = ''.join(sorted(s, key=lambda x: o_dict.get(x, -1)))
        return ans
