class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        valid_triples = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            lo, hi = i + 1, len(nums) - 1

            while lo < hi:
                cur = nums[lo] + nums[hi]

                if cur > target:
                    hi -= 1
                elif cur < target: 
                    lo += 1
                else:
                    valid_triples.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1

                    while nums[lo] == nums[lo - 1] and lo < hi:
                        lo += 1

        return valid_triples
