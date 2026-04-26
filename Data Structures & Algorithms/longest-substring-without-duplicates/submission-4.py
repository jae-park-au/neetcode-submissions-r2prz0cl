class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        lo, hi = 0, 0
        cur_max = 0

        while hi < len(s):
            while s[hi] in seen:
                seen.remove(s[lo])
                lo += 1
                
            cur_max = max(cur_max, hi - lo + 1)
            seen.add(s[hi])
            hi += 1

        return cur_max