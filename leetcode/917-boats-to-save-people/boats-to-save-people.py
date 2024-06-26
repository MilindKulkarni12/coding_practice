class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        # 3 3 4 5 - 5

        while l <= r:
            if people[l] + people[r] <= limit:
                boats += 1
                l += 1
                r -= 1
            else:
                r -= 1
                boats += 1
            
        return boats
