# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        # def isSameTree(p, q):
        #     if (p and not q) or (not p and q):
        #         return False
        #     if (not p and not q):
        #         return True
        #     if p.val != q.val:
        #         return False
        #     if p.val == q.val:
        #         return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        # if root and subRoot:
        #     return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        # else:
        #     return False

        def preOrder(root):
            if root:
                return str(root.val) + "," + preOrder(root.left) + "," + preOrder(root.right)
            else:
                return "null"
        
        s = preOrder(root)
        sub = preOrder(subRoot)

        i,j=0,0

        while i < len(s):
            while j < len(sub):
                if i<len(s) and s[i] == sub[j]:
                    i,j=i+1,j+1
                else:
                    i = i - j + 1
                    j = 0
                if j==len(sub):
                    return True
                if i > len(s):
                    break
        
        return j == len(sub)

                


