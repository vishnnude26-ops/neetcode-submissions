from typing import List, Dict
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        storage_list: List = [[] for x in range(len(nums) + 1)] 
        freq_dict: Dict = defaultdict(int)
        
        """
            Creating the frequency dictionary - so that 
            we can store the element in the respective  index of storage_list
        """
        for x in nums: freq_dict[x] += 1
        for current_element, index in freq_dict.items():
            storage_list[index].append(current_element)

        result: List = []
        for index in range(len(storage_list)-1, -1, -1):
            for element in storage_list[index]:
                result.append(element)
                if k == len(result): return result
