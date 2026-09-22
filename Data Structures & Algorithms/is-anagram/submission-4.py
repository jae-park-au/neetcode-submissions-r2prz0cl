class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        check = [0] * (ord('z') - ord('a') + 1) 
        for char_s, char_t in zip(s, t):
            check[ord(char_s) - ord('a')] += 1
            check[ord(char_t) - ord('a')] -= 1

        return not any(check)