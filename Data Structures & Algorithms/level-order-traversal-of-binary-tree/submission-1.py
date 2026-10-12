# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        from collections import deque
        d = deque()
        d.append(root)
        result = []

        while d:
            level = []
            for i in range(0, len(d)):
                current = d.popleft()
                level.append(current.val)
                if current.left:
                    d.append(current.left)
                if current.right:
                    d.append(current.right)
            result.append(level)

        return result

        # from collections import deque
        # d = deque()
        # height = 0
        # d.append((root, height))

        # result = []
        # current_result = []

        # if not root:
        #     return []

        # while d:
        #     current, node_height = d.popleft()
        #     if current:
        #         if height == node_height:
        #             current_result.append(current.val)
        #         else:
        #             result.append(current_result)
        #             current_result = [current.val] if current else None
        #             height += 1

        #         if current.left:
        #             d.append((current.left, node_height + 1))
        #         if current.right:
        #             d.append((current.right, node_height + 1))
        
        # result.append(current_result)
        # return result
            


        