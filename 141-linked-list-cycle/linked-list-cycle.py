# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        pos=head
        while pos and pos.next:
            head=head.next
            pos=pos.next.next
            if head is pos:
                return True
            
        return False
        