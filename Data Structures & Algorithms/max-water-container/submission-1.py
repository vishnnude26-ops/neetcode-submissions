class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_pointer, right_pointer = 0, len(heights) - 1
        result: int = 0

        while left_pointer < right_pointer:
            current_result = (
                    min(heights[left_pointer], heights[right_pointer])
                ) * (right_pointer - left_pointer)
            
            if heights[left_pointer] < heights[right_pointer]: left_pointer += 1
            else: right_pointer -= 1
            
            result = max(current_result, result)
        return result

