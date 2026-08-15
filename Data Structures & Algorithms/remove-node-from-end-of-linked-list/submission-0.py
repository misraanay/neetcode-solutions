# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        for i in range(n):
            fast = fast.next
        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        # fast is null => slow is the node to remove
        if prev is None:
            head = slow.next
            slow.next = None
            return head
        prev.next = slow.next
        slow.next = None
        return head