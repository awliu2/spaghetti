# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # get middle of linked list
        i = head
        j = head
        while j:
            i = i.next
            j = j.next.next
        
        # reverse second half


"""
[1 2 3 4 5]
[1 3 4 5 2]
[1 3 5 2 4]
[1 5 2 4 3]
"""

