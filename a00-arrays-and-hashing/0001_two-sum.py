from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def brute_twoSum(self, nums: list[int], target: int) -> list[int]:
        if not nums: return []

        length = len(nums)
        for idx_one in range(length):
            for idx_two in range(length):
                # indices must be distinct
                if idx_one == idx_two: continue
                
                # distinct indices sum to target
                if nums[idx_one] + nums[idx_two] == target:
                    return sorted([idx_one, idx_two])

        return []

    def optimal_twoSum(self, nums: list[int], target: int) -> list[int]:
        if not nums: return []
        value_to_idx = dict()

        for idx, value in enumerate(nums):
            # compute needed value to complement `value`
            complement = target - value

            # complement exists; solution found
            if complement in value_to_idx:
                # no need to sort as this solution is sequential
                return [value_to_idx[complement], idx]
            # complement doesn't exist; add this value to the dict
            else:
                value_to_idx[value] = idx

        return []


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=([2, 7, 11, 15], 9), expected=[0, 1]),
        GenericTestCase(input=([3, 2, 4], 6), expected=[1, 2]),
        GenericTestCase(input=([3, 3], 6), expected=[0, 1])
    ]

    run_tests(
        test_cases,
        [
            solution.brute_twoSum, 
            solution.optimal_twoSum
        ],
        label=__file__
    )
