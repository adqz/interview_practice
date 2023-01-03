import time
from datetime import datetime
from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        i, j = 0, 1
        min_time_diff = float('inf')
        for i in range(0, len(timePoints)-1):
            for j in range(i+1, len(timePoints)):
                t1, t2 = timePoints[i], timePoints[j]
                time_diff = self.get_time_diff(t1, t2)
                if time_diff < min_time_diff:
                    min_time_diff = time_diff
        
        return min_time_diff
    
    def get_time_diff(self, t1, t2):
        # hour1, min1 = t1.split(':')
        # hour2, min2 = t2.split(':')
        FMT = '%H:%M'
        tdelta = datetime.strptime(t2, FMT) - datetime.strptime(t1, FMT)
        # t1 = time.asctime((2018, 12, 28, int(hour1), int(min1), 0, 0, 362, 0))
        # t2 = time.asctime((2018, 12, 28, int(hour2), int(min2), 0, 0, 362, 0))
        print(tdelta)
        print(tdelta, tdelta)

if __name__ == "__main__":
    sol = Solution()
    sol.findMinDifference(["23:59","00:00"])