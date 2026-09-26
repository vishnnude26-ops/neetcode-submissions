from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_dict = defaultdict(list)

        for current_element in strs:
            counts: List = [0] * 26

            for i in current_element:
                counts[ord(i) - ord('a')] += 1
        
            freq_dict[tuple(counts)].append(current_element)
        
        return list(freq_dict.values())

