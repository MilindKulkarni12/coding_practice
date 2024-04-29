class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = bin(start)[2:]
        goal = bin(goal)[2:]

        n = len(start)
        m = len(goal)
        if n < m:
            start = '0'*(m-n) + start
            n = m
        elif m < n:
            goal = '0'*(n-m) + goal
            m = n
        
        return sum([1 for i in range(n) if start[i] != goal[i]])
