import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        while lo < hi:
            k = (lo + hi) // 2

            val = sum([math.ceil(x / k) for x in piles])
            if val <= h:
                hi = k
            else:
                lo = k + 1

        return lo