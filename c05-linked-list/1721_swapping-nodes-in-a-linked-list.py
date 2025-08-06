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
    def nonOptimalSwapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Non-optimal solution that swaps nodes in two passes.

        Time: O(n)
        Space: O(1)
        """
        length = 0

        curr = head
        while curr:
            length += 1
            curr = curr.next

        left_node = right_node = head
        for _ in range(k - 1): left_node = left_node.next
        for _ in range(length - k): right_node = right_node.next

        left_node.val, right_node.val = right_node.val, left_node.val

        return head

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Given the head of a linked list and an integer k, return
        the head of the linked list after swapping the values of the
        kth node from the beginning and the kth node from the end.

        Assume the list is 1-indexed.
        """
        pass


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
        [solution.swapNodes],
        label=__file__
    )
    """
