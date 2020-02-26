'''
@author: adnan
Problem 497. Random Point in Non-overlapping Rectangles (Medium)

Runtime: 236 ms, faster than 21.14% of Python3 online submissions for Random Point in Non-overlapping Rectangles.
Memory Usage: 16.6 MB, less than 100.00% of Python3 online submissions for Random Point in Non-overlapping Rectangles.
'''

import random
from typing import List
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = []
        for [x1, y1, x2, y2] in self.rects:
            num_point_in_rect = (x2-x1+1) * (y2-y1+1)
            self.weights.append(num_point_in_rect)

    def pick(self) -> List[int]:
        rect = random.choices(self.rects, weights=self.weights, k=1)[0]
        p_x = random.randint(rect[0], rect[2])
        p_y = random.randint(rect[1], rect[3])
        return [p_x, p_y]


if __name__ == "__main__":
    rects = [[1,1,5,5]]
    obj = Solution(rects)
    param_1 = obj.pick()
    print(param_1)