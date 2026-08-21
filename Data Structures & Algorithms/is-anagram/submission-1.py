class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        check = [0] * 26
        for char_c, char_t in zip(s, t):
            check[ord(char_c) - 97] += 1
            check[ord(char_t) - 97] -= 1

        return not sum(map(lambda x: x if x >= 0 else 0, check))