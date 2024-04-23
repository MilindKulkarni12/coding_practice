class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        
        q = deque([('0000', 0)])
        vis = set(deadends)
        
        def get_combinations(combi):
            res = []
            for i in range(4):
                digit = str((int(combi[i]) + 1) % 10)
                res.append(combi[:i] + digit + combi[i+1:])

                digit = str((int(combi[i]) - 1 + 10) % 10)
                res.append(combi[:i] + digit + combi[i+1:])
            return res

        while q:
            combi, turn = q.popleft()
            if combi == target:
                return turn

            for child in get_combinations(combi):
                if child not in vis:
                    q.append((child, turn + 1))
                    vis.add(child)
        return -1
