# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        storeRes=[]
        level = 0
        self.rightView(root,storeRes,level)
        return storeRes

    def rightView(self,root,storeRes,level):            
        if root is None:
            return 
        if level == len(storeRes):
            storeRes.append(root.val)

        self.rightView(root.right,storeRes,level+1)
        self.rightView(root.left,storeRes,level+1)



            

        