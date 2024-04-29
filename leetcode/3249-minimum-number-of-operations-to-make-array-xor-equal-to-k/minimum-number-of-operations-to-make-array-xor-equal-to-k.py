class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0
        for n in nums:
            xor = n ^ xor
        
        bin_xor = bin(xor)[2:]
        bin_k = bin(k)[2:]

        if len(bin_xor) < len(bin_k):
            bin_xor = '0' * ((len(bin_k) - len(bin_xor))) + bin_xor
        elif len(bin_k) < len(bin_xor):
            bin_k = '0' * (len(bin_xor) - len(bin_k)) + bin_k
        # print(bin_xor, bin_k)
        return sum([1 for i in range(len(bin_k)) if bin_k[i] != bin_xor[i]])
