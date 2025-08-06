from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def invalidFindDuplicate(self, nums: list[int]) -> int:
        """
        An invalid solution to findDuplicate since it modifies
        the passed list.

        Achieves optimal time and space complexities, but violates
        the problem contstraints of leaving the list as read-only.

        Time: O(n)
        Space: O(1)
        """
        N = len(nums)
        duplicate = int()

        # find the duplicate
        for idx in range(N):
            curr = abs(nums[idx])
            mapping = nums[curr]

            # curr has been seen before
            if mapping < 0:
                duplicate = curr
                break
            
            # mark curr as seen
            nums[curr] *= -1

        # unmark all values
        for idx in range(N):
            nums[idx] = abs(nums[idx])

        return duplicate

    def findDuplicate(self, nums: list[int]) -> int:
        """
        Given an array of integers nums containing n + 1
        integers where each integer is in the range [1, n],
        return the repeated number.

        NOTE: There is only ever one repeated number in nums.

        You must solve the problem without modifying the list nums
        and using only constant extra space
        """
        slow = fast = 0

        # keep going until slow and fast intersect
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0

        # keep going until slow and slow2 intersect
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                break

        return slow


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=([1, 3, 4, 2, 2],), expected=2),
        GenericTestCase(input=([3, 1, 3, 4, 2],), expected=3),
        GenericTestCase(input=([3, 3, 3, 3, 3],), expected=3),
    ]

    run_tests(
        test_cases,
        [
            solution.invalidFindDuplicate,
            solution.findDuplicate
        ],
        label=__file__
    )
