from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length: int = len(nums)
        result: List = [1] * length

        prefix: int = 1
        for index in range(length):
            result[index] *= prefix
            prefix *= nums[index]
        
        suffix: int = 1
        for index in range(length - 1, -1, -1):
            result[index] *= suffix
            suffix *= nums[index]
        
        return result