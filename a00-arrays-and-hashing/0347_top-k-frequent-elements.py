from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # add one extra as frequency is inclusive of length
        # frequencies = [[]] * (len(nums) + 1) DOESN'T CREATE INDEPENDENT LISTS
        frequencies = [[] for _ in range(len(nums) + 1)]

        from collections import defaultdict
        counts = defaultdict(int)

        # count each element
        for n in nums:
            counts[n] += 1

        # populate frequencies list
        # (i.e., frequencies[1] will contain the numbers that occur once)
        for n, count in counts.items():
            frequencies[count].append(n)

        result = []
        for idx in range(len(nums), -1, -1):
            for n in frequencies[idx]:
                result.append(n)
                if len(result) == k:
                    return sorted(result)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=([1, 1, 1, 2, 2, 3], 2), expected=[1, 2]),
        GenericTestCase(input=([1], 1), expected=[1]),
        GenericTestCase(input=([3, 0, 1, 0], 1), expected=[0]),
    ]

    run_tests(
        test_cases,
        [solution.topKFrequent],
        label=__file__
    )
