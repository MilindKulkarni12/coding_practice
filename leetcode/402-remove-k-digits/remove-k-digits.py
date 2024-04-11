class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # ans = [float(inf)]
        # print('--', len(num), len(num)-k)
        # def fx(numb, n, idx, lim):
        #     try:
        #         if n == lim and n > 0 and int(numb) < ans[0]:
        #             ans[0] = int(numb)
        #         if n == lim:
        #             return
        #         fx(numb + num[idx], n + 1, idx + 1, lim)
        #         fx(numb, n, idx + 1, lim)
        #     except:
        #         print(n, idx)

        # fx('', 0, 0, len(num) - k)
        # return "0" if ans[0] == float(inf) else str(ans[0])
        # if len(num) == k:
        #     return '0'

        # stack = []
        # stack.append(num[0])
        # for i in range(1, len(num)):
        #     # print(num[i], k, stack)
        #     if stack:
        #         if k > 0 and int(num[i]) < int(stack[-1]):
        #             stack.pop()
        #             k -= 1
        #             stack.append(num[i])
        #         elif k > 0 and int(num[i]) <= int(num[i-1]):
        #             stack.append(num[i])
        #         elif k <= 0:
        #             stack.append(num[i])
        #         else:
        #             k -= 1
        # # print(stack)
        # i = 0
        # while stack[i] == '0':
        #     i += 1
        # return ''.join(stack[i:])
        numStack = []
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1
            numStack.append(digit)
        finalStack = numStack[:-k] if k else numStack
        
        return "".join(finalStack).lstrip('0') or "0"
