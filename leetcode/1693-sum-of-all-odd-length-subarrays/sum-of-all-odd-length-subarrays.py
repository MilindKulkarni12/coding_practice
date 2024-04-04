class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = sum(arr)
        n = len(arr)
        if n < 3:
            return total
        
        for w in range(3, n+1, 2):
            for i in range(n-w+1):
                # print(i, w, n)
                total += sum(arr[i: i+w])
        return total
