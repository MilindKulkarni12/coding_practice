class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        task_queue = [-v for v in freq.values()]
        heapq.heapify(task_queue)

        time = 0
        q = deque()
        while task_queue or q:
            time += 1
            if task_queue:
                v = 1 + heapq.heappop(task_queue)
                if v:
                    q.append((v, time + n))
            if q and q[0][1] == time:
                heapq.heappush(task_queue, q.popleft()[0])
        return time
