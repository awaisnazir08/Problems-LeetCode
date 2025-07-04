# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(i, node1, node2):
            if not node1 or not node2:
                return None
            if i % 2 == 1:
                node1.val, node2.val = node2.val, node1.val
            
            i += 1

            dfs(i, node1.left, node2.right)
            dfs(i, node1.right, node2.left)

        
        dfs(1, root.left, root.right)

        return root