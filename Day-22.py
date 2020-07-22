# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        queue = []
        order = 0
        queue.append(root)
        while queue:
            size = len(queue)
            temp = []
            order += 1
            for i in range(size):
                cur_node = queue.pop(0)
                temp.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            if order%2==0:
                ans.append(temp[::-1])
            else:
                ans.append(temp)
        return ans
