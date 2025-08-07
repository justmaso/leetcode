from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    @staticmethod
    def normalize_groups(groups: list[list[str]]) -> list[list[str]]:
        return sorted(sorted(group) for group in groups)

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Given an array of strings strs, group the angrams
        together. The answer can be returned in any order
        """

        """
        Optimal solution that uses a dictionary that uses words
        as keys (i.e., list of characters) and maps them to a list
        containing the anagrams with those characters.

        Time: O(n)
        Space: O(n * k) where k is the length of the longest word in strs
        """
        from collections import defaultdict
        groups = defaultdict(list)

        for word in strs:
            mapping = [0] * 26
            for char in word:
                mapping[ord(char) - ord("a")] += 1

            # wrap in tuple since lists aren't hashable
            groups[tuple(mapping)].append(word)

        return self.normalize_groups(list(groups.values()))


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(
            input=(["eat", "tea", "tan", "ate", "nat", "bat"],),
            expected=Solution.normalize_groups([
                ["bat"],
                ["nat", "tan"],
                ["ate", "eat", "tea"]
            ])
        ),
        GenericTestCase(
            input=([""],),
            expected=Solution.normalize_groups([
                [""]
            ])
        ),
        GenericTestCase(
            input=(["a"],),
            expected=Solution.normalize_groups([
                ["a"]
            ])
        ),
        GenericTestCase(
            input=(["", ""],),
            expected=Solution.normalize_groups([
                ["", ""]
            ])
        ),
        GenericTestCase(
            input=(["abc", "bca", "cab", "xyz", "zyx", "yxz", "foo"],),
            expected=Solution.normalize_groups([
                ["abc", "bca", "cab"],
                ["xyz", "zyx", "yxz"],
                ["foo"]
            ])
        ),
        GenericTestCase(
            input=(["listen", "silent", "enlist", "google", "gogole"],),
            expected=Solution.normalize_groups([
                ["listen", "silent", "enlist"],
                ["google", "gogole"]
            ])
        ),
    ]

    run_tests(
        test_cases,
        [solution.groupAnagrams],
        label=__file__
    )
