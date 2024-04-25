class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            # print('in1')
            return range(numCourses)

        adj_list = defaultdict(list)
        pre_req_count = defaultdict(int)
        for c1, c2 in prerequisites:
            adj_list[c1].append(c2)
            adj_list[c2].append(c1)
            pre_req_count[c1] += 1
            pre_req_count[c2] += 0

        pickables = deque([k for k, v in pre_req_count.items() if v == 0])
        picked = {k: True for k in pickables}
        # print(picked)
        if len(pickables) == 0:
            # print('in2')
            return []
        
        while pickables:
            pick = pickables.popleft()
            for next_pick in adj_list[pick]:
                if next_pick not in picked:
                    pre_req_count[next_pick] -= 1
                    if pre_req_count[next_pick] == 0:
                        pickables.append(next_pick)
                        picked[next_pick] = True
        # print(picked)
        courses = []
        if len(picked) == len(pre_req_count):
            courses = list(picked.keys())
            if len(picked) != numCourses:
                courses = [i for i in range(numCourses) if i not in picked] + courses
        return courses
