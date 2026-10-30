# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preord: List[int], inord: List[int]) -> Optional[TreeNode]:
        if not preord or not inord:
            return None

        mem = {inord[j]: j for j in range(len(inord))}
        pre_idx = 0
        
        def build_tree(l, r):
            nonlocal pre_idx
            if l > r:
                return None
            
            root = TreeNode(preord[pre_idx])
            mid = mem[preord[pre_idx]]
            pre_idx += 1

            root.left = build_tree(l, mid - 1)
            root.right = build_tree(mid+1, r)

            return root

        return build_tree(0, len(inord)-1)