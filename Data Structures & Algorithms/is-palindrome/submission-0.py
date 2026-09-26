class Solution:
    def isPalindrome(self, s: str) -> bool:
        concatenated_string: str = ""

        for current_character in s:
            if current_character.isalnum():
                concatenated_string += current_character.lower()
        
        left_pointer, right_pointer = 0, len(concatenated_string) - 1
        
        while left_pointer < right_pointer:
            if concatenated_string[left_pointer] != concatenated_string[right_pointer]: return False
            left_pointer += 1
            right_pointer -= 1
        return True