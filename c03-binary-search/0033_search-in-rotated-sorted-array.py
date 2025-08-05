from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def bruteSearch(self, nums: list[int], target: int) -> int:
        """
        Brute force solution that just searches through the
        entire list.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        for k in range(len(nums)):
            if nums[k] == target: return k

        return -1

    def search(self, nums: list[int], target: int) -> int:
        """
        There is an integer array nums sorted in ascending
        order (with distinct values).

        Prior to being passed to your function, nums is possibly
        rotated at an unknown pivot index k (1 <= k < nums.length)
        such that the resulting array is [nums[k], nums[k+1], ...,
        nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
        For example, [0,1,2,4,5,6,7] might be rotated at pivot index
        3 and become [4,5,6,7,0,1,2].

        Given the array nums after the possible rotation and an integer
        target, return the index of target if it is in nums, or
        -1 if it is not in nums.

        You must write an algorithm with O(log n) runtime complexity.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left ) // 2
            leftValue, midValue, rightValue = nums[left], nums[mid], nums[right]

            # target found
            if target == midValue:
                return mid
            
            # left portion is sorted
            if leftValue <= midValue:
                # search the right since the target isn't in this portion
                if midValue < target or target < leftValue:
                    left = mid + 1
                # target is in this left portion; search it
                else:
                    right = mid - 1
            # right portion is sorted
            else:
                # search the left since the target isn't in this portion
                if target < midValue or rightValue < target:
                    right = mid - 1
                # target is in this right portion; search it
                else:
                    left = mid + 1

        return -1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=([4, 5, 6, 7, 0, 1, 2], 0), expected=4),
        GenericTestCase(input=([4, 5, 6, 7, 0, 1, 2], 3), expected=-1),
        GenericTestCase(input=([1], 0), expected=-1),
    ]

    run_tests(
        test_cases,
        [
            solution.bruteSearch,
            solution.search
        ],
        label=__file__
    )
