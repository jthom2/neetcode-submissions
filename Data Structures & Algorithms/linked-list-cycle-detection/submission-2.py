# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head; fast = head; i = 0
        
        while slow and fast:
            if (i!=0) and (slow == fast): return True
            
            slow = slow.next
            try: fast = fast.next.next
                
            except: return False
            i += 1
                
        return False
        