from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def brute_dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        Brute force solution that has the following complexities:
            - Time: O(n^2)
            - Space: O(1)
        """
        N = len(temperatures)
        daysUntilWarmer = [0] * N

        for outer_idx in range(N):
            for inner_idx in range(outer_idx + 1, N):
                left, right = temperatures[outer_idx], temperatures[inner_idx]
                
                # warmer temperature found
                if left < right:
                    daysUntilWarmer[outer_idx] = inner_idx - outer_idx
                    break # end the search
                
                # continue searching for a warmer temp

        return daysUntilWarmer

    def optimal_dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        Optimal solution that has the following complexities:
            - Time: O(n)
            - Space: O(n)
        """
        if not temperatures: return []

        daysUntilWarmer = [0] * len(temperatures)
        oldTemps = []

        for idx, temp in enumerate(temperatures):
            # solutions found for older temps in the stack
            while oldTemps and temp > oldTemps[-1][1]:
                oldIdx = oldTemps.pop()[0]
                daysUntilWarmer[oldIdx] = idx - oldIdx

            # add the current temperature to the stack
            oldTemps.append((idx, temp))

        return daysUntilWarmer
            


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=([73, 74, 75, 71, 69, 72, 76, 73],), expected=[1, 1, 4, 2, 1, 1, 0, 0]),
        GenericTestCase(input=([30, 40, 50, 60],), expected=[1, 1, 1, 0]),
        GenericTestCase(input=([30, 60, 90],), expected=[1, 1, 0]),
    ]

    run_tests(
        test_cases,
        [
            solution.brute_dailyTemperatures,
            solution.optimal_dailyTemperatures
        ],
        label=__file__
    )
