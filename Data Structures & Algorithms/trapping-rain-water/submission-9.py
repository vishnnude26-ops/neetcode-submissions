class Solution:
    def trap(self, height: List[int]) -> int:
      input = height
      left_pointer, right_pointer = 0, len(input) - 1
      max_left, max_right = input[left_pointer], input[right_pointer]
      max_water_stored: int = 0

      while left_pointer < right_pointer:
            if max_left <= max_right:
                  left_pointer += 1
                  max_left = max(max_left, input[left_pointer])
                  max_water_stored += (max_left - input[left_pointer])
            else:
                  right_pointer -= 1
                  max_right = max(max_right, input[right_pointer])
                  max_water_stored += (max_right - input[right_pointer])
      return max_water_stored