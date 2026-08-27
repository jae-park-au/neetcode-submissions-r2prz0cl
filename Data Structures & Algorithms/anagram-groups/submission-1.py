class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}

        for s in strs:
            count_arr = [0] * 26
            for char in s: 
                count_arr[ord(char) - ord('a')] += 1

            count_key = tuple(count_arr)
            if count_key not in check:
                check[count_key] = [s]
            else:
                check[count_key].append(s)

        return list(check.values())