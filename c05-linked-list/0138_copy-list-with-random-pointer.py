from __future__ import annotations
from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests
from typing import Optional


class Node:
    def __init__(self, x: int = 0, next: Optional[Node] = None, random: Optional[Node] = None) -> None:
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def nonOptimalTwoPassCopyRandom(self, head: Optional[Node]) -> Optional[Node]:
        """
        Non-optimal two pass solution that first builds out deep copies, then
        links them.

        Time: O(n)
        Space: O(n)
        """
        old_to_copy = dict()

        # build out the deep copy (no links yet)
        curr = head
        while curr:
            copy = Node(curr.val)
            old_to_copy[curr] = copy
            curr = curr.next

        # link together the deep copy
        curr = head
        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next] if curr.next else None
            copy.random = old_to_copy[curr.random] if curr.random else None
            curr = curr.next

        return old_to_copy[head] if head else None

    def cleanerNonOptimalTwoPassCopyRandom(self, head: Optional[Node]) -> Optional[Node]:
        """
        The exact same code as nonOptimalTwoPassCopyRandom, just cleaner.
        """
        old_to_copy = {None: None}

        # build out deep copy (no linking yet)
        curr = head
        while curr:
            copy = Node(curr.val)
            old_to_copy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]
            curr = curr.next

        return old_to_copy[head]

    def nonOptimalOnePassCopyRandom(self, head: Optional[Node]) -> Optional[Node]:
        """
        Another non-optimal solution that builds out the deep copy and links
        the entire list in one pass.

        Time: O(n)
        Space: O(n)
        """
        from collections import defaultdict
        old_to_copy = defaultdict(lambda: Node())
        old_to_copy[None] = None

        # build out + link the nodes
        curr = head
        while curr:
            old_to_copy[curr].val = curr.val
            old_to_copy[curr].next = old_to_copy[curr.next]
            old_to_copy[curr].random = old_to_copy[curr.random]
            curr = curr.next

        return old_to_copy[head]


    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        A linked list of length n is given such that each node
        contains an additional random pointer, which could point
        to any node in the list, or None.

        Construct a deep copy of the list. The deepy copy should consist
        of exactly n brand new nodes, where each node has its value set
        to the value of its corresponding original node. Both the next
        and random pointer of the new nodes should point to the new nodes,
        in the copied list such that the pointers in the original list and
        copied list and copied list represent the same list state. None of
        the pointers in the new list should point to nodes in the original
        list.

        For example, if there are two nodes X and Y in the original list, where
        X.random --> Y, then the corresponding two nodes x and y in the copied list,
        x.random --> y.

        Return the head of the copied linked list.
        
        The linked list is represented in the input/output as a list of n nodes. Each
        node is represented as a pair of [val, random_index] where:
            - val: an integer representing Node.val
            - random_index: the index of the node (range from 0 to n-1) that the random
              pointer points to, or None if it does not point to any node.

        Your code will only be given the head of the original linked list.
        """
                
        """
        Optimal solution that 

        Time: O(n)
        Space: O(1)
        """

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
        [solution.copyRandomList],
        label=__file__
    )
    """
