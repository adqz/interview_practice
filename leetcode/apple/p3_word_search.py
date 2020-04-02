'''
@author: adnan
Problem 79. Word Search (Medium)

Runtime: 436 ms, faster than 19.43% of Python3 online submissions for Word Search.
Memory Usage: 15 MB, less than 19.15% of Python3 online submissions for Word Search.
'''
from typing import List
from collections import deque, defaultdict
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        Use Backtracking with BFS
        '''
        self.board = board
        self.R, self.C = len(board), len(board[0])
        self.word_found = False

        for r in range(self.R):
            for c in range(self.C):
                self.visited = defaultdict(lambda: False)
                word_found = self.backtrack(r, c, word)
                # Return True if word was found
                if word_found:
                    return True
        
        return False

    def backtrack(self, r, c, word):
        # Base Case
        if len(word) == 1 and self.board[r][c] == word[0]:
            return True

        if self.board[r][c] != word[0]:
            return False

        self.visited[(r, c)] = True
        # 3. Explore neighbours
        word_found = False
        neighbours = self.get_neighbours(r, c)
        for neighbour in neighbours:
            nr, nc = neighbour
            if not self.visited[(nr, nc)]:
                word_found = self.backtrack(nr, nc, word[1:])
                # 4. Backtrack if solution did not work
                if word_found: break
                self.visited[(nr, nc)] = False
        
        return word_found
    
    def get_neighbours(self, r, c):
        neighbours = []
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if 0 <= nr < self.R and 0 <= nc < self.C:
                neighbours.append((nr, nc))
        
        return neighbours

if __name__ == "__main__":
    board = [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
            ]
    sol = Solution()
    print(sol.exist(board, "ABCCED")) #True
    print(sol.exist(board, "SEE")) #True
    print(sol.exist(board, "ABCB")) #False
    print(sol.exist([['a']], 'a')) #True

