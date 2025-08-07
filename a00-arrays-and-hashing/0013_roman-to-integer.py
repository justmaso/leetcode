from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def oldRomanToInt(self, s: str) -> int:
        """
        Given a valid roman numeral, convert it
        it to an integer
        """
        numeral_to_value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        pre_numerals = {
            "I": ["V", "X"],
            "X": ["L", "C"],
            "C": ["D", "M"]
        }

        total = 0
        last_added = str()

        for roman_numeral in s:
            if last_added in pre_numerals and roman_numeral in pre_numerals[last_added]:
                total -= 2 * numeral_to_value[last_added]
            
            total += numeral_to_value[roman_numeral]
            last_added = roman_numeral

        return total

    def romanToInt(self, s: str) -> int:
        """
        Given a valid roman numeral, convert it to
        an integer.
        """
        # largest to smallest: add them up
        # smaller before larger: subtract smaller
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        N = len(s)
        total = 0

        for k in range(N):
            numeral = s[k]
            value = roman[numeral]

            if k + 1 < N and value < roman[s[k + 1]]:
                total -= value
            else:
                total += value

        return total


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=("III",), expected=3),
        GenericTestCase(input=("IV",), expected=4),
        GenericTestCase(input=("IX",), expected=9),
        GenericTestCase(input=("LVIII",), expected=58),
        GenericTestCase(input=("MCMXCIV",), expected=1994),
        GenericTestCase(input=("XL",), expected=40),
        GenericTestCase(input=("XC",), expected=90),
        GenericTestCase(input=("CD",), expected=400),
        GenericTestCase(input=("CM",), expected=900),
        GenericTestCase(input=("MMMCMXCIX",), expected=3999),
        GenericTestCase(input=("I",), expected=1),
        GenericTestCase(input=("II",), expected=2),
        GenericTestCase(input=("VI",), expected=6),
        GenericTestCase(input=("VII",), expected=7),
        GenericTestCase(input=("VIII",), expected=8),
        GenericTestCase(input=("XIII",), expected=13),
        GenericTestCase(input=("XIV",), expected=14),
        GenericTestCase(input=("XIX",), expected=19),
        GenericTestCase(input=("XX",), expected=20),
        GenericTestCase(input=("XLIX",), expected=49),
        GenericTestCase(input=("L",), expected=50),
        GenericTestCase(input=("XCIX",), expected=99),
        GenericTestCase(input=("C",), expected=100),
        GenericTestCase(input=("D",), expected=500),
        GenericTestCase(input=("M",), expected=1000),
        GenericTestCase(input=("MDCCLXXVI",), expected=1776),
        GenericTestCase(input=("MMXXIV",), expected=2024),
        GenericTestCase(input=("MMMDLXXXVIII",), expected=3588),
    ]

    run_tests(
        test_cases,
        [
            solution.oldRomanToInt,
            solution.romanToInt
        ],
        label=__file__
    )
