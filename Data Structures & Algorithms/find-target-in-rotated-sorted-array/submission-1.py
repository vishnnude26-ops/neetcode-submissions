class Solution:
    def search(self, nums: List[int], target: int) -> int:
        input = nums
        left_pointer, right_pointer = (0, len(input) - 1)
        while left_pointer <= right_pointer:
            middle_pointer: int = (left_pointer + right_pointer) // 2
            if input[middle_pointer] == target: return middle_pointer

            # In the left sorted array:
            if input[left_pointer] < input[middle_pointer]:
                  if target > input[middle_pointer] or target < input[left_pointer]: left_pointer = middle_pointer + 1
                  else: right_pointer = middle_pointer - 1
            # In the right sorted array:
            elif input[left_pointer] > input[middle_pointer]:
                  if target < input[middle_pointer] or target > input[right_pointer]: right_pointer = middle_pointer - 1
                  else: left_pointer = middle_pointer + 1
            else: left_pointer += 1
        return -1