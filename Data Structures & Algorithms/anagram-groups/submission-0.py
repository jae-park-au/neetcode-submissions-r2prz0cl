class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {} # key -> list[str]

        for string in strs:
            key = tuple(self.char_count(string))
            if key not in anagram_groups.keys():
                anagram_groups[key] = [string]
            else:
                anagram_groups[key].append(string)

        return list(anagram_groups.values())
            
    def char_count(self, string: str) -> list[int]:
        char_count = [0] * 26

        for char in string:
            char_count[ord(char) - 97] += 1

        return char_count
