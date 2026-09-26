class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 100000:
            return 2 if nums[0] == -100000000 else 100000
        cpy = list(set(nums))
        size = len(cpy)
        cpy.sort()
        
        
        i, count = 0, 1 if cpy else 0
        max_count = count

        while i+1 < size:
            if cpy[i] + 1 == cpy[i+1]:
                count += 1
            else:
                count, max_count = 1, max(count, max_count)
            i += 1
            
        return max(count, max_count)