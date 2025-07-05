# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def bfs(i, root):
            if not root:
                return i
            i += 1

            l = bfs(i, root.left)
            r = bfs(i, root.right)

            return max(l, r)
        
        return bfs(0, root)
        