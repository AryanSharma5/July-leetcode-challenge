# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        queue = []
        if not root:
            return result
        queue.append(root)
        while queue:
            size = len(queue)
            temp = []
            for i in range(size):
                cur_node = queue.pop(0)
                temp.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            result.append(temp)
        return result[::-1]