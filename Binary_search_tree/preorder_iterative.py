# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        stack=[root.val] if root else []
        
        while len(stack)>0:
            root=stack.pop()
            ans.append(root.val)
            if root.right!=None:
                stack.append(root.right)
            if root.left!=None:
                stack.append(root.left)
        return ans