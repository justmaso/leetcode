from utils.bootstrap import rootify
rootify()
from utils.tester import GenericTestCase, run_tests


class Solution:
    def bruteMinEatingSpeed(self, piles: list[int], h: int) -> int:
        """
        Brute force solution to `minEatingSpeed`.

        Time complexity: O(M * n) where `M = max(piles)`
        Space complexity: O(1)
        """
        import math
        currentK, upperK = 1, max(piles)

        # just check every possible eating speed k
        while True:
            hours = 0
            for p in piles:
                hours += math.ceil(p / currentK)

            # optimal eating speed found
            if hours <= h:
                # this will always return the optimal k since we start
                # from the smallest possible k and increase by one if
                # we're eating too slow at the currentK
                return currentK
            # eating too slow
            else:
                currentK += 1
        
        return optimalK

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """
        Koko loves to eat bananas. There are `n` piles of bananas, the
        `ith` pile has `piles[i]` bananas. The guards have gone and will
        come back in `h` hours.

        Koko can decide her bananas-per-hour eating speed of `k`. Each hour,
        she chooses some pile of bananas and eats `k` bananas from that pile. 
        If the pile has less than `k` bananas, she eats all of them instead 
        and will not eat any more bananas during this hour.

        Koko likes to eat slowly but still wants to finish eating 
        all the bananas before the guards return.

        Return the minimum integer `k` such that she can eat all the
        bananas within `h` hours.
        """

        """
        Optimal solution that uses binary search from 1 to the max in the pile
        of bananas.

        Intuition:
            - The upper bound is just the max banana pile in `piles`.
                - True since `piles.length <= h` (LeetCode constraints)
        
        Time complexity: O(n * log(M)) where `M = max(piles)`
        Space complexity: O(1)
        """

        import math
        maxInPile = max(piles)
        optimalK = maxInPile

        lowerK, upperK = 1, maxInPile
        while lowerK <= upperK:
            midK = lowerK + (upperK - lowerK) // 2
            hours = 0

            for p in piles:
                # += bananas / (bananas per hour) 
                hours += math.ceil(p / midK)
            
            # eating too fast; decrease k (not maximizing time)
            if hours <= h:
                optimalK = min(optimalK, midK)
                upperK = midK - 1
            # eating too slow; increase k
            else:
                lowerK = midK + 1
                
        return optimalK


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        GenericTestCase(input=([3, 6, 7, 11], 8), expected=4),
        GenericTestCase(input=([30, 11, 23, 4, 20], 5), expected=30),
        GenericTestCase(input=([30, 11, 23, 4, 20], 6), expected=23),
    ]

    run_tests(
        test_cases,
        [
            solution.bruteMinEatingSpeed,
            solution.minEatingSpeed
        ],
        label=__file__
    )
