# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorderMap = {val:i for i, val in enumerate(inorder)}
        
        def recursion(low, high):
            if low>high:
                return
            root = TreeNode(postorder.pop())
            mid = inorderMap[root.val]
            root.right = recursion(mid+1, high)
            root.left = recursion(low, mid-1)
            return root
        
        return recursion(0, len(postorder)-1)