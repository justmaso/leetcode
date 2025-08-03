from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # trivial case; different lengths
        if len(s) != len(t):
            return False

        from collections import defaultdict
        s_map, t_map = defaultdict(int), defaultdict(int)
        N = len(s)

        for idx in range(N):
            s_map[s[idx]] += 1
            t_map[t[idx]] += 1

        return s_map == t_map


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=("anagram", "nagaram"), expected=True),
        GenericTestCase(input=("rat", "car"), expected=False),
        GenericTestCase(input=("", ""), expected=True),
        GenericTestCase(input=(" ", " "), expected=True),
        GenericTestCase(input=("a", "A"), expected=False),
        GenericTestCase(input=("AA", "LLL"), expected=False),
    ]

    run_tests(
        test_cases,
        [solution.isAnagram],
        label=__file__
    )
