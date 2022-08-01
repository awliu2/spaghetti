# Definition for singly-linked list.
from typing import Optional

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
        while j.next and j.next.next:
            i = i.next
            j = j.next.next
        
        
        # reverse second half
        prev, curr = None, i.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        i.next = None
        
        # merge
        head1 = head
        head2 = prev
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt







"""
[1 2 3 4 5]
[1 3 4 5 2]
[1 3 5 2 4]
[1 5 2 4 3]
"""

