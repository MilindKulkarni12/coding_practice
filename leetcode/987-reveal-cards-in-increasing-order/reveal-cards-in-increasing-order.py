class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        ans = [-1]*n
        i = j = 0
        count = 0
        flag = True
        while count < n:
            if flag and ans[i] == -1:
                ans[i] = deck[j]
                j += 1
                count += 1
                flag = False
            elif ans[i] == -1:
                flag = True
            i = (i + 1) % n
        return ans
