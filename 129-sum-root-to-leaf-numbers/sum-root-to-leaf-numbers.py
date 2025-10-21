# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = []

        def dfs(node, string):
            if not node:
                return
            
            if not node.left and not node.right:
                res.append(int(string[:]))
            else:
                if node.left:
                    string += str(node.left.val)
                    dfs(node.left, string)
                    string = string[:-1]
                if node.right:
                    string += str(node.right.val)
                    dfs(node.right, string)
                    string = string[:-1]
        
        dfs(root, str(root.val))

        return sum(res)
