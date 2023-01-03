from typing import List
from collections import Counter, deque
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        sortedHand = sorted(hand)
        sortedHand = deque(sortedHand)
        group = []
        actualNumberOfGroups = 0
        expectedNumberOfGroups = len(hand)/W
        lastNumberSeen = None

        i = 0
        while sortedHand:
            if len(group) == W:
                print('group = ', group)
                actualNumberOfGroups += 1
                group = []
                lastNumberSeen = None
                i = 0
                
            
            number = sortedHand[i]
            if lastNumberSeen != None:
                if number == lastNumberSeen + 1:
                    group.append(number)
                    lastNumberSeen = number
                    del sortedHand[i]
                elif number == lastNumberSeen:
                    i += 1
                    continue
                else:
                    return False
            else:
                group.append(number)
                lastNumberSeen = number
                del sortedHand[i]
    
        if expectedNumberOfGroups == actualNumberOfGroups:
            return True
        else:
            return False

if __name__ == "__main__":
    sol = Solution()
    # print(sol.isNStraightHand(hand = [1,2,3], W = 1)) #true
    # print(sol.isNStraightHand(hand = [1,2,3], W = 3)) #true
    print(sol.isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], W = 3)) #true
    # print(sol.isNStraightHand(hand = [1,2,3,4,5], W = 4)) #false