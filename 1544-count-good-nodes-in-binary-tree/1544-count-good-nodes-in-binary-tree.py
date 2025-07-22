# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxi):
            count = 0
            if not node:
                return 0
            if node.val>= maxi:
                maxi = node.val
                count+=1
            lcount = dfs(node.left,maxi)
            rcount = dfs(node.right,maxi)
            return count+ lcount+rcount
        
        return dfs(root,root.val)
        
        