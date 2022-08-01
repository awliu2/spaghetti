from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseLinked(self, head: Optional[ListNode]) -> None:
        curr = head
        prev = None
        while curr:
            temp = curr
            curr.next = prev
            prev = curr
            curr = temp.next
        return prev

    # def reverseList(self, head: Optional[ListNode]) -> None:
    #     prev = None
    #     while head:
    #         temp = head.next
    #         head.next = prev
    #         prev, head, = head, temp
    #     return prev
