from collections import defaultdict
from typing import Dict, List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_dict: Dict = defaultdict(list)
        
        for current_element in strs:
            sorted_element: str = ''.join(sorted(current_element))
            freq_dict[sorted_element].append(current_element)
        return list(freq_dict.values())
        