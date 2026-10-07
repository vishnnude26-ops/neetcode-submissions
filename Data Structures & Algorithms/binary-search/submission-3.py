class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left_pointer, right_pointer = 0, len(nums) - 1
        while left_pointer <= right_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2
            if nums[middle_pointer] == target: return middle_pointer
            elif nums[middle_pointer] < target: left_pointer = middle_pointer + 1
            else: right_pointer = middle_pointer - 1
        return -1