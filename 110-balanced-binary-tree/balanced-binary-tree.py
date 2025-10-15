# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkHeight(node):
            if not node:
                return 0  # height = 0
            
            left = checkHeight(node.left)
            right = checkHeight(node.right)
            
            # If left or right subtree is unbalanced
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1  # signal unbalanced
            
            return max(left, right) + 1  # return height if balanced
        
        return checkHeight(root) != -1



        

