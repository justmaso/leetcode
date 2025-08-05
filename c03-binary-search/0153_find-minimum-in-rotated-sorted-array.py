from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def bruteFindMin(self, nums: list[int]) -> int:
        """
        Brute force solution. Literally just iterate through
        the entire list.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        currentMin = nums[0]

        for k in range(1, len(nums)):
            currentMin = min(currentMin, nums[k])

        return currentMin

    def findMin(self, nums: list[int]) -> int:
        """
        Suppose an array of length n sorted in ascending
        order is rotated between 1 and n times. For example,
        the array nums = [0,1,2,4,5,6,7] might become:
            - [4,5,6,7,0,1,2] if it was rotated 4 times.
            - [0,1,2,4,5,6,7] if it was rotated 7 times.

        Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] one
        time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

        Given the sorted rotated array nums of unique elements, return
        the minimum element of this array.

        You must write an algorithm that runs in O(log n) time.
        """
        
        """
        Rough thoughts:
            - Can't use the start of a sequence since sequentiality isn't a constraint.
            - Maybe use binary search to find where the sequence "splits".
        """
        left, right = 0, len(nums) - 1
        minElement = nums[left]

        while left <= right:
            mid = left + (right - left) // 2
            leftValue, midValue, rightValue = nums[left], nums[mid], nums[right]

            # the current pointers form a sorted subset
            if leftValue < rightValue:
                minElement = min(minElement, nums[left])
                break

            minElement = min(minElement, midValue)
            
            # if left half is sorted, the pivot is in the rightward portion
            if leftValue <= midValue:
                left = mid + 1
            # otherwise, the rotation is in the leftward portion
            else:
                r = mid - 1

        return minElement


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=([3, 4, 5, 1, 2],), expected=1),
        GenericTestCase(input=([4, 5, 6, 7, 0, 1, 2],), expected=0),
        GenericTestCase(input=([11, 13, 15, 17],), expected=11),
    ]

    run_tests(
        test_cases,
        [
            solution.bruteFindMin,
            solution.findMin
        ],
        label=__file__
    )
