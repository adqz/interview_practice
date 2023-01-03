'''
Leetcode: 79 (Word Search)
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.

Given word = "SEE", return true.

Given word = "ABCB", return false.

The problem is one of search. 
Can use - BFS
Time: O(M x N), M = number of occurences of word[0] in board, N = number of elements on board
Spae: O()
# TODO: Add bactracking
'''

from collections import deque 
def find_pattern(board, word):
    # TODO: asserts and docstring
    R = len(board)
    C = len(board[0])
    start_locations = []
    
    # Finding locations of first character in word
    for i in range(R):
        for j in range(C):
            if board[i][j] == word[0]:
                start_locations.append((i,j))
    
    if not start_locations:
        return False
    
    found = False
    for start in start_locations:
        # 1. Do BFS. Return True/False
        found = found or bfs(board, start, word)
        # 2. Return it
    return found
    
def bfs(board, start, word):
    # BFS
    i = 1
    queue = deque(start)
    R, C = len(board), len(board[0])
    while queue:
        # 1. Pop a node
        node = queue.popleft()
        neighbors = getNeighbors(node, R, C)
        for neighbor in neighbors:
            if board[neighbor] == word[i]:
                queue.append(neighbor)
                i += 1
                
    if i == len(word)-1: return True
    return False
    
def getNeighbors(node, R, C):
    r, c = node[0], node[1]
    neighbors = []
    for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
        if 0 <= nr < R and 0 <= nc < C:
            neighbors.append((nr, nc))
    
    return neighbors
        
        
        
    