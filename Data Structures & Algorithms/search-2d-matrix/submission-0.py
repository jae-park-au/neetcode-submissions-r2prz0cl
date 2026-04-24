class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Outer search
        lo, hi = 0, len(matrix)

        while lo < hi:
            mid = (lo + hi) // 2

            if target < matrix[mid][0]:
                hi = mid
            else:
                lo = mid + 1

        if lo > 0:
            outer_target = lo - 1
        else:
            outer_target = lo
        # Lower search
        l, h = 0, len(matrix[outer_target])

        while l < h:
            m = (l + h) // 2

            if target < matrix[outer_target][m]:
                h = m
            else:
                l = m + 1

        if l > 0 and matrix[outer_target][l - 1] == target:
            return True
        return False