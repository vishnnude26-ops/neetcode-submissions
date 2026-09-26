from typing import Dict
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False
        lookup_dict: Dict = defaultdict(int)

        for current_element in s:
            lookup_dict[current_element] += 1
        
        for current_element in t:
            if current_element in lookup_dict:
                lookup_dict[current_element] -= 1
        
        for value in lookup_dict.values():
            if value != 0:
                return False
        return True