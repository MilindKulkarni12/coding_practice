class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        adj_list = defaultdict(list)
        pre_req_count = defaultdict(int)
        for c1, c2 in prerequisites:
            adj_list[c1].append(c2)
            adj_list[c2].append(c1)
            pre_req_count[c1] += 1
            pre_req_count[c2] += 0

        pickables = deque([k for k, v in pre_req_count.items() if v == 0])
        picked = set(pickables)
        if len(pickables) == 0:
            return False
        
        while pickables:
            pick = pickables.popleft()
            for next_pick in adj_list[pick]:
                if next_pick not in picked:
                    pre_req_count[next_pick] -= 1
                    if pre_req_count[next_pick] == 0:
                        pickables.append(next_pick)
                        picked.add(next_pick)
        return True if len(picked) == len(pre_req_count) else False





