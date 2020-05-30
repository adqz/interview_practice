'''
https://leetcode.com/problems/delete-nodes-and-return-forest/

Runtime: 68 ms, faster than 76.85% of Python3 online submissions for Delete Nodes And Return Forest.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Delete Nodes And Return Forest.
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
    '''
    n = number of nodes in tree
    k = number of nodes to delete
    Time: O(n)
    Space: O(k)
    '''
    def __init__(self):
        self.ans = []

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.to_delete = set(to_delete)
        if root.val not in to_delete:
            self.ans.append(root)
        
        self.helperDFS(root)

        return self.ans
    
    def helperDFS(self, node):
        # Base
        if node is None:
            return
        # Build
        if node.val in self.to_delete:
            if node.left and node.left.val not in self.to_delete:
                self.ans.append(node.left)
            if node.right and node.right.val not in self.to_delete:
                self.ans.append(node.right)
        
        l, r = node.left, node.right
        if l and l.val in self.to_delete:
            node.left = None
        if r and r.val in self.to_delete:
            node.right = None
        
        self.helperDFS(l)
        self.helperDFS(r)


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
    ans = sol.delNodes(root, to_delete)
    print([node.val for node in ans])