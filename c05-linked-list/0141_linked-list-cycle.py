from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def nonOptimalHasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Non-optimal solution to hasCycle using a set to track
        seen nodes.
        """
        seen = ()
        
        while head:
            if head in seen:
                return True

            seen.add(head)
            head = head.next

        return False


    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Given the head of a linked list, determine if the
        linked list has a cycle in it.

        There is a cycle in a linked list if there is some
        node in the list that can be reached again by continuously
        following the next pointer.
        """

        """
        Optimal solution using tortoise-hare algorithm:
            - Time: O(n)
            - Space: O(1)

        Note: the tortoise and hare will always meet in a cycle since
        the hare has a speed 2x that of the tortoise.
        """
        slow = fast = head    

        while fast and fast.next:
            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next.next

        return False

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
        [solution.solution],
        label=__file__
    )
    """
