from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Given two strings s1 and s2, return True if s2
        contains a permutation of s1, or False otherwise.

        In other words, return True if one of s1's permutations
        is a substring of s2.
        """
        L1, L2 = len(s1), len(s2)

        # no permutation of s1 can exist in s2
        if L1 > L2:
            return False

        # frequency lists of characters
        s1Chars = [0] * 26
        s2Chars = [0] * 26

        # add the first L1 chars to both frequency lists
        for k in range(L1):
            s1Chars[ord(s1[k]) - ord("a")] += 1
            s2Chars[ord(s2[k]) - ord("a")] += 1
       
        # the first L1 chars of s2 is a substring of s1
        if s1Chars == s2Chars:
            return True

        # check each L1-lengthed substrings in s2
        for k in range(L1, L2):
            # remove the leftmost char of the substring
            s2Chars[ord(s2[k - L1]) - ord("a")] -= 1
            
            # add the rightmost char of the substring
            s2Chars[ord(s2[k]) - ord("a")] += 1

            # check if we found a permutation in s2
            if s1Chars == s2Chars:
                return True

        # no substring in s2 is a permutation of s1
        return False


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=("ab", "eidbaooo"), expected=True),
        GenericTestCase(input=("ab", "eidboaoo"), expected=False),
        GenericTestCase(input=("abc", "cadb"), expected=False),
    ]

    run_tests(
        test_cases,
        [solution.checkInclusion],
        label=__file__
    )
