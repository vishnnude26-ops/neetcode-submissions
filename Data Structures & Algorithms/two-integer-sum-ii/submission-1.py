class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left_pointer, right_pointer = 0, len(numbers) - 1
        while left_pointer < right_pointer:
            current_sum: int = numbers[left_pointer] + numbers[right_pointer]
            if current_sum == target: return [left_pointer + 1, right_pointer + 1]
            elif current_sum < target: left_pointer += 1
            else: right_pointer -= 1
        return []