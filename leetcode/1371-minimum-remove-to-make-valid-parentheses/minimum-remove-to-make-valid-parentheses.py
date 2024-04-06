class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == ')':
                # ())()(((
                temp = []
                f = False
                while stack:
                    x = stack.pop()
                    if x == '(':
                        temp.append('*')
                        f = True
                        break
                    else:
                        temp.append(x)
                if temp and f:
                    stack.extend(temp[::-1])
                    stack.append('#')
                    # print(stack)
                else:
                    stack.extend(temp[::-1])
                    # print(stack)
            else:
                stack.append(s[i])
        
        return ''.join(stack).replace('(', '').replace('*', '(').replace('#', ')')
