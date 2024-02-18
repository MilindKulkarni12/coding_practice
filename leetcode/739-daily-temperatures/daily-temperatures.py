class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        """
            73 push
            74: 73 pop, push (1-0) = 73,1
            75: 74 pop, push (2-1) = 74,1
            71 push
            69 push
            72: 69 pop (5-4) = 69,1, 71 pop (5-3) = 71,2
            76: 72 pop (6-5) = 72,1, 75 pop (6-2) = 75,4
            73: push
        """
        stack = []
        waiting_days = [0]*len(temps)
        for i in range(len(temps)):
            if len(stack) == 0:
                stack.append((temps[i], i))
            else:
                while stack and stack[-1][0] < temps[i]:
                    x, y = stack.pop()
                    waiting_days[y] = i - y
                stack.append((temps[i], i))
        return waiting_days
                

