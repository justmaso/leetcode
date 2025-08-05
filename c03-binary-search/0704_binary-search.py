from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        targetIdx = -1
        left, right = 0, len(nums) - 1

        # need unstrict comparison for odd case
        while left <= right:
            # bad practice due to potential int overflow
            # midpoint = (left + right) // 2

            # avoids potetnial int overflow from left + right
            midpoint = left + (right - left) // 2
            midval = nums[midpoint]

            if midval == target:
                targetIdx = midpoint
                break
            elif midval < target:
                left = midpoint + 1
            else:
                right = midpoint - 1

        return targetIdx
        


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=([-1, 0, 3, 5, 9, 12], 9), expected=4),
        GenericTestCase(input=([-1, 0, 3, 5, 9, 12], 2), expected=-1),
        GenericTestCase(input=([5], 5), expected=0),
        GenericTestCase(input=([5], 3), expected=-1),
        GenericTestCase(input=([1, 3], 1), expected=0),
        GenericTestCase(input=([1, 3], 3), expected=1),
        GenericTestCase(input=([1, 3], 2), expected=-1),
        GenericTestCase(input=([1, 2, 3, 4, 5], 3), expected=2),
        GenericTestCase(input=([-10, -5, 0, 3, 9], -10), expected=0),
        GenericTestCase(input=([-10, -5, 0, 3, 9], 9), expected=4),
        GenericTestCase(input=([-10, -5, 0, 3, 9], 7), expected=-1),
        GenericTestCase(input=([], 1), expected=-1),
        GenericTestCase(input=(list(range(58)), 57), expected=57),
        GenericTestCase(input=(list(range(333)), -1), expected=-1),
    ]

    run_tests(
        test_cases,
        [solution.search],
        label=__file__
    )
