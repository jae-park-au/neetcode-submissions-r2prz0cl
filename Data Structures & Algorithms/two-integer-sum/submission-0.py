class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if nums[i] in diff_map:
                return [diff_map[nums[i]], i]
            else:
                diff_map[diff] = i

        