from __future__ import annotations
from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optiona[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        You are given two non-empty linked lists representing
        non-negative integers. The digits are stored in reverse order,
        and each of their nodes contains a single digit. Add the two
        numbers and return the sum as a linked list.

        You may assume the two numbers do not contain any leading zero,
        except the number 0 itself.
        """
        sum_list = curr = ListNode()
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            curr_sum = v1 + v2 + carry
            curr_digit = curr_sum % 10
            carry = curr_sum // 10

            curr.next = ListNode(curr_digit)

            if l1: l1 = l1.next
            if l2: l2 = l2.next
            curr = curr.next

        curr = sum_list.next
        while curr:
            s = f"{curr.val}->"
            if curr.next == None: s += "None\n"
            print(s, end="")
            curr = curr.next

        return sum_list.next


def list_to_linked_list(lst: list[int]) -> Optional[ListNode]:
    full_list = temp = ListNode()    

    for n in lst:
        temp.next = ListNode(n)
        temp = temp.next

    return full_list.next


if __name__ == "__main__":
    solution = Solution()

    
    solution.addTwoNumbers(
        list_to_linked_list([9, 9, 9, 9, 9, 9, 9]),
        list_to_linked_list([9, 9, 9, 9])
    )
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
