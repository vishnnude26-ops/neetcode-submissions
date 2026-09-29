class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left_pointer = 1
        right_pointer = max(piles)
        
        while left_pointer < right_pointer:

            middle_pointer = (left_pointer + right_pointer) // 2
            current_time = self.k_works(piles, middle_pointer)
            
            if current_time <= h: right_pointer = middle_pointer
            else: left_pointer = middle_pointer + 1

        return left_pointer

    def k_works(self, piles, currrent_k):
        time_taken: int = 0
        for current_pile in piles:
            time_taken += math.ceil(current_pile / currrent_k)
        return time_taken


