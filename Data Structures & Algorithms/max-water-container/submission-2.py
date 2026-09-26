class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_pointer, right_pointer = 0, len(heights) - 1
        max_volume: int = 0

        while left_pointer < right_pointer:
            current_volume: int = min(heights[left_pointer], heights[right_pointer]) * (right_pointer - left_pointer)

            max_volume = max(max_volume, current_volume)
            if heights[left_pointer] < heights[right_pointer]: left_pointer += 1
            else: right_pointer -= 1
        return max_volume
