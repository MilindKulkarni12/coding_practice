class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:         
        tgt = tickets[k]
        tix = 0
        for i in range(len(tickets)):
            # print(tix)
            if i < k:
                if tickets[i] <= tgt:
                    tix += tickets[i]
                else:
                    tix += tgt
            elif i > k:
                if tickets[i] < tgt:
                    tix += tickets[i]
                else:
                    tix += tgt - 1
        return tix + tgt
