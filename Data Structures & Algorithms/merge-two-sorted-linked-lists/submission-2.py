# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        l1 = list1; l2 = list2
        if not l1: return l2
        elif not l2: return l1
        if l1.val < l2.val: 
            head = ListNode(l1.val); l1 = l1.next
        else: 
            head = ListNode(l2.val); l2 = l2.next

        root = head

        while l1 or l2:
            while l1 and l2:
                if l1.val < l2.val:
                    node = ListNode(l1.val)
                    head.next = node
                    l1 = l1.next
                else:
                    node = ListNode(l2.val)
                    head.next = node
                    l2 = l2.next
                head = head.next
            while l1:
                node = ListNode(l1.val)
                head.next = node
                head = head.next
                l1 = l1.next
            while l2:
                node = ListNode(l2.val)
                head.next = node
                head = head.next
                l2 = l2.next
        
        return root

        



        