from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def nonoptimal_trapRainWater(self, height: list[int]) -> int:
        """linear memory and time solution"""
        reine = 0
        N = len(height)

        max_left = [0] * N
        max_right = [0] * N

        left_temp = right_temp = 0

        # populate left maxes
        for idx in range(N):
            max_left[idx] = left_temp
            left_temp = max(left_temp, height[idx])

        # populate right maxes
        for idx in range(N - 1, -1, -1):
            max_right[idx] = right_temp
            right_temp = max(right_temp, height[idx])

        for idx in range(N):
            nominal_reine = min(max_left[idx], max_right[idx]) - height[idx]
            reine += max(0, nominal_reine)

        return reine

    def optimal_trapRainWater(self, height: list[int]) -> int:
        """constant memory and linear time solution"""
        reine = 0
        N = len(height)

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                reine += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                reine += right_max - height[right]

        return reine


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],), expected=6),
        GenericTestCase(input=([4, 2, 0, 3, 2, 5],), expected=9),
    ]

    run_tests(
        test_cases,
        [
            solution.nonoptimal_trapRainWater,
            solution.optimal_trapRainWater
        ],
        label=__file__
    )
