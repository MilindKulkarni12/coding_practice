class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        mpg = [0, 0, 0]
        minutes = 0

        new_travel = [0]
        for i in range(1, len(travel)+1):
            new_travel.append(travel[i-1] + new_travel[i-1])
        # print(new_travel)
        
        for i, g in enumerate(garbage):
            pos = mpg[::]
            for c in g:
                if c == 'M':
                    minutes += 1
                    mpg[0] = i
                if c == 'P':
                    minutes += 1
                    mpg[1] = i
                if c == 'G':
                    minutes += 1
                    mpg[2] = i
            # print(pos, mpg, minutes)
            for j in range(3):
                if pos[j] != mpg[j]:
                    # print(new_travel[mpg[j]] - new_travel[pos[j]])
                    minutes += (new_travel[mpg[j]] - new_travel[pos[j]])
    
        return minutes
