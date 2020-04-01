'''
@author: adnan
Problem 841. Keys and Rooms (Medium)

Runtime: 68 ms, faster than 52.21% of Python3 online submissions for Keys and Rooms.
Memory Usage: 14.1 MB, less than 9.09% of Python3 online submissions for Keys and Rooms.
'''
from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = [0]
        rooms_visited = set()

        while keys:
            key = keys.pop()
            if key not in rooms_visited:
                new_keys = rooms[key]
                keys += new_keys
                rooms_visited.add(key)

        if len(rooms_visited) == len(rooms):
            return True

        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.canVisitAllRooms([[1],[2],[3],[]])) #True
    print(sol.canVisitAllRooms([[1,3],[3,0,1],[2],[0]])) #False