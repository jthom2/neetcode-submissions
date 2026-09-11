# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False

        right = self.isSameTree(p.right, q.right) & self.isSameTree(p.left, q.left)
        return right
            

        
        

        return True
        








        # if p is None and q is not None:
        #     return False
        # if q is None and p is not None:
        #     return False
        


        # if p:
        #     if not q:
        #         return False
        # if q:
        #     if not p:
        #         return False
        

        # lst = []
        
        # if (p and q) is not None:

        #         lst.append(p.val)
        #         lst.append(q.val)

        #         if lst[-1] != lst[-2]:
        #             return False



        #         if (p.val) != (q.val):
        #             return False


                
        #         if (p.left and q.left):
        #             if (p.left).val != (q.left).val:
        #                 return False
                
        #         if (p.right and q.right):
        #             if (p.right).val != (q.right).val:
        #                 return False
                
        #         if (p.right) and not (q.right):
        #             return False
        #         if (q.right) and not (p.right):
        #             return False
        #         if (p.left) and not (q.left):
        #             return False
        #         if (q.left) and not (p.left):
        #             return False


        #         print(p.val + 1)
                
        #         self.isSameTree(p.left, q.left)
        #         self.isSameTree(p.right, q.right)

        



       

     
        


        

        # return True
            

                
        
        

        
        

        
        
