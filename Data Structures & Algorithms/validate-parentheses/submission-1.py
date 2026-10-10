from typing import Dict

class Solution:
    def isValid(self, s: str) -> bool:
        
        mapping_dict: Dict = {"]": "[", ")" : "(", "}" : "{"}
        stack: List = []

        for current_element in s:
            if current_element in mapping_dict:
                if stack and stack[-1] == mapping_dict[current_element]:
                    stack.pop()
                else: return False
            else:
                stack.append(current_element)
        
        return len(stack) == 0
        