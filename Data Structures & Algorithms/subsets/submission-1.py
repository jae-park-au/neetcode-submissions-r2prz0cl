class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return_list = []
        MAX_DEPTH = len(nums)

        def backtrack(cur_state: list, depth: int):
            if depth == MAX_DEPTH:
                return_list.append(cur_state)
                return

            backtrack(cur_state, depth + 1)

            next_state = cur_state + [nums[depth]]
            backtrack(next_state, depth + 1)

        backtrack([], 0)

        return return_list