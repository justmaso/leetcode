from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def bruteContainsDuplicate(self, nums: list[int]) -> bool:
        """
        Brute force solution to containsDuplicate that just
        checks every single pair.

        Time: O(n^2)
        Space: O(1)
        """
        N = len(nums)

        for left in range(N):
            for right in range(left + 1, N):
                if nums[left] == nums[right]:
                    return True

        return False

    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Given an integer array nums, return True if any
        value appears at least twice in the array, and
        return False if every element is distinct.
        """

        """
        Optimal solution using a hash set to track seen
        values.
        
        Time: O(n)
        Space: O(n)
        """
        seen = set()
        
        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=([1, 2, 3, 1],), expected=True),
        GenericTestCase(input=([1, 2, 3, 4],), expected=False),
        GenericTestCase(input=([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],), expected=True),
        GenericTestCase(input=([],), expected=False),
    ]

    run_tests(
        test_cases,
        [
            solution.containsDuplicate,
            solution.bruteContainsDuplicate
        ],
        label=__file__
    )
