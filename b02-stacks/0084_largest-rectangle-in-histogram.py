from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        largestArea = 0
        stack = []  # [(idx, height)]

        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                oldIdx, oldHeight = stack.pop()
                largestArea = max(largestArea, oldHeight * (idx - oldIdx))
                start = oldIdx

            stack.append((start, height))

        for idx, height in stack:
            largestArea = max(largestArea, height * (len(heights) - idx))

        return largestArea


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=([2, 1, 5, 6, 2, 3],), expected=10),
        GenericTestCase(input=([2, 4],), expected=4),
    ]

    run_tests(
        test_cases,
        [solution.largestRectangleArea],
        label=__file__
    )
