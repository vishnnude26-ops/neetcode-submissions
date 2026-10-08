class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_pointer, right_pointer = (0, len(nums) - 1)

        while left_pointer <= right_pointer:

            middle_pointer: int = ( left_pointer + right_pointer ) // 2

            if nums[middle_pointer] == target: return middle_pointer
            # In the left sorted array:
            if nums[left_pointer] < nums[middle_pointer]:
                if target > nums[middle_pointer] or target < nums[left_pointer]:
                    left_pointer = middle_pointer + 1
                else: right_pointer = middle_pointer - 1
            # In the right sorted array
            elif nums[left_pointer] > nums[middle_pointer]:
                if target < nums[middle_pointer] or target > nums[right_pointer]:
                    right_pointer = middle_pointer - 1
                else: left_pointer = middle_pointer + 1
            else:
                left_pointer += 1

        return -1