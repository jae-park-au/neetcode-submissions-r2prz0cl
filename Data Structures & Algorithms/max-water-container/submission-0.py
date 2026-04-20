class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        cur_max = (right - left) * min(heights[right], heights[left])
        
        while left < right:
            if heights[left] < heights[right]: 
                left += 1
            else:
                right -= 1

            cur_max = max(cur_max, (right - left) * min(heights[right], heights[left]))

        return cur_max
            
            