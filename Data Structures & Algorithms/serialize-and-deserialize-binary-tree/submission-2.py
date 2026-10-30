# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "null"

        q = deque([root])
        res = []

        while q:
            current = q.popleft()
            if current:
                res.append(str(current.val))
                q.append(current.left)
                q.append(current.right)
            else:
                res.append("null")

        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        q = deque()
        if vals[0] == "null":
            return None
        
        root = TreeNode(vals[0])
        q.append(root)

        index = 1
        while q:
            node = q.popleft()
            
            if vals[index] != "null":
                node.left = TreeNode(int(vals[index]))
                q.append(node.left)
                
            index += 1

            if vals[index] != "null":
                node.right = TreeNode(int(vals[index]))
                q.append(node.right)
            
            index += 1
        
        return root
            
            



