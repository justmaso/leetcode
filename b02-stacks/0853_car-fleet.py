from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        stack = []

        # loop from furthest to closest to target
        for p, s in sorted(pairs)[::-1]:
            stack.append((target - p) / s)
            
            # car behind caught up to fleet ahead (before or at target)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # this car becomes a part of the fleet ahead
                stack.pop()

                # no need to handle speed since a car catching up
                # implies it's faster than a car ahead
                # (it's handled by the algorithm)

        return len(stack)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]), expected=3),
        GenericTestCase(input=(10, [3], [3]), expected=1),
        GenericTestCase(input=(100, [0, 2, 4], [4, 2, 1]), expected=1),
    ]

    run_tests(
        test_cases,
        [solution.carFleet],
        label=__file__
    )
