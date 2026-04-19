class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s, l = 0, len(numbers) - 1

        while s < l:
            cur = numbers[s] + numbers[l] 

            if cur == target:
                return [s + 1, l + 1]
            elif cur < target:
                s += 1
            elif cur > target:
                l -= 1