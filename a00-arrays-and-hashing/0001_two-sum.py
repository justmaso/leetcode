from dataclasses import dataclass


def brute_twoSum(nums: list[int], target: int) -> list[int]:
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


def optimal_twoSum(nums: list[int], target: int) -> list[int]:
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


@dataclass
class TestCase:
    nums: list[int]
    target: int
    expected: list[int]


def run_tests():
    test_cases = [
        TestCase(nums=[2, 7, 11, 15], target=9, expected=[0, 1]),
        TestCase(nums=[3, 2, 4], target=6, expected=[1, 2]),
        TestCase(nums=[3, 3], target=6, expected=[0, 1])
    ]

    solutions = [
        brute_twoSum,
        optimal_twoSum
    ]

    for idx, case in enumerate(test_cases):
        print(f"case {idx}: ({case.nums}, {case.target}) -> {case.expected}")

        for solution in solutions:
            result = solution(case.nums, case.target)
            passed = result == case.expected
            status = "+" if passed else f"- (got {result})"
            print(f"\t{status}{solution.__name__}")

if __name__ == "__main__":
    run_tests()

