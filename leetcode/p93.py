'''
@author: adnan
Problem 112. Path Sum (Easy)

Runtime: 40 ms, faster than 80.84% of Python3 online submissions for Path Sum.
Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Path Sum.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        return self.helper_hasPathSum(0, root, sum)

    def helper_hasPathSum(self, path_sum, node, sum):
        # Base cases
        if self.is_leaf_node(node):
            path_sum += node.val
            if path_sum > sum:
                return False
            if path_sum == sum:
                return True
        else:
            path_sum += node.val
            if node.left and node.right:
                return self.helper_hasPathSum(path_sum, node.left, sum) or self.helper_hasPathSum(path_sum, node.right, sum)
            if node.left:
                return self.helper_hasPathSum(path_sum, node.left, sum)
            if node.right:
                return self.helper_hasPathSum(path_sum, node.right, sum)

    def is_leaf_node(self, node):
        if not node:
            return False
        if node.left or node.right: #if left of right are there, return False
            return False
        else:
            return True

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(sol.hasPathSum(root, 0)) #False