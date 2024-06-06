class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        elements_left = [False]
        def get_next_card(curr = -1):
            for i, card in enumerate(hand):
                if card != -1:
                    elements_left[0] = True
                    if curr == -1 or card - curr == 1:
                        return i
            return -1

        n = len(hand)
        if n % groupSize != 0:
            return False
        
        hand.sort()
        curr_group_size = 1
        curr = hand[0]
        hand[0] = -1
        while True:
            # print(curr)
            if curr_group_size == groupSize:
                next_card = get_next_card(-1)
                if next_card == -1:
                    return False if elements_left[0] else True
                elements_left[0] = False
                curr = hand[next_card]
                hand[next_card] = -1
                curr_group_size = 1
            else:
                next_card = get_next_card(curr)
                if next_card == -1:
                    return False if elements_left[0] else True
                curr = hand[next_card]
                hand[next_card] = -1
                elements_left[0] = False
                curr_group_size += 1
        