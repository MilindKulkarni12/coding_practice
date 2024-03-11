class Solution:
    def customSortString(self, order: str, s: str) -> str:
        o_dict = {order[i]: i for i in range(len(order))}
        i = len(order)
        for c in s:
            if o_dict.get(c, -1) == -1:
                o_dict[c] = i
                i += 1 
        ans = ''.join(sorted(s, key=lambda x: o_dict[x]))
        return ans
