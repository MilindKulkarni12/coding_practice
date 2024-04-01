class Solution:
    def minSwaps(self, s: str) -> int:
        """
            1111000     
            1010101        
            
            11110000 
            10101010         
            TFTFFTFT
            
            11110000
            01010101
            FTFTTFTF
        """
        n = len(s)
        freq = Counter(s)
        if n % 2 == 0:
            if freq['0'] != freq['1']:
                return -1
        else:
            if abs(freq['0'] - freq['1']) != 1:
                return -1

        if n % 2 != 0:
            k = '1' if freq['1'] > freq['0'] else '0'
            count = 0
            for c in s:
                if c != k:
                    count += 1
                k = '0' if k == '1' else '1'
        else:
            k = '1'
            count1 = count2 = 0
            for c in s:
                if c != k:
                    count1 += 1
                k = '0' if k == '1' else '1'
            k = '0'
            for c in s:
                if c != k:
                    count2 += 1
                k = '0' if k == '1' else '1'
            count = min(count1, count2)
        return count // 2
