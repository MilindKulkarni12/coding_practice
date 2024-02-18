class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        min_digits = len(str(low))
        max_digits = len(str(high))
        ans = []
        for i in range(min_digits, max_digits+1):
            # initialize starting digit
            fd = 1
            num = []
            # initialize first num in the seq
            for j in range(i):
                num.append(fd) 
                fd += 1
            # fd = 5
            curr_num = int(''.join([str(n) for n in num]))
            if low <= curr_num <= high:
                ans.append(curr_num) # 1234
            while fd < 10:
                num.append(fd) # 123456789
                curr_num = int(''.join([str(n) for n in num[len(num)-i:]]))
                if low <= curr_num <= high:
                    ans.append(curr_num)
                fd += 1
            
        return ans
