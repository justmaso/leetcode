from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def maxArea(self, height: list[int]) -> int:
        maximum = 0
        left, right = 0, len(height) - 1

        while left < right:
            curr_width = right - left
            left_height, right_height = height[left], height[right]
            curr_height = min(left_height, right_height)
            curr_area = curr_width * curr_height
            maximum = max(curr_area, maximum)

            # determine which pointer to shift
            if left_height <= right_height:
                left += 1
            else:
                right -= 1

        return maximum


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=([1, 8, 6, 2, 5, 4, 8, 3, 7],), expected=49),
        GenericTestCase(input=([1, 1],), expected=1),
    ]

    run_tests(
        test_cases,
        [solution.maxArea],
        label=__file__
    )
