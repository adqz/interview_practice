# 129. Sum Root to Leaf Numbers
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
Runtime: 24 ms, faster than 95.65% of Python3 online submissions for Sum Root to Leaf Numbers.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Sum Root to Leaf Numbers.
'''
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
            if not root:
                return 0

            def dfs(node, prev):
                prev = prev*10 + node.val 

                if node.left and node.right:
                    return dfs(node.left, prev) + dfs(node.right, prev)
                elif node.left:
                    return dfs(node.left, prev)
                elif node.right:
                    return dfs(node.right, prev)
                else:
                    return prev

            return dfs(root, 0)


'''
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
            def dfs(node, prev):
        
                if not node:
                    return 0

                prev = prev*10 + node.val 

                if node.left and node.right:
                    return dfs(node.left, prev) + dfs(node.right, prev)
                elif node.left:
                    return dfs(node.left, prev)
                elif node.right:
                    return dfs(node.right, prev)
                else:
                    return prev

            return dfs(root, 0)
'''