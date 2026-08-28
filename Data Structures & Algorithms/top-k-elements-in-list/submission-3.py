class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        # Populate frequency hashmap
        for num in nums:
            if num not in freqs:
                freqs[num] = 1
            else:
                freqs[num] += 1

        # len(nums) + 1 because max frequency is len(nums), and i want to use 0-based indexing.
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in freqs.items():
            buckets[freq].append(num)

        # Go from end of list and get top k most frequent elements
        top_k = []
        for i in range(len(nums), -1, -1):
            for num in buckets[i]:
                top_k.append(num)

                if len(top_k) == k:
                    return top_k

        