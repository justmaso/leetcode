from __future__ import annotations
from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests
from typing import Optional


class ListNode:
    val: int
    next: Optional[ListNode]

    def __init__(self, val: int = 0, next: Optional[ListNode] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def nonOptimalRemoveNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        A non-optimal solution to removeNthFromEnd that uses two passes
        to remove the Nth node.
        
        Time: O(n)
        Space: O(1)
        """
        # get the length of the list
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # n is out of bounds
        if n > length or not head:
            return head
        
        # shift to the node to remove and the one before it
        prev = None
        curr = head
        for _ in range(length - n):
            prev = curr
            curr = curr.next

        # prev is now the node before the one to remove
        # curr is node to remove

        # the node to remove is the head
        if prev is None:
            return head.next
        # the node to remove is the tail
        elif curr is None:
            prev.next = None
            return head
        # the node to remove isn't the head
        else:
            prev.next = curr.next
            return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Given the head of a linked list, remove the Nth node
        from the end of the list and return the head.
        """

        """
        Optimal solution using a boundary node to better handle edge cases.

        Time: O(n)
        Space: O(1)
        """
        boundary = ListNode(0, head)
        prev = boundary
        later = head

        # shift to the Nth node from the head
        while n > 0 and later:
            later = later.next
            n -= 1

        # now, prev and later have N nodes between them

        # shift later until it's out of bounds
        while later:
            prev = prev.next
            later = later.next
        
        # now, prev is the node before the one to remove.
        # later is out of bounds now, but since prev and later
        # have N nodes between them, the node after prev is the Nth
        # node (i.e., the one to remove)

        # remove Nth node
        prev.next = prev.next.next

        # return the new head
        return boundary.next


if __name__ == "__main__":
    solution = Solution()

    """
    test_cases = [
        GenericTestCase(input=(), expected=None),
        GenericTestCase(input=(), expected=None),
        GenericTestCase(input=(), expected=None),
    ]

    run_tests(
        test_cases,
        [
            solution.nonOptimalRemoveNthFromEnd,
            solution.removeNthFromEnd
        ],
        label=__file__
    )
    """
