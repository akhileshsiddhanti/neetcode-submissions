# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next if head is not None else None
    
        while slow is not None or fast is not None:
            if slow == fast:
                return True
            
            slow = slow.next
            
            if fast and fast.next is not None:
                fast = fast.next.next
            else:
                return False
        
        return False

        