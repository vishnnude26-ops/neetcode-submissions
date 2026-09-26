from typing import Set

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        converted_set: Set = set(nums)
        longest: int = 0

        for index in range(len(nums)):
            if nums[index] - 1 not in converted_set:
                length: int = 1
                while (nums[index] + length) in converted_set:
                    length += 1
                longest = max(longest, length)
                    
        return longest