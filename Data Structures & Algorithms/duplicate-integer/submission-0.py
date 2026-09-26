from typing import Dict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contains_dict: Dict = {}

        for index, current_num in enumerate(nums):
            if current_num in contains_dict: return True
            contains_dict[current_num] = index
        return False