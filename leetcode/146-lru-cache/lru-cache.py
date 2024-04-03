class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lru = {}
        self.time = 0

    def get(self, key: int) -> int:
        self.time += 1
        if key in self.lru:
            self.lru[key] = (self.lru[key][0], self.time)
            return self.lru[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        self.time += 1
        if key in self.lru: # existing
            self.lru[key] = (value, self.time)
        else: # new
            if self.cap == 0:
                # remove lru
                oldest = 1000000
                idx = -1
                for k, v in self.lru.items():
                    if v[1] < oldest:
                        oldest = v[1]
                        idx = k
                self.lru.pop(idx)
                self.lru[key] = (value, self.time)
            else:
                self.lru[key] = (value, self.time)
                self.cap -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)