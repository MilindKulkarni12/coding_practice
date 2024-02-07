class OrderedStream:

    def __init__(self, n: int):
        self.size = n + 1
        self.stream = [0]*(n+1)
        self.ptr = 1
    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        op = []
        while self.ptr < self.size and self.stream[self.ptr] != 0:
            op.append(self.stream[self.ptr])
            self.ptr += 1
        
        return op


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)