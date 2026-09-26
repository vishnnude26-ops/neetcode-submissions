from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length: int = len(nums) - 1
        result_list: List = []

        for index, current_element in enumerate(nums):
            if index > 0 and nums[index] == nums[index - 1]: continue

            left_pointer, right_pointer = index + 1, length
            while left_pointer < right_pointer:
                current_sum: int = (current_element + nums[left_pointer] + nums[right_pointer])
                if current_sum < 0: left_pointer += 1
                elif current_sum > 0: right_pointer -= 1
                else:
                    result_list.append([current_element, nums[left_pointer], nums[right_pointer]])
                    left_pointer += 1
                    while left_pointer < right_pointer and nums[left_pointer] == nums [left_pointer - 1]:
                        left_pointer += 1
        
        return result_list