class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def add_room(r, c):
            if r < 0 or r >= n or c < 0 or c >= m or ((r, c) in vis ) or rooms[r][c] == -1:
                return
            q.append((r, c))
            vis.add((r, c))
        
        n = len(rooms)
        m = len(rooms[0])
        q = deque()
        vis = set()

        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    q.append((i, j))
                    vis.add((i, j))
        
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                vis.add((r, c))
                rooms[r][c] = dist

                add_room(r, c + 1)
                add_room(r, c - 1)
                add_room(r + 1, c)
                add_room(r - 1, c)
            dist += 1

