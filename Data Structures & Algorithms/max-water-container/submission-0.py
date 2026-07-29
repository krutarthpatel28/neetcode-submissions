class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_content = 0
        while left < right:
            min_height = min(heights[left], heights[right])
            current_content = min_height * (right - left)
            max_content = max(max_content, current_content)
            if min_height == heights[left]:
                left += 1
            else:
                right -= 1
        return max_content