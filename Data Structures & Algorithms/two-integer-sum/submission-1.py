from collections import defaultdict
from typing import Dict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup_dict: Dict = defaultdict(int)

        for index, current_element in enumerate(nums):
            difference: int = (target - current_element)
            if difference in lookup_dict:
                return [lookup_dict[difference], index]

            lookup_dict[current_element] = index
        return []