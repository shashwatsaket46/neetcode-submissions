from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        freq=Counter(hand)
        for i in sorted(hand):
            while freq[i]>0:
                for x in range(i, i+groupSize):
                    if freq[x]==0:
                        return False
                    freq[x]-=1
        return True
