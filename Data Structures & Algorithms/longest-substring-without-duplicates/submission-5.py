class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()   # char : index
        lo, hi = 0, 0
        cur_max = 0

        while hi < len(s):
            if s[hi] in seen and seen[s[hi]] >= lo:
                lo = seen[s[hi]] + 1
            seen[s[hi]] = hi
            cur_max = max(cur_max, hi - lo + 1)
            hi += 1
            
        return cur_max