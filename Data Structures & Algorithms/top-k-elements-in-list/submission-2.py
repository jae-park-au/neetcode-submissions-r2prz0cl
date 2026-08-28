class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for _ in range(len(nums) + 1)]

        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        for num, freq in count.items():
            freqs[freq].append(num)

        return_list = []
        for i in range(len(nums), -1 , -1):
            for n in freqs[i]:
                return_list.append(n)
                if len(return_list) == k:
                    return return_list
