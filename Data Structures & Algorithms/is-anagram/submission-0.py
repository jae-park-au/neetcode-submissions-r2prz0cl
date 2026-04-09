class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ref_set = {}

        for char_s, char_t in zip(s, t):
            if char_s not in ref_set:
                ref_set[char_s] = 1
            else:
                ref_set[char_s] += 1

            if char_t not in ref_set:
                ref_set[char_t] = -1
            else:
                ref_set[char_t] -= 1

        return not any(ref_set.values())

        