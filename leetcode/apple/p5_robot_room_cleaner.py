'''
@author: adnan
Problem 489. Robot Room Cleaner (Hard)

Runtime: 76 ms, faster than 45.08% of Python3 online submissions for Robot Room Cleaner.
Memory Usage: 14.9 MB, less than 50.00% of Python3 online submissions for Robot Room Cleaner.
'''
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """

#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """

#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """

#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

from collections import defaultdict
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.visited = defaultdict(lambda: False)
        self.directions = [(-1,0), (0,1), (1, 0), (0, -1)]
        self.robot = robot
        self.dfs()

    def dfs(self, curr_cell = (0,0), curr_direction = 0):
        self.visited[curr_cell] = True
        self.robot.clean()
        # Explore directions
        for i in range(4):
            new_d = (curr_direction + i) % 4
            next_cell = (curr_cell[0] + self.directions[new_d][0], curr_cell[1] + self.directions[new_d][1])
            
            if not self.visited[next_cell] and self.robot.move():
                self.dfs(next_cell, new_d)
                self.go_back() #backtracking
            
            self.robot.turnRight()

    def go_back(self):
        self.robot.turnRight()
        self.robot.turnRight()
        self.robot.move()
        self.robot.turnRight()
        self.robot.turnRight()
        