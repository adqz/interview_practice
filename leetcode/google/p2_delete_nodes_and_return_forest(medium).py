'''
https://leetcode.com/problems/delete-nodes-and-return-forest/
'''
from typing import List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.rootsToExplore = deque([])
        self.ans = []

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.to_delete = set(to_delete)
        self.rootsToExplore.append(root)
        self.helperDelNodes()

        return self.ans
    
    def helperDelNodes(self):
        while self.rootsToExplore:
            currentRoot = self.rootsToExplore.popleft()
            if currentRoot.val not in self.to_delete:
                self.ans.append(currentRoot)
                self.helperDFS(currentRoot)
            else:
                if currentRoot.left:
                    self.rootsToExplore.append(currentRoot.left)
                if currentRoot.right:
                    self.rootsToExplore.append(currentRoot.right)
                
    def helperDFS(self, node):
        # Base
        if not node:
            return
        if node.val in self.to_delete:
            if node.left:
                self.rootsToExplore.append(node.left)
            if node.right:
                self.rootsToExplore.append(node.right)
            return
        # Build
        self.helperDFS(node.left)
        self.helperDFS(node.right)

if __name__ == "__main__":
    sol = Solution()
    root             = TreeNode(1)
    root.left        = TreeNode(2)
    root.right       = TreeNode(3)
    root.left.left   = TreeNode(4)
    root.left.right  = TreeNode(5)
    root.right.left  = TreeNode(6)
    root.right.right = TreeNode(7)
    to_delete = [3,5]
    print(sol.delNodes(root, to_delete))