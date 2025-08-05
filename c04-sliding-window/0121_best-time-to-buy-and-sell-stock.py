from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        You are given an array prices where prices[i]
        is the price of a given stock on the ith day.

        You want to maximize your profit by choosing
        a single day to buy one stock and choosing a
        different day in the future to sell that stock.

        Return the maximum profit you can achieve from 
        this transaction. If you cannot achieve any profit,
        return 0.
        """
        maxP = 0
        entry = prices[0]

        for k in range(1, len(prices)):
            currPrice = prices[k]

            # new local minimum found
            if currPrice < entry:
                entry = currPrice

            maxP = max(maxP, currPrice - entry)

        return maxP


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=([7, 1, 5, 3, 6, 4],), expected=5),
        GenericTestCase(input=([7, 6, 4, 3, 1],), expected=0),
    ]

    run_tests(
        test_cases,
        [solution.maxProfit],
        label=__file__
    )
